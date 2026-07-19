"""Behavioral tests for scripts/session_start.py.

Every case builds its own throwaway repository tree, so these tests keep
passing after a founder configures the template (confirms documents and
advances the stage).
"""
from __future__ import annotations

from pathlib import Path
import importlib.util
import tempfile
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "session_start.py"
spec = importlib.util.spec_from_file_location("session_start", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)

LEGACY_COMMENT = "<!-- Statements personally confirmed by the founder. -->"


def make_repo(
    root: Path,
    statuses: dict[str, str] | str = "`draft`",
    stage_line: str | None = "stage: uninitialized",
    omit_docs: tuple[str, ...] = (),
) -> None:
    """Build a minimal fake template tree under root."""
    founder_dir = root / "company" / "founder"
    state_dir = root / "company" / "state"
    founder_dir.mkdir(parents=True, exist_ok=True)
    state_dir.mkdir(parents=True, exist_ok=True)
    if isinstance(statuses, str):
        statuses = {name: statuses for name in module.FOUNDER_DOC_NAMES}
    for name in module.FOUNDER_DOC_NAMES:
        if name in omit_docs:
            continue
        status = statuses.get(name, "`draft`")
        (founder_dir / name).write_text(
            f"# {name}\n\nStatus: {status}\nOwner: Founder\n\n"
            f"## Confirmed\n\n{LEGACY_COMMENT}\n",
            encoding="utf-8",
        )
    if stage_line is not None:
        (state_dir / "project-state.yaml").write_text(
            f"{stage_line}\nproject_name: null\n", encoding="utf-8"
        )


class SessionStartTests(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)

    def test_fresh_template_is_bootstrap(self) -> None:
        make_repo(self.root)
        result = module.build_result(self.root)
        self.assertEqual(result["mode"], "bootstrap_interview")
        self.assertEqual(len(result["missing_or_unconfirmed_founder_docs"]), 5)
        self.assertTrue(result["exit_steps"])

    def test_all_confirmed_and_stage_advanced_is_operating(self) -> None:
        make_repo(self.root, statuses="confirmed", stage_line="stage: discovery")
        result = module.build_result(self.root)
        self.assertEqual(result["mode"], "operating_loop")
        self.assertEqual(result["missing_or_unconfirmed_founder_docs"], [])
        self.assertEqual(result["exit_steps"], [])

    def test_same_keys_in_both_modes(self) -> None:
        make_repo(self.root)
        bootstrap = module.build_result(self.root)
        make_repo(self.root, statuses="confirmed", stage_line="stage: discovery")
        operating = module.build_result(self.root)
        self.assertEqual(set(bootstrap), set(operating))

    def test_backticked_confirmed_accepted_despite_legacy_comment(self) -> None:
        # The v0.1 gate rejected docs that still contained the legacy HTML
        # comment; the status line alone must decide now.
        make_repo(self.root, statuses="`confirmed`", stage_line="stage: discovery")
        result = module.build_result(self.root)
        self.assertEqual(result["mode"], "operating_loop")

    def test_status_value_case_insensitive(self) -> None:
        make_repo(self.root, statuses="Confirmed", stage_line="stage: discovery")
        result = module.build_result(self.root)
        self.assertEqual(result["mode"], "operating_loop")

    def test_stage_with_quotes_and_inline_comment(self) -> None:
        make_repo(
            self.root,
            statuses="confirmed",
            stage_line='stage: "discovery"  # advanced after bootstrap',
        )
        self.assertEqual(module.read_stage(self.root), "discovery")
        self.assertEqual(module.build_result(self.root)["mode"], "operating_loop")

    def test_missing_state_file_is_bootstrap(self) -> None:
        make_repo(self.root, statuses="confirmed", stage_line=None)
        result = module.build_result(self.root)
        self.assertEqual(result["stage"], "uninitialized")
        self.assertEqual(result["mode"], "bootstrap_interview")

    def test_missing_doc_listed_as_missing(self) -> None:
        make_repo(
            self.root,
            statuses="confirmed",
            stage_line="stage: discovery",
            omit_docs=("vision.md",),
        )
        result = module.build_result(self.root)
        self.assertEqual(result["mode"], "bootstrap_interview")
        self.assertIn(
            "company/founder/vision.md",
            result["missing_or_unconfirmed_founder_docs"],
        )
        self.assertEqual(result["founder_docs"]["company/founder/vision.md"], "missing")

    def test_unconfirmed_doc_forces_bootstrap_despite_stage(self) -> None:
        make_repo(
            self.root,
            statuses={
                name: ("draft" if name == "quality-bar.md" else "confirmed")
                for name in module.FOUNDER_DOC_NAMES
            },
            stage_line="stage: discovery",
        )
        result = module.build_result(self.root)
        self.assertEqual(result["mode"], "bootstrap_interview")
        self.assertEqual(
            result["missing_or_unconfirmed_founder_docs"],
            ["company/founder/quality-bar.md"],
        )

    def test_output_paths_use_forward_slashes(self) -> None:
        make_repo(self.root)
        result = module.build_result(self.root)
        for doc in result["founder_docs"]:
            self.assertIn("/", doc)
            self.assertNotIn("\\", doc)
        for doc in result["missing_or_unconfirmed_founder_docs"]:
            self.assertNotIn("\\", doc)


if __name__ == "__main__":
    unittest.main()
