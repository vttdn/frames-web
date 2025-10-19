#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final verification script to check question7 answers don't contain iCloud reference.
"""

import json
import sys
from pathlib import Path


def verify_no_icloud_sentence(file_path, lang_code):
    """Verify that question7 doesn't contain iCloud sentence."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if 'qa' not in data or 'question7' not in data['qa']:
            print(f"❌ {lang_code}: Missing question7")
            return False

        answer = data['qa']['question7']['answer']

        # Check if any iCloud reference exists
        if 'icloud' in answer.lower():
            print(f"❌ {lang_code}: Still contains iCloud reference")
            print(f"    Answer: {answer[:100]}...")
            return False

        # Check that answer is non-empty
        if not answer.strip():
            print(f"❌ {lang_code}: Empty answer")
            return False

        # Check that answer ends properly (not with extra spaces)
        if answer != answer.rstrip():
            print(f"⚠️  {lang_code}: Answer has trailing whitespace")

        print(f"✓ {lang_code}: No iCloud reference, answer looks good")
        return True

    except Exception as e:
        print(f"❌ {lang_code}: Error - {e}")
        return False


def main():
    """Main verification function."""
    locales_dir = Path(__file__).parent / "sources" / "locales"

    if not locales_dir.exists():
        print(f"❌ Locales directory not found: {locales_dir}")
        sys.exit(1)

    print("🔍 Final verification: Checking all question7 answers...\n")

    results = {"success": 0, "failed": 0}

    for json_file in sorted(locales_dir.glob("*.json")):
        if json_file.name == "global.json":
            continue

        lang_code = json_file.stem
        result = verify_no_icloud_sentence(json_file, lang_code)

        if result:
            results["success"] += 1
        else:
            results["failed"] += 1

    print(f"\n📊 Final Verification Summary:")
    print(f"   ✓ Valid: {results['success']}")
    print(f"   ✗ Invalid: {results['failed']}")

    if results["failed"] == 0:
        print("\n✅ All files verified! No iCloud references found.")
    else:
        print("\n⚠️  Some files still have issues")

    sys.exit(0 if results["failed"] == 0 else 1)


if __name__ == "__main__":
    main()
