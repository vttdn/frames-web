#!/usr/bin/env python3
import json
import glob
import os

# Find all 1.10.0-macos.json files
pattern = "sources/locales/changelog/*/1.10.0-macos.json"
files = glob.glob(pattern)

print(f"Found {len(files)} files to update")

for file_path in files:
    print(f"Updating {file_path}...")

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Update the date
    data['release_date'] = '2025-10-31T10:00:00.000Z'

    # Write back with proper formatting
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')  # Add newline at end

    print(f"✓ Updated {file_path}")

print(f"\n✓ Successfully updated {len(files)} files!")
