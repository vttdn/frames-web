#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification script to ensure all locale files have question7 properly added.
"""

import json
import sys
from pathlib import Path


def verify_locale_file(file_path, lang_code):
    """Verify a locale JSON file has question7 in the correct place."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Check if qa section exists
        if 'qa' not in data:
            print(f"❌ {lang_code}: Missing 'qa' section")
            return False

        qa = data['qa']

        # Check if all questions 1-7 exist
        for i in range(1, 8):
            q_key = f"question{i}"
            if q_key not in qa:
                print(f"❌ {lang_code}: Missing {q_key}")
                return False

        # Verify question7 has both question and answer
        q7 = qa['question7']
        if 'question' not in q7 or 'answer' not in q7:
            print(f"❌ {lang_code}: question7 missing 'question' or 'answer' field")
            return False

        # Check that both are non-empty strings
        if not q7['question'] or not q7['answer']:
            print(f"❌ {lang_code}: question7 has empty 'question' or 'answer'")
            return False

        # Verify question7 mentions sync/iPhone/Mac
        question_text = q7['question'].lower()
        answer_text = q7['answer'].lower()

        has_sync_mention = any(word in question_text or word in answer_text
                               for word in ['sync', 'synk', 'συγχ', 'सिंक', 'đồng bộ', '同期', '동기화', '同步', 'senkron'])

        has_device_mention = ('iphone' in question_text or 'iphone' in answer_text or
                             'mac' in question_text or 'mac' in answer_text)

        if not (has_sync_mention or has_device_mention):
            print(f"⚠️  {lang_code}: question7 content may not be about sync (please verify manually)")

        print(f"✓ {lang_code}: Valid JSON, question7 exists with proper structure")
        return True

    except json.JSONDecodeError as e:
        print(f"❌ {lang_code}: Invalid JSON - {e}")
        return False
    except Exception as e:
        print(f"❌ {lang_code}: Error - {e}")
        return False


def main():
    """Main verification function."""
    locales_dir = Path(__file__).parent / "sources" / "locales"

    if not locales_dir.exists():
        print(f"❌ Locales directory not found: {locales_dir}")
        sys.exit(1)

    print("🔍 Verifying all locale files...\n")

    results = {"success": 0, "failed": 0}

    for json_file in sorted(locales_dir.glob("*.json")):
        if json_file.name == "global.json":
            continue

        lang_code = json_file.stem
        result = verify_locale_file(json_file, lang_code)

        if result:
            results["success"] += 1
        else:
            results["failed"] += 1

    print(f"\n📊 Verification Summary:")
    print(f"   ✓ Valid: {results['success']}")
    print(f"   ✗ Invalid: {results['failed']}")

    if results["failed"] == 0:
        print("\n✅ All locale files are valid!")
    else:
        print("\n⚠️  Some locale files have issues")

    sys.exit(0 if results["failed"] == 0 else 1)


if __name__ == "__main__":
    main()
