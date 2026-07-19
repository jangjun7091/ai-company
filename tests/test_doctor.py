"""Tests for scripts/doctor.py.

Only the live-repo PASS test touches the real tree: doctor must pass on
the shipped template and on any correctly configured fork, so that check
stays green after founders fill in their documents. Failure cases use
throwaway fixture trees.
"""
from __future__ import annotations

from pathlib import Path
import importlib.util
import tempfile
import unittest

REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "doctor.py"
spec = importlib.util.spec_from_file_location("doctor_module", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)

MINIMAL_MANIFEST = """\
lifecycle:
  stages:
    - uninitialized
    - discovery
  portfolio_stages:
    - formation
"""

MINIMAL_ESCALATION_SCHEMA = """\
{
  "properties": {
    "trigger": {"enum": ["missing_input", "repeated_failure"]}
  }
}
"""


class DoctorTests(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)

    def write(self, relative: str, content: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_doctor_passes_on_live_repo(self) -> None:
        self.assertEqual(module.collect_errors(REPO_ROOT), [])

    def test_workflow_templates_required(self) -> None:
        # The templates the workflows build artifacts from must be REQUIRED,
        # so deleting one fails doctor instead of silently breaking a step.
        errors = module.collect_errors(self.root)
        for relative in (
            "templates/idea-brief.md",
            "templates/product-spec.md",
            "templates/adr.md",
            "templates/incident.md",
            "templates/research-note.md",
        ):
            self.assertIn(f"missing: {relative}", errors)

    def test_invalid_stage_reported(self) -> None:
        self.write("ai-company.yaml", MINIMAL_MANIFEST)
        self.write(
            "company/state/project-state.yaml",
            "stage: bogus # not a lifecycle stage\n",
        )
        errors = module.collect_errors(self.root)
        self.assertTrue(
            any("stage 'bogus'" in error for error in errors),
            f"expected a stage error in {errors}",
        )

    def test_agent_vocab_mismatch_reported(self) -> None:
        self.write("ai-company.yaml", MINIMAL_MANIFEST)
        self.write(
            "company/schemas/escalation.schema.json", MINIMAL_ESCALATION_SCHEMA
        )
        self.write(
            "company/agents/product-engineering.yaml",
            "id: product-engineering\nmandatory_escalation:\n- high_impact_action\n",
        )
        errors = module.collect_errors(self.root)
        self.assertTrue(
            any(
                "company/agents/product-engineering.yaml" in error
                and "high_impact_action" in error
                for error in errors
            ),
            f"expected a vocabulary error in {errors}",
        )


if __name__ == "__main__":
    unittest.main()
