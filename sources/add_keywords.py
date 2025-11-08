#!/usr/bin/env python3
"""
Script to add meta keywords to all locale JSON files
"""
import json
import os

# Read keywords from file
keywords_data = {}
with open('keywords_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        lang, keywords = line.split(':', 1)
        keywords_data[lang.strip()] = keywords.strip()

# Update each locale JSON file
locales_dir = 'locales'
for lang_code, keywords_str in keywords_data.items():
    json_file = os.path.join(locales_dir, f'{lang_code}.json')

    if not os.path.exists(json_file):
        print(f"Warning: {json_file} not found, skipping...")
        continue

    # Read existing JSON
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Add keywords to meta section
    if 'meta' in data:
        data['meta']['keywords'] = keywords_str
        print(f"✓ Added keywords to {lang_code}.json")
    else:
        print(f"Warning: No 'meta' section found in {json_file}")
        continue

    # Write back with proper formatting (2-space indent)
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')  # Add trailing newline

print("\nDone! Updated all locale files with keywords.")
