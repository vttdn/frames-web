#!/usr/bin/env python3
"""
Script to update 1.12.0-macos.json changelog files:
1. Add the missing heading block for "Exposure Mode and Exposure Program"
2. Reorder sections: media first, then heading, then paragraphs
"""

import json
from pathlib import Path

# Translations for "Exposure Mode and Exposure Program"
HEADING_TRANSLATIONS = {
    "da": "Eksponeringstilstand og eksponeringsprogram",
    "de": "Belichtungsmodus und Belichtungsprogramm",
    "el": "Λειτουργία έκθεσης και πρόγραμμα έκθεσης",
    "es": "Modo de exposición y programa de exposición",
    "fi": "Valotustila ja valotusohjelma",
    "fr": "Mode d'exposition et programme d'exposition",
    "hi": "एक्सपोज़र मोड और एक्सपोज़र प्रोग्राम",
    "id": "Mode Eksposur dan Program Eksposur",
    "it": "Modalità di esposizione e programma di esposizione",
    "ja": "撮影モードと露出プログラム",
    "ko": "노출 모드와 노출 프로그램",
    "nb": "Eksponeringsmodus og eksponeringsprogram",
    "nl": "Belichtingsmodus en belichtingsprogramma",
    "pl": "Tryb ekspozycji i program ekspozycji",
    "pt": "Modo de exposição e programa de exposição",
    "ro": "Modul de expunere și programul de expunere",
    "ru": "Режим экспозиции и программа экспозиции",
    "sv": "Exponeringsläge och exponeringsprogram",
    "th": "โหมดการเปิดรับแสงและโปรแกรมการเปิดรับแสง",
    "tr": "Pozlama Modu ve Pozlama Programı",
    "uk": "Режим експозиції та програма експозиції",
    "vi": "Chế độ phơi sáng và chương trình phơi sáng",
    "zh-hant": "曝光模式和曝光程式",
    "zh": "曝光模式和曝光程序",
}

def update_changelog_file(filepath: Path, lang: str) -> bool:
    """Update a single changelog file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        sections = data.get('sections', [])

        # Find existing blocks
        media_block = None
        paragraphs = []

        for section in sections:
            if section.get('type') == 'media':
                media_block = section
            elif section.get('type') == 'paragraph':
                paragraphs.append(section)

        if not media_block or len(paragraphs) < 2:
            print(f"  Warning: {lang} - unexpected structure, skipping")
            return False

        # Create the heading block
        heading_block = {
            "type": "heading",
            "level": 3,
            "content": HEADING_TRANSLATIONS[lang]
        }

        # Reorder: media, heading, paragraph1, paragraph2
        data['sections'] = [
            media_block,
            heading_block,
            paragraphs[0],
            paragraphs[1]
        ]

        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"  Updated: {lang}")
        return True

    except Exception as e:
        print(f"  Error processing {lang}: {e}")
        return False

def main():
    base_path = Path(__file__).parent.parent / "sources" / "locales" / "changelog"

    print("Updating 1.12.0-macos.json files...")
    print()

    updated = 0
    for lang in HEADING_TRANSLATIONS.keys():
        filepath = base_path / lang / "1.12.0-macos.json"
        if filepath.exists():
            if update_changelog_file(filepath, lang):
                updated += 1
        else:
            print(f"  Not found: {lang}")

    print()
    print(f"Done. Updated {updated} files.")

if __name__ == "__main__":
    main()
