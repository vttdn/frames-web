#!/usr/bin/env python3
"""
Script to populate howto meta translations from howto_meta_translations.txt to all locale JSON files
"""

import json
import re
from pathlib import Path

def parse_translations_file(filepath):
    """Parse the howto_meta_translations.txt file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    translations = {}

    # Split by language sections (looking for patterns like "DANISH (da)" or "NORWEGIAN BOKMÅL (nb)")
    lang_sections = re.split(r'\n(?=[A-Z][A-ZÅ\s]+\([a-z\-]+\))', content)

    for section in lang_sections:
        if not section.strip():
            continue

        # Extract language name and code
        lang_match = re.match(r'([A-Z][A-ZÅ\s]+)\(([a-z\-]+)\)', section)
        if not lang_match:
            continue

        lang_code = lang_match.group(2).strip()

        # Extract meta.title
        title_match = re.search(r'meta\.title:\s*(.+?)$', section, re.MULTILINE)
        if not title_match:
            continue

        title = title_match.group(1).strip()

        # Extract meta.description
        desc_match = re.search(r'meta\.description:\s*(.+?)(?=\n[A-Z]|\Z)', section, re.MULTILINE | re.DOTALL)
        if not desc_match:
            continue

        description = desc_match.group(1).strip()

        translations[lang_code] = {
            'title': title,
            'description': description
        }

    return translations

def update_locale_file(lang_code, meta_data):
    """Update a locale JSON file with howto meta data"""
    locale_path = Path(__file__).parent.parent / 'locales' / f'{lang_code}.json'

    # Read existing JSON
    with open(locale_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Add/update howto.meta section
    if 'howto' not in data:
        print(f"⚠ Warning: {lang_code}.json does not have a 'howto' section")
        return

    data['howto']['meta'] = meta_data

    # Write back with proper formatting
    with open(locale_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    print(f"✓ Updated {lang_code}.json")

def main():
    # Get the translations file path
    translations_file = Path(__file__).parent.parent / 'locales' / 'howto_meta_translations.txt'

    print("Parsing meta translations file...")
    translations = parse_translations_file(translations_file)

    print(f"\nFound translations for {len(translations)} languages")
    print("\nUpdating locale files...")

    for lang_code, meta_data in translations.items():
        update_locale_file(lang_code, meta_data)

    print(f"\n✓ Successfully updated {len(translations)} locale files")

if __name__ == '__main__':
    main()
