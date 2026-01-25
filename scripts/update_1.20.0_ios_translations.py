#!/usr/bin/env python3
"""
Script to update 1.20.0-ios.json changelog files with version 1.20.3 patch,
new fixes, and new improvements across all supported languages.
"""

import json
import os
from pathlib import Path

# Base path for changelog locales
BASE_PATH = Path(__file__).parent.parent / "sources" / "locales" / "changelog"

# Translations for all new content
TRANSLATIONS = {
    "en": {
        "patch_description": "Clearer export options, fixed picker ordering, and improved localization.",
        "fix_title": "Frame picker ordering",
        "fix_description": "Fixed an issue where frame numbers appeared out of order in the form picker.",
        "improvement_1": "Added icons to the export menu to make finding formats easier",
        "improvement_2": "Localized camera permission descriptions to match device language"
    },
    "da": {
        "patch_description": "Tydeligere eksportmuligheder, rettet rækkefølge i vælger og forbedret lokalisering.",
        "fix_title": "Rækkefølge i rammevælger",
        "fix_description": "Rettet et problem, hvor rammenumre blev vist i forkert rækkefølge i formularvælgeren.",
        "improvement_1": "Tilføjet ikoner til eksportmenuen for nemmere at finde formater",
        "improvement_2": "Lokaliserede kameratilladelsebeskrivelser til at matche enhedens sprog"
    },
    "de": {
        "patch_description": "Klarere Exportoptionen, korrigierte Auswahlreihenfolge und verbesserte Lokalisierung.",
        "fix_title": "Einzelbild-Auswahlreihenfolge",
        "fix_description": "Ein Problem wurde behoben, bei dem Einzelbildnummern in der Formularauswahl in falscher Reihenfolge angezeigt wurden.",
        "improvement_1": "Symbole zum Exportmenü hinzugefügt, um Formate leichter zu finden",
        "improvement_2": "Kameraberechtigungsbeschreibungen an die Gerätesprache angepasst"
    },
    "el": {
        "patch_description": "Σαφέστερες επιλογές εξαγωγής, διορθωμένη σειρά επιλογέα και βελτιωμένη τοπική προσαρμογή.",
        "fix_title": "Σειρά επιλογέα καρέ",
        "fix_description": "Διορθώθηκε ένα πρόβλημα όπου οι αριθμοί καρέ εμφανίζονταν με λάθος σειρά στον επιλογέα φόρμας.",
        "improvement_1": "Προστέθηκαν εικονίδια στο μενού εξαγωγής για ευκολότερη εύρεση μορφών",
        "improvement_2": "Οι περιγραφές αδειών κάμερας προσαρμόστηκαν στη γλώσσα της συσκευής"
    },
    "es": {
        "patch_description": "Opciones de exportación más claras, orden del selector corregido y localización mejorada.",
        "fix_title": "Orden del selector de fotogramas",
        "fix_description": "Se corrigió un problema donde los números de fotograma aparecían desordenados en el selector del formulario.",
        "improvement_1": "Se añadieron iconos al menú de exportación para encontrar formatos más fácilmente",
        "improvement_2": "Descripciones de permisos de cámara localizadas para coincidir con el idioma del dispositivo"
    },
    "fi": {
        "patch_description": "Selkeämmät vientivaihtoehdot, korjattu valitsimen järjestys ja parannettu lokalisointi.",
        "fix_title": "Kehysvalitsimen järjestys",
        "fix_description": "Korjattiin ongelma, jossa kehysnumerot näkyivät väärässä järjestyksessä lomakevalitsimessa.",
        "improvement_1": "Lisätty kuvakkeet vienti-valikkoon muotojen löytämisen helpottamiseksi",
        "improvement_2": "Kameran käyttöoikeuskuvaukset lokalisoitu vastaamaan laitteen kieltä"
    },
    "fr": {
        "patch_description": "Options d'exportation plus claires, ordre du sélecteur corrigé et localisation améliorée.",
        "fix_title": "Ordre du sélecteur de frames",
        "fix_description": "Correction d'un problème où les numéros de frame apparaissaient dans le désordre dans le sélecteur de formulaire.",
        "improvement_1": "Ajout d'icônes au menu d'exportation pour trouver les formats plus facilement",
        "improvement_2": "Descriptions des autorisations de caméra localisées pour correspondre à la langue de l'appareil"
    },
    "hi": {
        "patch_description": "स्पष्ट निर्यात विकल्प, पिकर क्रम ठीक किया गया और बेहतर स्थानीयकरण।",
        "fix_title": "फ्रेम पिकर क्रम",
        "fix_description": "एक समस्या ठीक की गई जहां फॉर्म पिकर में फ्रेम नंबर गलत क्रम में दिखाई देते थे।",
        "improvement_1": "फॉर्मेट आसानी से खोजने के लिए निर्यात मेनू में आइकन जोड़े गए",
        "improvement_2": "कैमरा अनुमति विवरण डिवाइस भाषा से मेल खाने के लिए स्थानीयकृत"
    },
    "id": {
        "patch_description": "Opsi ekspor lebih jelas, urutan pemilih diperbaiki, dan lokalisasi ditingkatkan.",
        "fix_title": "Urutan pemilih frame",
        "fix_description": "Memperbaiki masalah di mana nomor frame muncul tidak berurutan di pemilih formulir.",
        "improvement_1": "Menambahkan ikon ke menu ekspor untuk memudahkan menemukan format",
        "improvement_2": "Deskripsi izin kamera dilokalkan sesuai bahasa perangkat"
    },
    "it": {
        "patch_description": "Opzioni di esportazione più chiare, ordine del selettore corretto e localizzazione migliorata.",
        "fix_title": "Ordine del selettore fotogrammi",
        "fix_description": "Risolto un problema per cui i numeri dei fotogrammi apparivano in ordine errato nel selettore del modulo.",
        "improvement_1": "Aggiunte icone al menu di esportazione per trovare i formati più facilmente",
        "improvement_2": "Descrizioni dei permessi della fotocamera localizzate per corrispondere alla lingua del dispositivo"
    },
    "ja": {
        "patch_description": "エクスポートオプションの明確化、ピッカーの順序修正、ローカライズの改善。",
        "fix_title": "コマピッカーの順序",
        "fix_description": "フォームピッカーでコマ番号が順不同で表示される問題を修正しました。",
        "improvement_1": "フォーマットを見つけやすくするためエクスポートメニューにアイコンを追加",
        "improvement_2": "カメラ許可の説明をデバイスの言語に合わせてローカライズ"
    },
    "ko": {
        "patch_description": "더 명확한 내보내기 옵션, 선택기 순서 수정 및 현지화 개선.",
        "fix_title": "프레임 선택기 순서",
        "fix_description": "폼 선택기에서 프레임 번호가 순서대로 표시되지 않는 문제를 수정했습니다.",
        "improvement_1": "형식을 쉽게 찾을 수 있도록 내보내기 메뉴에 아이콘 추가",
        "improvement_2": "카메라 권한 설명을 기기 언어에 맞게 현지화"
    },
    "nb": {
        "patch_description": "Tydeligere eksportalternativer, rettet rekkefølge i velger og forbedret lokalisering.",
        "fix_title": "Rekkefølge i rammevelger",
        "fix_description": "Rettet et problem der rammenumre ble vist i feil rekkefølge i skjemavelgeren.",
        "improvement_1": "Lagt til ikoner i eksportmenyen for å gjøre det enklere å finne formater",
        "improvement_2": "Lokaliserte kameratillatelsesbeskrivelser for å matche enhetens språk"
    },
    "nl": {
        "patch_description": "Duidelijkere exportopties, volgorde van kiezer hersteld en verbeterde lokalisatie.",
        "fix_title": "Volgorde filmframekiezer",
        "fix_description": "Een probleem opgelost waarbij filmframenummers in de verkeerde volgorde werden weergegeven in de formulierkiezer.",
        "improvement_1": "Pictogrammen toegevoegd aan het exportmenu om formaten makkelijker te vinden",
        "improvement_2": "Cameratoestemmingsbeschrijvingen gelokaliseerd naar de taal van het apparaat"
    },
    "pl": {
        "patch_description": "Wyraźniejsze opcje eksportu, poprawiona kolejność w selektorze i ulepszona lokalizacja.",
        "fix_title": "Kolejność selektora klatek",
        "fix_description": "Naprawiono problem, w którym numery klatek wyświetlały się w nieprawidłowej kolejności w selektorze formularza.",
        "improvement_1": "Dodano ikony do menu eksportu, aby łatwiej znajdować formaty",
        "improvement_2": "Zlokalizowano opisy uprawnień aparatu, aby pasowały do języka urządzenia"
    },
    "pt": {
        "patch_description": "Opções de exportação mais claras, ordem do seletor corrigida e localização melhorada.",
        "fix_title": "Ordem do seletor de fotogramas",
        "fix_description": "Corrigido um problema em que os números dos fotogramas apareciam fora de ordem no seletor do formulário.",
        "improvement_1": "Adicionados ícones ao menu de exportação para encontrar formatos mais facilmente",
        "improvement_2": "Descrições de permissões da câmera localizadas para corresponder ao idioma do dispositivo"
    },
    "ro": {
        "patch_description": "Opțiuni de export mai clare, ordine selector corectată și localizare îmbunătățită.",
        "fix_title": "Ordinea selectorului de cadre",
        "fix_description": "S-a remediat o problemă în care numerele cadrelor apăreau în ordine greșită în selectorul formularului.",
        "improvement_1": "S-au adăugat pictograme în meniul de export pentru a găsi formatele mai ușor",
        "improvement_2": "Descrierile permisiunilor camerei au fost localizate pentru a corespunde limbii dispozitivului"
    },
    "ru": {
        "patch_description": "Более понятные параметры экспорта, исправлен порядок в селекторе и улучшена локализация.",
        "fix_title": "Порядок селектора кадров",
        "fix_description": "Исправлена проблема, при которой номера кадров отображались в неправильном порядке в селекторе формы.",
        "improvement_1": "Добавлены значки в меню экспорта для удобного поиска форматов",
        "improvement_2": "Описания разрешений камеры локализованы в соответствии с языком устройства"
    },
    "sv": {
        "patch_description": "Tydligare exportalternativ, korrigerad ordning i väljaren och förbättrad lokalisering.",
        "fix_title": "Ordning i rutväljaren",
        "fix_description": "Åtgärdade ett problem där rutanummer visades i fel ordning i formulärväljaren.",
        "improvement_1": "Lagt till ikoner i exportmenyn för att lättare hitta format",
        "improvement_2": "Lokaliserade kamerabehörighetsbeskrivningar för att matcha enhetens språk"
    },
    "th": {
        "patch_description": "ตัวเลือกส่งออกชัดเจนขึ้น แก้ไขลำดับตัวเลือก และปรับปรุงการแปลภาษา",
        "fix_title": "ลำดับตัวเลือกเฟรม",
        "fix_description": "แก้ไขปัญหาที่หมายเลขเฟรมแสดงไม่เรียงลำดับในตัวเลือกฟอร์ม",
        "improvement_1": "เพิ่มไอคอนในเมนูส่งออกเพื่อให้ค้นหารูปแบบได้ง่ายขึ้น",
        "improvement_2": "แปลคำอธิบายสิทธิ์กล้องให้ตรงกับภาษาของอุปกรณ์"
    },
    "tr": {
        "patch_description": "Daha net dışa aktarma seçenekleri, düzeltilmiş seçici sıralaması ve geliştirilmiş yerelleştirme.",
        "fix_title": "Kare seçici sıralaması",
        "fix_description": "Form seçicide kare numaralarının yanlış sırada görüntülenmesi sorunu düzeltildi.",
        "improvement_1": "Formatları daha kolay bulmak için dışa aktarma menüsüne simgeler eklendi",
        "improvement_2": "Kamera izin açıklamaları cihaz diline uyacak şekilde yerelleştirildi"
    },
    "uk": {
        "patch_description": "Чіткіші параметри експорту, виправлено порядок у селекторі та покращено локалізацію.",
        "fix_title": "Порядок селектора кадрів",
        "fix_description": "Виправлено проблему, через яку номери кадрів відображалися в неправильному порядку в селекторі форми.",
        "improvement_1": "Додано іконки до меню експорту для зручнішого пошуку форматів",
        "improvement_2": "Локалізовано описи дозволів камери відповідно до мови пристрою"
    },
    "vi": {
        "patch_description": "Tùy chọn xuất rõ ràng hơn, sửa thứ tự bộ chọn và cải thiện bản địa hóa.",
        "fix_title": "Thứ tự bộ chọn khung hình",
        "fix_description": "Đã sửa lỗi số khung hình hiển thị không đúng thứ tự trong bộ chọn biểu mẫu.",
        "improvement_1": "Thêm biểu tượng vào menu xuất để tìm định dạng dễ dàng hơn",
        "improvement_2": "Bản địa hóa mô tả quyền camera phù hợp với ngôn ngữ thiết bị"
    },
    "zh-hant": {
        "patch_description": "更清晰的匯出選項、修正選擇器順序及改進本地化。",
        "fix_title": "畫格選擇器順序",
        "fix_description": "修正了表單選擇器中畫格編號顯示順序錯誤的問題。",
        "improvement_1": "在匯出選單中新增圖示，更容易找到格式",
        "improvement_2": "相機權限說明已本地化以符合裝置語言"
    },
    "zh": {
        "patch_description": "更清晰的导出选项、修复选择器顺序及改进本地化。",
        "fix_title": "帧选择器顺序",
        "fix_description": "修复了表单选择器中帧编号显示顺序错误的问题。",
        "improvement_1": "在导出菜单中添加图标，更容易找到格式",
        "improvement_2": "相机权限说明已本地化以匹配设备语言"
    }
}


