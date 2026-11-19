# 🛡️ automated-git-commit-linter

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](linter/)
[![Git Hooks](https://img.shields.io/badge/Git-Hooks-F05032?style=for-the-badge&logo=git)](linter/)
[![CI](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)](ci/)

Conventional Commits Specification Validator and Git Commit Hook Enforcer with custom rule definitions.

## Features
- **Conventional Commits 1.0.0:** Enforces type specifications (`feat`, `fix`, `docs`, `chore`, etc.).
- **Header Formatting:** Restricts header length to 72 characters, lowercase start, and no trailing period.
- **Git Hook Automation:** Installs `commit-msg` hooks directly into any local git repository.

## Usage
```bash
python -m linter.cli "feat(auth): implement jwt refresh token"
```
