#!/usr/bin/env python3
"""
Update SEO title and description for remaining 19 languages.
Following EN/FR pattern with "app" keyword in title where space allows.
"""

import json
from pathlib import Path

# Updated SEO metadata for each language
seo_updates = {
    'de': {
        'title': 'Frames: Filmfotografie-Notizbuch-App für Analogfotografen',
        'description': 'Kameraeinstellungen präzise erfassen. Filme organisieren, Aufnahmen loggen und EXIF-Metadaten in Scans einbetten. Analogfotografie-Notizbuch-App für iOS & Mac.'
    },
    'nl': {
        'title': 'Frames: Filmfotografie-notitieboek voor analoge fotografen',
        'description': 'Leg camera-instellingen precies vast. Organiseer films, log opnames en voeg EXIF-metadata in scans. Analoge fotografie-notitieboek-app voor iOS & Mac.'
    },
    'ja': {
        'title': 'Frames: アナログ写真家のためのフィルム写真ノートアプリ',
        'description': 'カメラ設定を精密に記録。フィルムを整理、撮影をログ、スキャンにEXIFメタデータを埋め込み。アナログ写真ノートアプリ、iOS & Mac対応。'
    },
    'es': {
        'title': 'Frames: Cuaderno fotografía analógica app para fotógrafos',
        'description': 'Registra ajustes de cámara con precisión. Organiza películas, registra tomas e integra metadatos EXIF. Aplicación de fotografía analógica para iOS & Mac.'
    },
    'it': {
        'title': 'Frames: Quaderno fotografia analogica app per fotografi',
        'description': 'Registra impostazioni fotocamera con precisione. Organizza pellicole, registra scatti e incorpora metadati EXIF. Applicazione fotografia analogica per iPhone & Mac.'
    },
    'pt': {
        'title': 'Frames: Caderno de fotografia analógica app para fotógrafos',
        'description': 'Registre configurações da câmera com precisão. Organize filmes, registre fotos e incorpore metadados EXIF em digitalizações. Aplicação fotografia analógica para iPhone & Mac.'
    },
    'sv': {
        'title': 'Frames: Filmfotografi-anteckningsbok-app för fotografer',
        'description': 'Spåra kamerainställningar med precision. Organisera filmer, logga tagningar och bädda in EXIF-metadata i skanningar. Applikation för analog fotografering för iPhone & Mac.'
    },
    'da': {
        'title': 'Frames: Filmfotografi-notesbog-app til analoge fotografer',
        'description': 'Registrer kameraindstillinger med præcision. Organiser film, log optagelser og integrer EXIF-metadata i scanninger. Analog fotografi-applikation til iPhone & Mac.'
    },
    'nb': {
        'title': 'Frames: Filmfotografi-notatbok-app for analoge fotografer',
        'description': 'Registrer kamerainnstillinger med presisjon. Organiser filmer, logg opptak og integrer EXIF-metadata i skanninger. Analog fotografi-applikasjon for iPhone & Mac.'
    },
    'fi': {
        'title': 'Frames: Filmikuvausmuistikirja analogivalokuvaajille',
        'description': 'Tallenna kamera-asetukset tarkasti. Järjestä filmit, kirjaa otokset ja upota EXIF-metadata skannauksiin. Analogisen valokuvauksen sovellus iPhonelle & Macille.'
    },
    'pl': {
        'title': 'Frames: Notes fotografii analogowej dla fotografów',
        'description': 'Śledź ustawienia aparatu z precyzją. Organizuj filmy, rejestruj zdjęcia i osadzaj metadane EXIF w skanach. Aplikacja fotografii analogowej na iPhone i Mac.'
    },
    'ru': {
        'title': 'Frames: Блокнот плёночной фотографии для фотографов',
        'description': 'Записывайте настройки камеры с точностью. Организуйте плёнки, регистрируйте снимки и встраивайте EXIF-метаданные в сканы. Приложение аналоговой фотографии для iPhone и Mac.'
    },
    'uk': {
        'title': 'Frames: Блокнот-додаток плівкової фотографії для фотографів',
        'description': 'Записуйте налаштування камери з точністю. Організовуйте плівки, реєструйте знімки та вбудовуйте EXIF-метадані у скани. Додаток аналогової фотографії для iPhone та Mac.'
    },
    'ro': {
        'title': 'Frames: Caiet de fotografie analogică pentru fotografi',
        'description': 'Înregistrează setările camerei cu precizie. Organizează filme, înregistrează cadre și integrează metadate EXIF în scanări. Aplicație fotografie analogică pentru iPhone și Mac.'
    },
    'tr': {
        'title': 'Frames: Analog fotoğrafçılar için film fotoğraf defteri',
        'description': 'Kamera ayarlarını hassasiyetle kaydedin. Filmleri düzenleyin, çekimleri kaydedin ve EXIF meta verisini taramalara yerleştirin. Analog fotoğrafçılık uygulaması iPhone ve Mac için.'
    },
    'el': {
        'title': 'Frames: Σημειωματάριο αναλογικής φωτογραφίας για φωτογράφους',
        'description': 'Καταγράψτε ρυθμίσεις κάμερας με ακρίβεια. Οργανώστε φιλμ, καταγράψτε λήψεις και ενσωματώστε EXIF metadata σε σαρώσεις. Εφαρμογή αναλογικής φωτογραφίας για iPhone & Mac.'
    },
    'ko': {
        'title': 'Frames: 아날로그 사진가를 위한 필름 사진 노트 앱',
        'description': '카메라 설정을 정밀하게 기록. 필름 정리, 촬영 기록, 스캔에 EXIF 메타데이터 삽입. 아날로그 사진 애플리케이션, iPhone & Mac 지원.'
    },
    'hi': {
        'title': 'Frames: एनालॉग फोटोग्राफरों के लिए फिल्म फोटोग्राफी नोटबुक',
        'description': 'कैमरा सेटिंग्स को सटीकता से रिकॉर्ड करें। फिल्में व्यवस्थित करें, शॉट्स लॉग करें और EXIF मेटाडेटा एम्बेड करें। एनालॉग फोटोग्राफी एप्लिकेशन iPhone और Mac के लिए।'
    },
    'zh': {
        'title': 'Frames: 胶片摄影笔记本 - 为模拟摄影师',
        'description': '精确记录相机设置。整理胶片、记录拍摄、将 EXIF 元数据嵌入扫描。模拟摄影应用程序，支持 iPhone 和 Mac。'
    },
    'zh-hant': {
        'title': 'Frames: 底片攝影筆記本 - 為類比攝影師',
        'description': '精確記錄相機設定。整理底片、記錄拍攝、將 EXIF 中繼資料嵌入掃描。類比攝影應用程式，支援 iPhone 和 Mac。'
    },
    'id': {
        'title': 'Frames: Buku catatan fotografi analog untuk fotografer',
        'description': 'Lacak pengaturan kamera dengan presisi. Atur film, catat pengambilan gambar, dan sisipkan metadata EXIF ke hasil scan. Aplikasi fotografi analog untuk iPhone & Mac.'
    },
    'vi': {
        'title': 'Frames: Ứng dụng sổ tay nhiếp ảnh analog cho nhiếp ảnh gia',
        'description': 'Ghi lại cài đặt máy ảnh chính xác. Sắp xếp phim, ghi nhật ký chụp và nhúng siêu dữ liệu EXIF vào ảnh scan. Ứng dụng nhiếp ảnh analog cho iPhone & Mac.'
    },
    'th': {
        'title': 'Frames: สมุดบันทึกภาพอนาล็อกสำหรับช่างภาพ',
        'description': 'บันทึกการตั้งค่ากล้องอย่างแม่นยำ จัดระเบียบฟิล์ม บันทึกการถ่าย และฝังข้อมูลเมตา EXIF ลงในภาพสแกน แอปพลิเคชันถ่ายภาพอนาล็อกสำหรับ iPhone และ Mac'
    }
}

def update_seo_metadata(locales_dir):
    """Update title and description in meta section for all specified languages."""

    updated_count = 0
    error_count = 0

    for locale_code, seo_data in seo_updates.items():
        file_path = Path(locales_dir) / f"{locale_code}.json"

        if not file_path.exists():
            print(f"⚠️  File not found: {file_path}")
            error_count += 1
            continue

        try:
            # Read the file
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Update meta.title and meta.description
            if 'meta' not in data:
                data['meta'] = {}

            data['meta']['title'] = seo_data['title']
            data['meta']['description'] = seo_data['description']

            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            title_len = len(seo_data['title'])
            desc_len = len(seo_data['description'])
            print(f"✓ Updated {locale_code:8} → title: {title_len:2} chars, desc: {desc_len:3} chars")
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
    locales_dir = "/Users/vnn/Documents/Dev/framesWeb/sources/locales"
    update_seo_metadata(locales_dir)
