import re
from typing import Dict, Any, List

ALLOWED_TYPES = {"feat", "fix", "docs", "style", "refactor", "perf", "test", "build", "ci", "chore", "revert"}

class CommitLinter:
    def __init__(self, max_header_length: int = 72):
        self.max_header_length = max_header_length
        # Conventional Commit regex: type(scope)?: description
        self.pattern = re.compile(r"^([a-z]+)(\([a-zA-Z0-9_\-]+\))?!?: (.+)$")

    def lint(self, message: str) -> Dict[str, Any]:
        lines = message.strip().splitlines()
        if not lines:
            return {"valid": False, "errors": ["Commit message cannot be empty"]}

        header = lines[0].strip()
        errors = []

        if len(header) > self.max_header_length:
            errors.append(f"Header exceeds {self.max_header_length} characters (length: {len(header)})")

        match = self.pattern.match(header)
        if not match:
            errors.append("Header must follow format '<type>(<scope>): <subject>' (e.g. 'feat(auth): add login endpoint')")
        else:
            commit_type = match.group(1)
            scope = match.group(2)
            subject = match.group(3)

            if commit_type not in ALLOWED_TYPES:
                errors.append(f"Invalid commit type '{commit_type}'. Allowed types: {', '.join(sorted(ALLOWED_TYPES))}")

            if subject.endswith("."):
                errors.append("Subject should not end with a period")

            if subject[0].isupper():
                errors.append("Subject should start with a lowercase letter")

        return {
            "valid": len(errors) == 0,
            "header": header,
            "errors": errors
        }
