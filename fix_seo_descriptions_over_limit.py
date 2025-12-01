#!/usr/bin/env python3
"""
Fix SEO descriptions that went over 160 character limit.
"""

import json
from pathlib import Path

# Fixed descriptions under 160 chars
description_fixes = {
    'it': 'Registra impostazioni fotocamera con precisione. Organizza pellicole, registra scatti e incorpora metadati EXIF. App fotografia analogica per iPhone & Mac.',
    'pt': 'Registre configurações da câmera com precisão. Organize filmes, registre fotos e incorpore metadados EXIF. Aplicação fotografia analógica para iPhone & Mac.',
    'sv': 'Spåra kamerainställningar med precision. Organisera filmer, logga tagningar och bädda in EXIF-metadata. App för analog fotografering för iPhone & Mac.',
    'da': 'Registrer kameraindstillinger med præcision. Organiser film, log optagelser og integrer EXIF-metadata. Analog fotografi-app til iPhone & Mac.',
    'nb': 'Registrer kamerainnstillinger med presisjon. Organiser filmer, logg opptak og integrer EXIF-metadata. Analog fotografi-app for iPhone & Mac.',
    'ru': 'Записывайте настройки камеры с точностью. Организуйте плёнки, регистрируйте снимки и встраивайте EXIF-метаданные. Приложение для iPhone и Mac.',
    'uk': 'Записуйте налаштування камери з точністю. Організовуйте плівки, реєструйте знімки та вбудовуйте EXIF-метадані. Додаток для iPhone та Mac.',
    'ro': 'Înregistrează setările camerei cu precizie. Organizează filme, înregistrează cadre și integrează metadate EXIF. Aplicație fotografie analogică pentru iPhone și Mac.',
    'tr': 'Kamera ayarlarını hassasiyetle kaydedin. Filmleri düzenleyin, çekimleri kaydedin ve EXIF meta verisini ekleyin. Analog fotoğrafçılık uygulaması iPhone ve Mac için.',
    'el': 'Καταγράψτε ρυθμίσεις κάμερας με ακρίβεια. Οργανώστε φιλμ, καταγράψτε λήψεις και ενσωματώστε EXIF metadata. Εφαρμογή αναλογικής φωτογραφίας για iPhone & Mac.',
    'id': 'Lacak pengaturan kamera dengan presisi. Atur film, catat pengambilan gambar dan sisipkan metadata EXIF. Aplikasi fotografi analog untuk iPhone & Mac.'
}

def fix_descriptions(locales_dir):
    """Fix descriptions that are over 160 characters."""

    updated_count = 0
    error_count = 0

    for locale_code, description in description_fixes.items():
        file_path = Path(locales_dir) / f"{locale_code}.json"

        if not file_path.exists():
            print(f"⚠️  File not found: {file_path}")
            error_count += 1
            continue

        try:
            # Read the file
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Update meta.description
            data['meta']['description'] = description

            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            desc_len = len(description)
            print(f"✓ Fixed {locale_code:8} → desc: {desc_len:3} chars")
            updated_count += 1

        except Exception as e:
            print(f"❌ Error fixing {locale_code}: {e}")
            error_count += 1

    print()
    print("=" * 70)
    print(f"✓ Successfully fixed: {updated_count} files")
    if error_count > 0:
        print(f"❌ Errors: {error_count} files")
    print("=" * 70)

if __name__ == "__main__":
    locales_dir = "/Users/vnn/Documents/Dev/framesWeb/sources/locales"
    fix_descriptions(locales_dir)
