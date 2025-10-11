#!/usr/bin/env python3
"""
Add SEO metadata to changelog entries
Adds meta_title and meta_description fields to all changelog JSON files
"""

import json
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
CHANGELOG_DIR = PROJECT_ROOT / "build" / "locales" / "changelog"

# Languages to process
LANGUAGES = ['en', 'fr', 'de', 'es', 'it', 'nl', 'pl', 'pt', 'sv']

def add_seo_metadata(filepath):
    """Add SEO metadata to a single changelog entry file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Skip if already has meta fields
    if 'meta_title' in data and 'meta_description' in data:
        return False

    # Add meta_title (format: "Title · Frames")
    data['meta_title'] = f"{data['title']} · Frames"

    # Add meta_description (truncate summary if > 160 chars)
    summary = data['summary']
    if len(summary) > 160:
        # Try to truncate at last sentence before 160
        sentences = summary.split('. ')
        meta_desc = ""
        for sentence in sentences:
            if len(meta_desc) + len(sentence) + 2 <= 160:
                meta_desc += sentence + ". "
            else:
                break
        if not meta_desc:
            # If no complete sentence fits, truncate at word boundary
            words = summary.split()
            meta_desc = ""
            for word in words:
                if len(meta_desc) + len(word) + 4 <= 160:
                    meta_desc += word + " "
                else:
                    break
            meta_desc = meta_desc.strip() + "..."
        data['meta_description'] = meta_desc.strip()
    else:
        data['meta_description'] = summary

    # Write back with proper formatting
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return True

def main():
    """Process all changelog files"""
    total_updated = 0

    for lang in LANGUAGES:
        lang_dir = CHANGELOG_DIR / lang
        if not lang_dir.exists():
            print(f"⚠ Language directory not found: {lang}")
            continue

        updated_count = 0
        for json_file in sorted(lang_dir.glob("*.json")):
            if add_seo_metadata(json_file):
                updated_count += 1
                print(f"✓ Updated: {lang}/{json_file.name}")

        total_updated += updated_count
        print(f"✓ {lang}: Updated {updated_count} files")

    print(f"\n✓ Total: Updated {total_updated} files across {len(LANGUAGES)} languages")

if __name__ == "__main__":
    main()
