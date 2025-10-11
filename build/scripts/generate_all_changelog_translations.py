#!/usr/bin/env python3
"""
Automated Changelog Translation Generator
Generates changelog translations for all configured languages
"""

import json
import os
import sys
from pathlib import Path
import subprocess

# Get project root
PROJECT_ROOT = Path(__file__).parent.parent.parent
CHANGELOG_DIR = PROJECT_ROOT / "build" / "locales" / "changelog"
LOCALES_DIR = PROJECT_ROOT / "build" / "locales"
IMG_DIR = PROJECT_ROOT / "lib" / "img"

# Languages already complete
COMPLETED_LANGUAGES = ['en', 'fr', 'de', 'es', 'it']

# All languages that need changelogs
ALL_LANGUAGES = [
    'en', 'zh', 'zh-hant', 'da', 'de', 'el', 'es', 'fi', 'fr', 'hi', 'id',
    'it', 'ja', 'ko', 'nb', 'nl', 'pl', 'pt', 'ro', 'ru', 'sv', 'th', 'tr',
    'uk', 'vi'
]

def translate_with_deepl(text, target_lang, source_lang='en'):
    """
    Placeholder for DeepL API translation
    Replace with actual API call if you have DeepL API key
    """
    # This is where you'd integrate DeepL API
    # For now, return text as-is (manual translation needed)
    return f"[TRANSLATE TO {target_lang}]: {text}"

def create_locale_changelog_section(lang_code, changelog_title):
    """Create changelog section for locale file"""

    # Base translations for common labels
    label_translations = {
        'en': {
            'improvements': 'Improvements',
            'fixes': 'Fixes',
            'patches': 'Patches',
            'previous': 'Previous',
            'next': 'Next',
            'page': 'Page',
            'newer_posts': 'Newer posts',
            'older_posts': 'Older posts'
        },
        # Add more language-specific translations as needed
    }

    return {
        "meta": {
            "title": f"{changelog_title} - Frames",
            "description": f"Frames {changelog_title}.",
            "canonical_url": f"https://withframes.com/{lang_code}/changelog/" if lang_code != 'en' else "https://withframes.com/changelog/"
        },
        "heading": changelog_title,
        "labels": {
            "improvements": label_translations.get(lang_code, label_translations['en'])['improvements'],
            "fixes": label_translations.get(lang_code, label_translations['en'])['fixes'],
            "patches": label_translations.get(lang_code, label_translations['en'])['patches'],
            "platform_ios": "iOS",
            "platform_macos": "macOS",
            "previous": label_translations.get(lang_code, label_translations['en'])['previous'],
            "next": label_translations.get(lang_code, label_translations['en'])['next']
        },
        "pagination": {
            "previous": label_translations.get(lang_code, label_translations['en'])['previous'],
            "next": label_translations.get(lang_code, label_translations['en'])['next'],
            "page": label_translations.get(lang_code, label_translations['en'])['page'],
            "newer_posts": label_translations.get(lang_code, label_translations['en'])['newer_posts'],
            "older_posts": label_translations.get(lang_code, label_translations['en'])['older_posts']
        }
    }

def copy_images_for_language(lang_code):
    """Copy English changelog images to target language folder"""
    en_img_dir = IMG_DIR / "en" / "changelog"
    target_img_dir = IMG_DIR / lang_code / "changelog"

    if not en_img_dir.exists():
        print(f"  ⚠ Warning: English changelog images not found at {en_img_dir}")
        return False

    target_img_dir.mkdir(parents=True, exist_ok=True)

    # Copy all files
    import shutil
    for img_file in en_img_dir.glob("*"):
        if img_file.is_file():
            shutil.copy2(img_file, target_img_dir / img_file.name)

    print(f"  ✓ Copied images to {lang_code}/changelog/")
    return True

def main():
    print("=" * 70)
    print("AUTOMATED CHANGELOG TRANSLATION GENERATOR")
    print("=" * 70)
    print("\nThis script helps set up changelog directories and image folders")
    print("for all configured languages. Manual translation still required.\n")

    # Load global config to get changelog titles
    global_config_path = LOCALES_DIR / "global.json"
    try:
        with open(global_config_path, 'r', encoding='utf-8') as f:
            global_config = json.load(f)
    except FileNotFoundError:
        print(f"✗ Error: global.json not found at {global_config_path}")
        sys.exit(1)

    # Create a mapping of language codes to changelog titles
    lang_to_title = {}
    for lang_file in LOCALES_DIR.glob("*.json"):
        if lang_file.stem in ['global']:
            continue
        try:
            with open(lang_file, 'r', encoding='utf-8') as f:
                locale_data = json.load(f)
                if 'header' in locale_data and 'navigation' in locale_data['header']:
                    changelog_title = locale_data['header']['navigation'].get('changelog', 'Changelog')
                    lang_to_title[lang_file.stem] = changelog_title
        except:
            continue

    print(f"Found {len(lang_to_title)} language configurations\n")

    # Process each language
    remaining_langs = [lang for lang in ALL_LANGUAGES if lang not in COMPLETED_LANGUAGES]

    print(f"Already completed: {', '.join(COMPLETED_LANGUAGES)}")
    print(f"To process: {len(remaining_langs)} languages\n")

    for lang_code in remaining_langs:
        print(f"Processing {lang_code}...")

        # Create changelog directory
        lang_changelog_dir = CHANGELOG_DIR / lang_code
        lang_changelog_dir.mkdir(parents=True, exist_ok=True)
        print(f"  ✓ Created directory: {lang_changelog_dir}")

        # Copy images
        copy_images_for_language(lang_code)

        # Update locale file with changelog section if needed
        locale_file = LOCALES_DIR / f"{lang_code}.json"
        if locale_file.exists():
            try:
                with open(locale_file, 'r', encoding='utf-8') as f:
                    locale_data = json.load(f)

                if 'changelog' not in locale_data or locale_data.get('changelog') is None:
                    changelog_title = lang_to_title.get(lang_code, 'Changelog')
                    locale_data['changelog'] = create_locale_changelog_section(lang_code, changelog_title)

                    with open(locale_file, 'w', encoding='utf-8') as f:
                        json.dump(locale_data, f, ensure_ascii=False, indent=2)

                    print(f"  ✓ Added changelog section to {lang_code}.json")
                else:
                    print(f"  ℹ Changelog section already exists in {lang_code}.json")
            except Exception as e:
                print(f"  ✗ Error updating locale file: {e}")

        print()

    print("=" * 70)
    print("SETUP COMPLETE")
    print("=" * 70)
    print("\nNext steps:")
    print("1. Directories and images are ready for all languages")
    print("2. Locale files have been updated with changelog sections")
    print("3. Use professional translation service (DeepL, etc.) to translate")
    print("   the 23 English changelog files for each remaining language")
    print("4. Place translated files in respective /build/locales/changelog/{lang}/ directories")
    print("\nAlternatively, update this script with DeepL API integration")
    print("for automated translation.")

if __name__ == "__main__":
    main()
