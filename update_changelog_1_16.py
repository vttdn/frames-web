#!/usr/bin/env python3
"""
Update title and meta_title for 1.16.0-ios changelog across all languages.
"""

import json
from pathlib import Path

# Translations for the new title
titles_by_locale = {
    'en': {
        'title': 'Lifetime Purchase Option Now Available',
        'meta_title': 'Lifetime Purchase Option Now Available - Frames'
    },
    'de': {
        'title': 'Einmalige Kaufoption jetzt verfügbar',
        'meta_title': 'Einmalige Kaufoption jetzt verfügbar - Frames'
    },
    'fr': {
        'title': 'Achat à vie désormais disponible',
        'meta_title': 'Achat à vie désormais disponible - Frames'
    },
    'it': {
        'title': 'Acquisto a vita ora disponibile',
        'meta_title': 'Acquisto a vita ora disponibile - Frames'
    },
    'pt': {
        'title': 'Opção de compra vitalícia agora disponível',
        'meta_title': 'Opção de compra vitalícia agora disponível - Frames'
    },
    'es': {
        'title': 'Opción de compra de por vida ahora disponible',
        'meta_title': 'Opción de compra de por vida ahora disponible - Frames'
    },
    'nl': {
        'title': 'Levenslange aankoopoptie nu beschikbaar',
        'meta_title': 'Levenslange aankoopoptie nu beschikbaar - Frames'
    },
    'sv': {
        'title': 'Livstidsköp nu tillgängligt',
        'meta_title': 'Livstidsköp nu tillgängligt - Frames'
    },
    'da': {
        'title': 'Livstidskøb nu tilgængeligt',
        'meta_title': 'Livstidskøb nu tilgængeligt - Frames'
    },
    'nb': {
        'title': 'Livstidskjøp nå tilgjengelig',
        'meta_title': 'Livstidskjøp nå tilgjengelig - Frames'
    },
    'fi': {
        'title': 'Elinikäinen osto nyt saatavilla',
        'meta_title': 'Elinikäinen osto nyt saatavilla - Frames'
    },
    'pl': {
        'title': 'Opcja zakupu dożywotniego już dostępna',
        'meta_title': 'Opcja zakupu dożywotniego już dostępna - Frames'
    },
    'ru': {
        'title': 'Доступна опция пожизненной покупки',
        'meta_title': 'Доступна опция пожизненной покупки - Frames'
    },
    'uk': {
        'title': 'Доступна опція довічної покупки',
        'meta_title': 'Доступна опція довічної покупки - Frames'
    },
    'ro': {
        'title': 'Opțiunea de achiziție pe viață acum disponibilă',
        'meta_title': 'Opțiunea de achiziție pe viață acum disponibilă - Frames'
    },
    'tr': {
        'title': 'Ömür boyu satın alma seçeneği artık mevcut',
        'meta_title': 'Ömür boyu satın alma seçeneği artık mevcut - Frames'
    },
    'el': {
        'title': 'Διαθέσιμη η επιλογή αγοράς εφ\' όρου ζωής',
        'meta_title': 'Διαθέσιμη η επιλογή αγοράς εφ\' όρου ζωής - Frames'
    },
    'ja': {
        'title': '買い切り購入オプションが利用可能に',
        'meta_title': '買い切り購入オプションが利用可能に - Frames'
    },
    'ko': {
        'title': '평생 구매 옵션 출시',
        'meta_title': '평생 구매 옵션 출시 - Frames'
    },
    'hi': {
        'title': 'आजीवन खरीद विकल्प अब उपलब्ध',
        'meta_title': 'आजीवन खरीद विकल्प अब उपलब्ध - Frames'
    },
    'zh': {
        'title': '现已提供终身购买选项',
        'meta_title': '现已提供终身购买选项 - Frames'
    },
    'zh-hant': {
        'title': '現已提供終身購買選項',
        'meta_title': '現已提供終身購買選項 - Frames'
    },
    'id': {
        'title': 'Opsi pembelian seumur hidup kini tersedia',
        'meta_title': 'Opsi pembelian seumur hidup kini tersedia - Frames'
    },
    'vi': {
        'title': 'Tùy chọn mua trọn đời hiện đã có',
        'meta_title': 'Tùy chọn mua trọn đời hiện đã có - Frames'
    },
    'th': {
        'title': 'ตัวเลือกซื้อแบบตลอดชีพพร้อมแล้ว',
        'meta_title': 'ตัวเลือกซื้อแบบตลอดชีพพร้อมแล้ว - Frames'
    }
}

def update_changelog_titles(changelog_dir):
    """Update title and meta_title in all 1.16.0-ios.json files."""

    updated_count = 0
    error_count = 0

    for locale_code, titles in titles_by_locale.items():
        file_path = Path(changelog_dir) / locale_code / "1.16.0-ios.json"

        if not file_path.exists():
            print(f"⚠️  File not found: {file_path}")
            error_count += 1
            continue

        try:
            # Read the file
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Update title and meta_title
            data['title'] = titles['title']
            data['meta_title'] = titles['meta_title']

            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            print(f"✓ Updated {locale_code:8} → {titles['title']}")
            updated_count += 1

        except Exception as e:
            print(f"❌ Error updating {locale_code}: {e}")
            error_count += 1

    print()
    print("=" * 70)
    print(f"✓ Successfully updated: {updated_count} files")
    if error_count > 0:
        print(f"❌ Errors: {error_count} files")
    print("=" * 70)

if __name__ == "__main__":
    changelog_dir = "/Users/vnn/Documents/Dev/framesWeb/sources/locales/changelog"
    update_changelog_titles(changelog_dir)
