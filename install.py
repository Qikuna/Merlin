import os
import shutil
import sys

BIN_PATH = os.path.expanduser("~/.local/bin")
LAUNCHER_FILE = os.path.join(BIN_PATH, "merlin")
SOURCE_DIR = os.path.dirname(os.path.abspath(__file__))
ENTRY_POINT = os.path.join(SOURCE_DIR, "merlin.py")


def deploy():
    print("==> Running system checks...")
    if not os.path.exists(BIN_PATH):
        os.makedirs(BIN_PATH)
        print(f"--> Created missing binary path directory: {BIN_PATH}")

    wrapper_content = f'#!/usr/bin/env bash\npython3 "{ENTRY_POINT}" "$@"\n'

    try:
        with open(LAUNCHER_FILE, "w") as launcher:
            launcher.write(wrapper_content)

        os.chmod(LAUNCHER_FILE, 0o755)
        print(
            f"==> Success! Application launcher successfully linked to: {LAUNCHER_FILE}"
        )
        print(
            "\n[Installation finished] You can now open a new terminal session and type 'merlin'."
        )
    except Exception as e:
        print(
            f"!! [Installation failed] Error creating entry launcher: {e}",
            file=sys.stderr,
        )


if __name__ == "__main__":
    deploy()
