#!/usr/bin/env python3
"""
Script to populate howto translations from howto_translations.txt to all locale JSON files
"""

import json
import re
from pathlib import Path

# Language code mapping
LANG_MAP = {
    'Danish': 'da',
    'Dutch': 'nl',
    'Finnish': 'fi',
    'French': 'fr',
    'German': 'de',
    'Greek': 'el',
    'Hindi': 'hi',
    'Indonesian': 'id',
    'Italian': 'it',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Norwegian Bokmål': 'nb',
    'Polish': 'pl',
    'Portuguese': 'pt',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Simplified Chinese': 'zh',
    'Spanish': 'es',
    'Swedish': 'sv',
    'Thai': 'th',
    'Traditional Chinese': 'zh-hant',
    'Turkish': 'tr',
    'Ukrainian': 'uk',
    'Vietnamese': 'vi'
}

def parse_translations_file(filepath):
    """Parse the howto_translations.txt file"""
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

        lang_name = lang_match.group(1).strip()
        lang_code = lang_match.group(2).strip()

        # Extract heading
        heading_match = re.search(r'heading:\s*(.+?)$', section, re.MULTILINE)
        if not heading_match:
            continue

        heading = heading_match.group(1).strip()

        # Extract howto entries
        howto_data = {'heading': heading}

        for i in range(1, 7):
            # Extract heading for this howto
            heading_pattern = rf'howto{i}\.heading:\s*(.+?)$'
            heading_match = re.search(heading_pattern, section, re.MULTILINE)

            # Extract description for this howto
            desc_pattern = rf'howto{i}\.description:\s*(.+?)(?=\nhowto|\n[A-Z]|\Z)'
            desc_match = re.search(desc_pattern, section, re.MULTILINE | re.DOTALL)

            if heading_match and desc_match:
                howto_heading = heading_match.group(1).strip()
                howto_desc = desc_match.group(1).strip()

                howto_data[f'howto{i}'] = {
                    'heading': howto_heading,
                    'description': howto_desc
                }

        # Only add if we have all 6 howto entries
        if len(howto_data) == 7:  # heading + 6 howto entries
            translations[lang_code] = howto_data

    return translations

def update_locale_file(lang_code, howto_data):
    """Update a locale JSON file with howto data"""
    locale_path = Path(__file__).parent.parent / 'locales' / f'{lang_code}.json'

    # Read existing JSON
    with open(locale_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Add/update howto section
    data['howto'] = howto_data

    # Write back with proper formatting
    with open(locale_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    print(f"✓ Updated {lang_code}.json")

def main():
    # Get the translations file path
    translations_file = Path(__file__).parent.parent / 'locales' / 'howto_translations.txt'

    print("Parsing translations file...")
    translations = parse_translations_file(translations_file)

    print(f"\nFound translations for {len(translations)} languages")
    print("\nUpdating locale files...")

    for lang_code, howto_data in translations.items():
        update_locale_file(lang_code, howto_data)

    print(f"\n✓ Successfully updated {len(translations)} locale files")

if __name__ == '__main__':
    main()
