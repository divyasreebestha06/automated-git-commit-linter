import os
import stat

HOOK_SCRIPT = '''#!/bin/sh
python -m linter.cli "$1"
if [ $? -ne 0 ]; then
    echo "[COMMIT-LINTER] Commit rejected: message does not follow Conventional Commits standard."
    exit 1
fi
'''

def install_hook(git_dir: str = ".git"):
    hooks_dir = os.path.join(git_dir, "hooks")
    if not os.path.exists(hooks_dir):
        raise FileNotFoundError(f"Hooks directory {hooks_dir} does not exist.")
    target_path = os.path.join(hooks_dir, "commit-msg")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(HOOK_SCRIPT)
    os.chmod(target_path, os.stat(target_path).st_mode | stat.S_IEXEC)
    return target_path
