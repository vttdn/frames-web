#!/usr/bin/env python3
"""
Script to fix Subject Distance and Subject Distance Range translations
in 1.21.0-ios.json and 1.13.0-macos.json files.
Uses Canon/Nikon terminology for each language.
"""

import json
from pathlib import Path

# Base path for changelog locales
BASE_PATH = Path(__file__).parent.parent / "sources" / "locales" / "changelog"

# Translations for Subject Distance and Subject Distance Range
# Based on Canon/Nikon camera terminology
SUBJECT_DISTANCE_TRANSLATIONS = {
    "da": {
        "subject_distance": "Motivafstand",
        "subject_distance_range": "Motivafstandsområde"
    },
    "de": {
        "subject_distance": "Motiventfernung",
        "subject_distance_range": "Motiventfernungsbereich"
    },
    "el": {
        "subject_distance": "Απόσταση θέματος",
        "subject_distance_range": "Εύρος απόστασης θέματος"
    },
    "es": {
        "subject_distance": "Distancia al sujeto",
        "subject_distance_range": "Rango de distancia al sujeto"
    },
    "fi": {
        "subject_distance": "Kohteen etäisyys",
        "subject_distance_range": "Kohteen etäisyysalue"
    },
    "fr": {
        "subject_distance": "Distance du sujet",
        "subject_distance_range": "Plage de distance du sujet"
    },
    "hi": {
        "subject_distance": "विषय दूरी",
        "subject_distance_range": "विषय दूरी सीमा"
    },
    "id": {
        "subject_distance": "Jarak subjek",
        "subject_distance_range": "Rentang jarak subjek"
    },
    "it": {
        "subject_distance": "Distanza dal soggetto",
        "subject_distance_range": "Intervallo distanza soggetto"
    },
    "ja": {
        "subject_distance": "被写体距離",
        "subject_distance_range": "被写体距離範囲"
    },
    "ko": {
        "subject_distance": "피사체 거리",
        "subject_distance_range": "피사체 거리 범위"
    },
    "nb": {
        "subject_distance": "Motivavstand",
        "subject_distance_range": "Motivavstandsområde"
    },
    "nl": {
        "subject_distance": "Afstand tot onderwerp",
        "subject_distance_range": "Bereik afstand tot onderwerp"
    },
    "pl": {
        "subject_distance": "Odległość od obiektu",
        "subject_distance_range": "Zakres odległości od obiektu"
    },
    "pt": {
        "subject_distance": "Distância do assunto",
        "subject_distance_range": "Intervalo de distância do assunto"
    },
    "ro": {
        "subject_distance": "Distanța subiectului",
        "subject_distance_range": "Intervalul distanței subiectului"
    },
    "ru": {
        "subject_distance": "Расстояние до объекта",
        "subject_distance_range": "Диапазон расстояния до объекта"
    },
    "sv": {
        "subject_distance": "Motivavstånd",
        "subject_distance_range": "Motivavståndsintervall"
    },
    "th": {
        "subject_distance": "ระยะห่างวัตถุ",
        "subject_distance_range": "ช่วงระยะห่างวัตถุ"
    },
    "tr": {
        "subject_distance": "Konu mesafesi",
        "subject_distance_range": "Konu mesafe aralığı"
    },
    "uk": {
        "subject_distance": "Відстань до об'єкта",
        "subject_distance_range": "Діапазон відстані до об'єкта"
    },
    "vi": {
        "subject_distance": "Khoảng cách chủ thể",
        "subject_distance_range": "Phạm vi khoảng cách chủ thể"
    },
    "zh": {
        "subject_distance": "主体距离",
        "subject_distance_range": "主体距离范围"
    },
    "zh-hant": {
        "subject_distance": "主體距離",
        "subject_distance_range": "主體距離範圍"
    }
}


def replace_in_string(text: str, lang_code: str) -> str:
    """Replace Subject Distance terms in a string."""
    if lang_code not in SUBJECT_DISTANCE_TRANSLATIONS:
        return text

    trans = SUBJECT_DISTANCE_TRANSLATIONS[lang_code]

    # Replace Subject Distance Range first (longer string) to avoid partial replacements
    text = text.replace("Subject Distance Range", trans["subject_distance_range"])
    text = text.replace("Subject Distance", trans["subject_distance"])

    return text


def update_json_values(obj, lang_code: str):
    """Recursively update all string values in a JSON object."""
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, str):
                obj[key] = replace_in_string(value, lang_code)
            elif isinstance(value, (dict, list)):
                update_json_values(value, lang_code)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            if isinstance(item, str):
                obj[i] = replace_in_string(item, lang_code)
            elif isinstance(item, (dict, list)):
                update_json_values(item, lang_code)


def update_file(file_path: Path, lang_code: str) -> bool:
    """Update a single file with translated Subject Distance terms."""
    if not file_path.exists():
        return False

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        update_json_values(data, lang_code)

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    """Main function to update all language files."""

    print("Updating Subject Distance translations...\n")

    # Files to update
    files_to_update = ["1.21.0-ios.json", "1.13.0-macos.json"]

    # Languages to process (excluding English)
    languages = [
        "da", "de", "el", "es", "fi", "fr", "hi", "id", "it", "ja", "ko",
        "nb", "nl", "pl", "pt", "ro", "ru", "sv", "th", "tr", "uk", "vi",
        "zh", "zh-hant"
    ]

    updated = 0
    skipped = 0

    for lang_code in languages:
        print(f"  {lang_code}: ", end="")
        lang_updated = False

        for filename in files_to_update:
            file_path = BASE_PATH / lang_code / filename
            if update_file(file_path, lang_code):
                lang_updated = True

        if lang_updated:
            print("Updated")
            updated += 1
        else:
            print("Skipped")
            skipped += 1

    print(f"\nDone! Updated: {updated}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