def update_changelog_file(lang_code: str, file_path: Path) -> bool:
    """Update a single changelog file with new translations."""

    if lang_code not in TRANSLATIONS:
        print(f"  Skipping {lang_code}: No translations available")
        return False

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"  File not found: {file_path}")
        return False
    except json.JSONDecodeError as e:
        print(f"  JSON error in {file_path}: {e}")
        return False

    trans = TRANSLATIONS[lang_code]

    # Add new patch entry (1.20.3)
    new_patch = {
        "version": "1.20.3",
        "description": trans["patch_description"]
    }

    # Check if patch already exists
    existing_versions = [p.get("version") for p in data.get("patches", [])]
    if "1.20.3" not in existing_versions:
        data.setdefault("patches", []).append(new_patch)

    # Add new fix entry
    new_fix = {
        "title": trans["fix_title"],
        "description": trans["fix_description"]
    }

    # Check if fix already exists (by title)
    existing_fix_titles = [f.get("title") for f in data.get("fixes", [])]
    if trans["fix_title"] not in existing_fix_titles:
        data.setdefault("fixes", []).append(new_fix)

    # Add new improvements
    improvements = data.setdefault("improvements", [])
    if trans["improvement_1"] not in improvements:
        improvements.append(trans["improvement_1"])
    if trans["improvement_2"] not in improvements:
        improvements.append(trans["improvement_2"])

    # Write back the updated file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')  # Add trailing newline

    return True


def main():
    """Main function to update all language files."""

    print("Updating 1.20.0-ios.json changelog files...\n")

    updated = 0
    skipped = 0
    errors = 0

    # Get all language directories
    if not BASE_PATH.exists():
        print(f"Error: Base path does not exist: {BASE_PATH}")
        return

    for lang_dir in sorted(BASE_PATH.iterdir()):
        if not lang_dir.is_dir():
            continue

        lang_code = lang_dir.name
        file_path = lang_dir / "1.20.0-ios.json"

        if not file_path.exists():
            print(f"  {lang_code}: File does not exist, skipping")
            skipped += 1
            continue

        print(f"  {lang_code}: ", end="")

        if update_changelog_file(lang_code, file_path):
            print("Updated")
            updated += 1
        else:
            errors += 1

    print(f"\nDone! Updated: {updated}, Skipped: {skipped}, Errors: {errors}")


if __name__ == "__main__":
    main()
