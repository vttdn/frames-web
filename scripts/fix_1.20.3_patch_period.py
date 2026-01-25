#!/usr/bin/env python3
"""
Script to remove the trailing period from patch 1.20.3 description
in all 1.20.0-ios.json changelog files.
"""

import json
from pathlib import Path

# Base path for changelog locales
BASE_PATH = Path(__file__).parent.parent / "sources" / "locales" / "changelog"


def fix_patch_description(file_path: Path) -> bool:
    """Remove trailing period from patch 1.20.3 description."""

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"  Error reading file: {e}")
        return False

    modified = False
    for patch in data.get("patches", []):
        if patch.get("version") == "1.20.3":
            desc = patch.get("description", "")
            if desc.endswith("."):
                patch["description"] = desc.rstrip(".")
                modified = True

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')

    return modified


def main():
    """Main function to fix all language files."""

    print("Removing trailing period from patch 1.20.3 description...\n")

    fixed = 0
    skipped = 0

    for lang_dir in sorted(BASE_PATH.iterdir()):
        if not lang_dir.is_dir():
            continue

        lang_code = lang_dir.name
        file_path = lang_dir / "1.20.0-ios.json"

        if not file_path.exists():
            continue

        print(f"  {lang_code}: ", end="")

        if fix_patch_description(file_path):
            print("Fixed")
            fixed += 1
        else:
            print("No change needed")
            skipped += 1

    print(f"\nDone! Fixed: {fixed}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
