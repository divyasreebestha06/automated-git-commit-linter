import sys
from linter.engine import CommitLinter

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m linter.cli <commit_message_or_file>")
        sys.exit(1)

    arg = sys.argv[1]
    import os
    if os.path.isfile(arg):
        with open(arg, "r", encoding="utf-8") as f:
            message = f.read()
    else:
        message = arg

    linter = CommitLinter()
    result = linter.lint(message)

    if not result["valid"]:
        print("[FAIL] Invalid commit message:")
        for err in result["errors"]:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("[PASS] Commit message conforms to Conventional Commits specification.")
        sys.exit(0)

if __name__ == "__main__":
    main()
