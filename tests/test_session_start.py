from pathlib import Path
import importlib.util
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "session_start.py"
spec = importlib.util.spec_from_file_location("session_start", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class SessionStartTests(unittest.TestCase):
    def test_initial_template_requests_bootstrap(self):
        result = module.build_result()
        self.assertEqual(result["mode"], "bootstrap_interview")
        self.assertTrue(result["missing_or_unconfirmed_founder_docs"])


if __name__ == "__main__":
    unittest.main()
