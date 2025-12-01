#!/usr/bin/env python3
"""
Update pricing > ios > features with concise version.
Note: "Unlimited rolls" in English translates to "Unlimited film rolls" in other languages.
"""

import json
from pathlib import Path

# New concise features with translations
# Important: "film" = photography film (not movie)
features_by_locale = {
    'en': [
        "Unlimited rolls",
        "Subfolders",
        "Data export",
        "Metadata embedding",
        "iPhone & Mac apps"
    ],
    'de': [
        "Unbegrenzte Filmrollen",  # Film = photography film
        "Unterordner",
        "Datenexport",
        "Metadaten-Einbettung",
        "iPhone- und Mac-Apps"
    ],
    'fr': [
        "Pellicules illimitées",  # Pellicule = photography film (not "film" which means movie)
        "Sous-dossiers",
        "Export de données",
        "Intégration de métadonnées",
        "Applications iPhone et Mac"
    ],
    'it': [
        "Rullini illimitati",  # Rullino = film roll (not "film" which means movie)
        "Sottocartelle",
        "Esportazione dati",
        "Incorporazione metadati",
        "App iPhone e Mac"
    ],
    'pt': [
        "Rolos de filme ilimitados",  # Filme fotográfico (not cinema film)
        "Subpastas",
        "Exportação de dados",
        "Incorporação de metadados",
        "Apps para iPhone e Mac"
    ],
    'es': [
        "Rollos de película ilimitados",  # Película fotográfica (not cinema)
        "Subcarpetas",
        "Exportación de datos",
        "Integración de metadatos",
        "Apps de iPhone y Mac"
    ],
    'nl': [
        "Onbeperkte filmrollen",  # Film = photography film
        "Submappen",
        "Gegevensexport",
        "Metagegevens insluiten",
        "iPhone- en Mac-apps"
    ],
    'sv': [
        "Obegränsade filmrullar",  # Film = photography film
        "Undermappar",
        "Dataexport",
        "Metadata inbäddning",
        "iPhone- och Mac-appar"
    ],
    'da': [
        "Ubegrænset antal filmruller",  # Film = photography film
        "Undermapper",
        "Dataeksport",
        "Metadataindlejring",
        "iPhone- og Mac-apps"
    ],
    'nb': [
        "Ubegrensede filmruller",  # Film = photography film
        "Undermapper",
        "Dataeksport",
        "Metadata innbygging",
        "iPhone- og Mac-apper"
    ],
    'fi': [
        "Rajoittamaton määrä filmirullia",  # Filmi = photography film
        "Alikansiot",
        "Tietojen vienti",
        "Metatietojen upotus",
        "iPhone- ja Mac-sovellukset"
    ],
    'pl': [
        "Nieograniczona liczba rolek filmu",  # Film fotograficzny
        "Podfoldery",
        "Eksport danych",
        "Osadzanie metadanych",
        "Aplikacje na iPhone i Mac"
    ],
    'ru': [
        "Неограниченное количество плёнок",  # Плёнка = photo film (not кино)
        "Подпапки",
        "Экспорт данных",
        "Встраивание метаданных",
        "Приложения для iPhone и Mac"
    ],
    'uk': [
        "Необмежена кількість плівок",  # Плівка = photo film (not фільм cinema)
        "Підпапки",
        "Експорт даних",
        "Вбудовування метаданих",
        "Додатки для iPhone і Mac"
    ],
    'ro': [
        "Role de film nelimitate",  # Film fotografic
        "Subfoldere",
        "Export de date",
        "Încorporare metadate",
        "Aplicații iPhone și Mac"
    ],
    'tr': [
        "Sınırsız film rulosu",  # Film = photography film
        "Alt klasörler",
        "Veri dışa aktarma",
        "Metadata gömme",
        "iPhone ve Mac uygulamaları"
    ],
    'el': [
        "Απεριόριστα φιλμ",  # Φιλμ = photography film
        "Υποφάκελοι",
        "Εξαγωγή δεδομένων",
        "Ενσωμάτωση μεταδεδομένων",
        "Εφαρμογές iPhone και Mac"
    ],
    'ja': [
        "無制限のフィルムロール",  # フィルム = photography film (not 映画 movie)
        "サブフォルダ",
        "データエクスポート",
        "メタデータ埋め込み",
        "iPhoneおよびMacアプリ"
    ],
    'ko': [
        "무제한 필름 롤",  # 필름 = photography film (not 영화 movie)
        "하위 폴더",
        "데이터 내보내기",
        "메타데이터 삽입",
        "iPhone 및 Mac 앱"
    ],
    'hi': [
        "असीमित फ़िल्म रोल्स",  # फ़िल्म = photography film
        "उप-फ़ोल्डर",
        "डेटा निर्यात",
        "मेटाडेटा एम्बेडिंग",
        "iPhone और Mac ऐप्स"
    ],
    'zh': [
        "无限胶卷",  # 胶卷 = film roll (not 电影 movie)
        "子文件夹",
        "数据导出",
        "元数据嵌入",
        "iPhone 和 Mac 应用"
    ],
    'zh-hant': [
        "無限膠卷",  # 膠卷 = film roll (not 電影 movie)
        "子資料夾",
        "資料匯出",
        "元資料嵌入",
        "iPhone 和 Mac 應用程式"
    ],
    'id': [
        "Rol film tak terbatas",  # Film fotografi (not movie)
        "Subfolder",
        "Ekspor data",
        "Penyematan metadata",
        "Aplikasi iPhone & Mac"
    ],
    'vi': [
        "Cuộn phim không giới hạn",  # Phim ảnh (not movie)
        "Thư mục con",
        "Xuất dữ liệu",
        "Nhúng metadata",
        "Ứng dụng iPhone & Mac"
    ],
    'th': [
        "ฟิล์มม้วนไม่จำกัด",  # ฟิล์มถ่ายรูป (not หนัง movie)
        "โฟลเดอร์ย่อย",
        "ส่งออกข้อมูล",
        "ฝังเมตาดาต้า",
        "แอป iPhone และ Mac"
    ]
}

def update_locale_features(locales_dir):
    """Update features array in all locale files."""

    updated_count = 0
    error_count = 0

    for locale_code, new_features in features_by_locale.items():
        file_path = Path(locales_dir) / f"{locale_code}.json"

        if not file_path.exists():
            print(f"⚠️  File not found: {file_path}")
            error_count += 1
            continue

        try:
            # Read the file
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Update the features array
            if 'pricing' in data and 'ios' in data['pricing']:
                data['pricing']['ios']['features'] = new_features

                # Write back
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)

                print(f"✓ Updated {locale_code}.json - {new_features[0]}")
                updated_count += 1
            else:
                print(f"⚠️  Missing pricing.ios structure in {locale_code}.json")
                error_count += 1

        except Exception as e:
            print(f"❌ Error updating {locale_code}.json: {e}")
            error_count += 1

    print()
    print("=" * 60)
    print(f"✓ Successfully updated: {updated_count} files")
    if error_count > 0:
        print(f"❌ Errors: {error_count} files")
    print("=" * 60)

if __name__ == "__main__":
    locales_dir = "/Users/vnn/Documents/Dev/framesWeb/sources/locales"
    update_locale_features(locales_dir)
