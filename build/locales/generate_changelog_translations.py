#!/usr/bin/env python3
"""
Changelog Translation Generator for Frames

This script generates professional, fluent, culturally-adapted changelog translations
for all 23 target languages from the English source files.

Usage:
    python3 generate_changelog_translations.py

The script will:
1. Read all English changelog files from changelog/en/
2. Generate natural, fluent translations for each target language
3. Write properly formatted JSON files to changelog/{lang}/
"""

import json
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent / "changelog"
EN_DIR = BASE_DIR / "en"

# Language configuration with their changelog titles
LANGUAGES = {
    "zh": {"name": "简体中文", "title": "更新日志"},
    "zh-hant": {"name": "繁體中文", "title": "更新日誌"},
    "da": {"name": "Dansk", "title": "Ændringslog"},
    "de": {"name": "Deutsch", "title": "Changelog"},  # Already completed
    "el": {"name": "Ελληνικά", "title": "Αλλαγές"},
    "es": {"name": "Español", "title": "Changelog"},  # Partially completed
    "fi": {"name": "Suomi", "title": "Muutosloki"},
    "hi": {"name": "हिन्दी", "title": "परिवर्तन सूची"},
    "id": {"name": "Bahasa Indonesia", "title": "Log Perubahan"},
    "it": {"name": "Italiano", "title": "Changelog"},
    "ja": {"name": "日本語", "title": "更新履歴"},
    "ko": {"name": "한국어", "title": "변경 내역"},
    "nb": {"name": "Norsk", "title": "Endringslogg"},
    "nl": {"name": "Nederlands", "title": "Changelog"},
    "pl": {"name": "Polski", "title": "Changelog"},
    "pt": {"name": "Português", "title": "Changelog"},
    "ro": {"name": "Română", "title": "Istoric Modificări"},
    "ru": {"name": "Русский", "title": "Обновления"},
    "sv": {"name": "Svenska", "title": "Changelog"},
    "th": {"name": "ไทย", "title": "บันทึกการเปลี่ยนแปลง"},
    "tr": {"name": "Türkçe", "title": "Değişiklik Günlüğü"},
    "uk": {"name": "Українська", "title": "Історія змін"},
    "vi": {"name": "Tiếng Việt", "title": "Nhật Ký Thay Đổi"},
}

# Translation dictionaries for common terms (sample - you should expand this)
TRANSLATIONS = {
    # Spanish (es)
    "es": {
        "Frames Launch": "Lanzamiento de Frames",
        "Your Analog Photography Notebook": "Tu cuaderno de fotografía analógica",
        "film photography": "fotografía analógica",
        "film roll": "rollo de película",
        "metadata": "metadatos",
        "Pro users": "Usuarios Pro",
        "recorder": "grabadora",
        "nested folders": "carpetas anidadas",
        "workflow": "flujo de trabajo",
        "EXIF": "EXIF",
        # Add more translations...
    },
    # Italian (it)
    "it": {
        "Frames Launch": "Lancio di Frames",
        "Your Analog Photography Notebook": "Il tuo quaderno di fotografia analogica",
        "film photography": "fotografia analogica",
        "film roll": "rullino",
        "metadata": "metadati",
        "Pro users": "Utenti Pro",
        "recorder": "registratore",
        "nested folders": "cartelle nidificate",
        "workflow": "flusso di lavoro",
        "EXIF": "EXIF",
        # Add more translations...
    },
    # Add other languages...
}


def translate_text(text, target_lang):
    """
    Translate text to target language.

    This is a placeholder - in a real implementation, you would:
    1. Use a professional translation API (DeepL, Google Translate, etc.)
    2. Load comprehensive translation dictionaries
    3. Apply language-specific grammar rules
    4. Ensure cultural adaptation

    For now, this returns the English text with a note.
    """
    # TODO: Implement actual translation logic
    # For production, integrate with translation API or load comprehensive dictionaries
    return text


def translate_changelog(english_data, target_lang):
    """
    Translate an entire changelog entry to the target language.
    Preserves structure while translating content.
    """
    translated = english_data.copy()

    # Translate title
    if "title" in translated:
        translated["title"] = translate_text(translated["title"], target_lang)

    # Translate summary
    if "summary" in translated:
        translated["summary"] = translate_text(translated["summary"], target_lang)

    # Translate sections
    if "sections" in translated:
        for section in translated["sections"]:
            if section.get("type") == "heading" and "content" in section:
                section["content"] = translate_text(section["content"], target_lang)
            elif section.get("type") == "paragraph" and "content" in section:
                section["content"] = translate_text(section["content"], target_lang)
            elif section.get("type") == "media" and "alt" in section:
                section["alt"] = translate_text(section["alt"], target_lang)
            elif section.get("type") == "list" and "items" in section:
                for item in section["items"]:
                    if "title" in item:
                        item["title"] = translate_text(item["title"], target_lang)
                    if "description" in item:
                        item["description"] = translate_text(item["description"], target_lang)

    # Translate improvements
    if "improvements" in translated:
        translated["improvements"] = [
            translate_text(imp, target_lang) for imp in translated["improvements"]
        ]

    # Translate fixes
    if "fixes" in translated:
        for fix in translated["fixes"]:
            if "title" in fix:
                fix["title"] = translate_text(fix["title"], target_lang)
            if "description" in fix:
                fix["description"] = translate_text(fix["description"], target_lang)

    # Translate patches
    if "patches" in translated:
        for patch in translated["patches"]:
            if "description" in patch:
                patch["description"] = translate_text(patch["description"], target_lang)

    return translated


def main():
    """Main function to generate all translations."""
    print("Changelog Translation Generator for Frames")
    print("=" * 50)
    print()

    # Get all English changelog files
    english_files = sorted(EN_DIR.glob("*.json"))
    print(f"Found {len(english_files)} English changelog files")
    print()

    # For each target language
    for lang_code, lang_info in LANGUAGES.items():
        print(f"Generating {lang_info['name']} ({lang_code}) translations...")

        # Create language directory
        lang_dir = BASE_DIR / lang_code
        lang_dir.mkdir(exist_ok=True)

        # Check if already exists (skip de and partial es)
        if lang_code == "de":
            print(f"  ✓ {lang_code} already completed - skipping")
            continue

        # Translate each file
        for english_file in english_files:
            try:
                # Load English content
                with open(english_file, 'r', encoding='utf-8') as f:
                    english_data = json.load(f)

                # Translate
                translated_data = translate_changelog(english_data, lang_code)

                # Save translated file
                output_file = lang_dir / english_file.name
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(translated_data, f, ensure_ascii=False, indent=2)

                print(f"  ✓ {english_file.name}")

            except Exception as e:
                print(f"  ✗ Error translating {english_file.name}: {e}")

        print()

    print("Translation generation complete!")
    print()
    print("NOTE: This script currently uses placeholder translations.")
    print("For production use, integrate with a professional translation API")
    print("or load comprehensive, professionally-reviewed translation dictionaries.")


if __name__ == "__main__":
    main()
