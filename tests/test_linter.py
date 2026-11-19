import unittest
from linter.engine import CommitLinter

class TestCommitLinter(unittest.TestCase):
    def setUp(self):
        self.linter = CommitLinter(max_header_length=72)

    def test_valid_conventional_commits(self):
        valid_samples = [
            "feat: add OAuth2 login support",
            "fix(api): handle null pointer in user registration",
            "docs: update installation instructions in README",
            "chore(deps): bump pydantic from 2.4.0 to 2.5.0",
            "perf: optimize database connection pooling"
        ]
        for msg in valid_samples:
            res = self.linter.lint(msg)
            self.assertTrue(res["valid"], f"Expected valid for: {msg}")

    def test_invalid_types(self):
        res = self.linter.lint("awesome: new landing page")
        self.assertFalse(res["valid"])
        self.assertTrue(any("Invalid commit type" in err for err in res["errors"]))

    def test_subject_rules(self):
        res_dot = self.linter.lint("feat: add search endpoint.")
        self.assertFalse(res_dot["valid"])
        self.assertTrue(any("period" in err for err in res_dot["errors"]))

        res_upper = self.linter.lint("feat: Add search endpoint")
        self.assertFalse(res_upper["valid"])
        self.assertTrue(any("lowercase" in err for err in res_upper["errors"]))

    def test_header_length_limit(self):
        long_msg = "feat: " + ("a" * 80)
        res = self.linter.lint(long_msg)
        self.assertFalse(res["valid"])
        self.assertTrue(any("Header exceeds" in err for err in res["errors"]))

if __name__ == "__main__":
    unittest.main()
