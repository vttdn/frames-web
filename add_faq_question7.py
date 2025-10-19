#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add FAQ question 7 to all language locale files.
"""

import json
import sys
from pathlib import Path

# Language code mapping
TRANSLATIONS = {
    "da": {
        "question": "Kan jeg synkronisere mine data mellem iPhone og Mac?",
        "answer": "Ja, du kan problemfrit overføre dine filmfotografidata mellem iPhone og Mac ved hjælp af .frames-fileksport. Eksporter simpelthen dine ruller fra én enhed og importer dem på en anden. Selvom automatisk cloud-synkronisering ikke er tilgængelig i øjeblikket for at bevare dit privatliv og dit dataejerskab, gør .frames-formatet manuel synkronisering hurtig og ligetil. Fremtidige opdateringer kan inkludere valgfri iCloud-synkronisering for Pro-brugere."
    },
    "nl": {
        "question": "Kan ik mijn gegevens synchroniseren tussen iPhone en Mac?",
        "answer": "Ja, je kunt je filmfotografiegegevens naadloos overzetten tussen iPhone en Mac met behulp van .frames-bestandsexporten. Exporteer simpelweg je rolletjes van het ene apparaat en importeer ze op het andere. Hoewel automatische cloudsynchronisatie momenteel niet beschikbaar is om je privacy en gegevenseigendom te behouden, maakt het .frames-formaat handmatige synchronisatie snel en eenvoudig. Toekomstige updates kunnen optionele iCloud-synchronisatie voor Pro-gebruikers bevatten."
    },
    "fi": {
        "question": "Voinko synkronoida tietoni iPhonen ja Macin välillä?",
        "answer": "Kyllä, voit siirtää filmivalokuvauksen tietosi saumattomasti iPhonen ja Macin välillä käyttämällä .frames-tiedostojen vientiä. Vie yksinkertaisesti rullasi yhdestä laitteesta ja tuo ne toiseen. Vaikka automaattinen pilvisynkronointi ei ole tällä hetkellä saatavilla yksityisyytesi ja tietojesi omistajuuden säilyttämiseksi, .frames-muoto tekee manuaalisesta synkronoinnista nopeaa ja suoraviivaista. Tulevat päivitykset voivat sisältää valinnaisen iCloud-synkronoinnin Pro-käyttäjille."
    },
    "fr": {
        "question": "Puis-je synchroniser mes données entre iPhone et Mac ?",
        "answer": "Oui, vous pouvez transférer facilement vos données de photographie argentique entre iPhone et Mac en utilisant les exportations de fichiers .frames. Exportez simplement vos pellicules d'un appareil et importez-les sur un autre. Bien que la synchronisation cloud automatique ne soit pas actuellement disponible pour préserver votre vie privée et la propriété de vos données, le format .frames rend la synchronisation manuelle rapide et simple. Les futures mises à jour pourront inclure une synchronisation iCloud optionnelle pour les utilisateurs Pro."
    },
    "de": {
        "question": "Kann ich meine Daten zwischen iPhone und Mac synchronisieren?",
        "answer": "Ja, Sie können Ihre Filmfotografie-Daten nahtlos zwischen iPhone und Mac übertragen, indem Sie .frames-Dateiexporte verwenden. Exportieren Sie einfach Ihre Filme von einem Gerät und importieren Sie sie auf einem anderen. Obwohl die automatische Cloud-Synchronisierung derzeit nicht verfügbar ist, um Ihre Privatsphäre und Ihr Dateneigentum zu wahren, macht das .frames-Format die manuelle Synchronisierung schnell und unkompliziert. Zukünftige Updates könnten eine optionale iCloud-Synchronisierung für Pro-Benutzer enthalten."
    },
    "el": {
        "question": "Μπορώ να συγχρονίσω τα δεδομένα μου μεταξύ iPhone και Mac;",
        "answer": "Ναι, μπορείτε να μεταφέρετε απρόσκοπτα τα δεδομένα φωτογραφίας φιλμ σας μεταξύ iPhone και Mac χρησιμοποιώντας εξαγωγές αρχείων .frames. Απλά εξάγετε τα φιλμ σας από μία συσκευή και εισάγετέ τα σε άλλη. Ενώ ο αυτόματος συγχρονισμός cloud δεν είναι επί του παρόντος διαθέσιμος για να διατηρηθεί το απόρρητο και η κυριότητα των δεδομένων σας, η μορφή .frames καθιστά τον χειροκίνητο συγχρονισμό γρήγορο και απλό. Μελλοντικές ενημερώσεις μπορεί να περιλαμβάνουν προαιρετικό συγχρονισμό iCloud για χρήστες Pro."
    },
    "hi": {
        "question": "क्या मैं iPhone और Mac के बीच अपना डेटा सिंक कर सकता हूं?",
        "answer": "हां, आप .frames फ़ाइल निर्यात का उपयोग करके iPhone और Mac के बीच अपने फिल्म फोटोग्राफी डेटा को सहजता से स्थानांतरित कर सकते हैं। बस एक डिवाइस से अपने रोल निर्यात करें और उन्हें दूसरे पर आयात करें। जबकि आपकी गोपनीयता और डेटा स्वामित्व बनाए रखने के लिए स्वचालित क्लाउड सिंक वर्तमान में उपलब्ध नहीं है, .frames प्रारूप मैनुअल सिंकिंग को त्वरित और सीधा बनाता है। भविष्य के अपडेट में Pro उपयोगकर्ताओं के लिए वैकल्पिक iCloud सिंक शामिल हो सकता है।"
    },
    "id": {
        "question": "Bisakah saya menyinkronkan data saya antara iPhone dan Mac?",
        "answer": "Ya, Anda dapat mentransfer data fotografi film Anda dengan mulus antara iPhone dan Mac menggunakan ekspor file .frames. Cukup ekspor rol Anda dari satu perangkat dan impor ke perangkat lain. Meskipun sinkronisasi cloud otomatis saat ini tidak tersedia untuk menjaga privasi dan kepemilikan data Anda, format .frames membuat sinkronisasi manual menjadi cepat dan mudah. Pembaruan di masa mendatang mungkin menyertakan sinkronisasi iCloud opsional untuk pengguna Pro."
    },
    "it": {
        "question": "Posso sincronizzare i miei dati tra iPhone e Mac?",
        "answer": "Sì, puoi trasferire facilmente i tuoi dati di fotografia analogica tra iPhone e Mac utilizzando le esportazioni di file .frames. Esporta semplicemente i tuoi rullini da un dispositivo e importali su un altro. Sebbene la sincronizzazione cloud automatica non sia attualmente disponibile per mantenere la tua privacy e la proprietà dei dati, il formato .frames rende la sincronizzazione manuale rapida e semplice. Gli aggiornamenti futuri potrebbero includere la sincronizzazione iCloud opzionale per gli utenti Pro."
    },
    "ja": {
        "question": "iPhoneとMac間でデータを同期できますか？",
        "answer": "はい、.framesファイルのエクスポートを使用して、iPhoneとMac間でフィルム写真データをシームレスに転送できます。一方のデバイスからロールをエクスポートし、もう一方のデバイスにインポートするだけです。プライバシーとデータ所有権を維持するために自動クラウド同期は現在利用できませんが、.frames形式により手動同期が迅速かつ簡単になります。将来のアップデートでは、Proユーザー向けにオプションのiCloud同期が含まれる可能性があります。"
    },
    "ko": {
        "question": "iPhone과 Mac 간에 데이터를 동기화할 수 있나요?",
        "answer": "예, .frames 파일 내보내기를 사용하여 iPhone과 Mac 간에 필름 사진 데이터를 원활하게 전송할 수 있습니다. 한 기기에서 롤을 내보내고 다른 기기로 가져오기만 하면 됩니다. 개인정보 보호와 데이터 소유권을 유지하기 위해 자동 클라우드 동기화는 현재 사용할 수 없지만, .frames 형식을 사용하면 수동 동기화가 빠르고 간단합니다. 향후 업데이트에는 Pro 사용자를 위한 선택적 iCloud 동기화가 포함될 수 있습니다."
    },
    "nb": {
        "question": "Kan jeg synkronisere dataene mine mellom iPhone og Mac?",
        "answer": "Ja, du kan sømløst overføre filmfotografidataene dine mellom iPhone og Mac ved hjelp av .frames-fileksport. Eksporter ganske enkelt rullene dine fra én enhet og importer dem på en annen. Selv om automatisk skysynkronisering ikke er tilgjengelig for øyeblikket for å opprettholde personvernet og dataeierskapet ditt, gjør .frames-formatet manuell synkronisering rask og enkel. Fremtidige oppdateringer kan inkludere valgfri iCloud-synkronisering for Pro-brukere."
    },
    "pl": {
        "question": "Czy mogę synchronizować swoje dane między iPhone a Mac?",
        "answer": "Tak, możesz bezproblemowo przesyłać swoje dane z fotografii filmowej między iPhone a Mac za pomocą eksportu plików .frames. Po prostu wyeksportuj swoje rolki z jednego urządzenia i zaimportuj je na drugim. Chociaż automatyczna synchronizacja w chmurze nie jest obecnie dostępna, aby chronić Twoją prywatność i własność danych, format .frames sprawia, że ręczna synchronizacja jest szybka i prosta. Przyszłe aktualizacje mogą obejmować opcjonalną synchronizację iCloud dla użytkowników Pro."
    },
    "pt": {
        "question": "Posso sincronizar meus dados entre iPhone e Mac?",
        "answer": "Sim, você pode transferir perfeitamente seus dados de fotografia analógica entre iPhone e Mac usando exportações de arquivo .frames. Simplesmente exporte seus rolos de um dispositivo e importe-os em outro. Embora a sincronização automática na nuvem não esteja disponível no momento para manter sua privacidade e propriedade dos dados, o formato .frames torna a sincronização manual rápida e direta. Atualizações futuras podem incluir sincronização iCloud opcional para usuários Pro."
    },
    "ro": {
        "question": "Pot sincroniza datele între iPhone și Mac?",
        "answer": "Da, poți transfera fără probleme datele tale de fotografie pe film între iPhone și Mac folosind exporturi de fișiere .frames. Exportă pur și simplu filmele tale de pe un dispozitiv și importă-le pe altul. Deși sincronizarea automată în cloud nu este disponibilă momentan pentru a-ți menține confidențialitatea și proprietatea datelor, formatul .frames face sincronizarea manuală rapidă și simplă. Actualizările viitoare ar putea include sincronizare iCloud opțională pentru utilizatorii Pro."
    },
    "ru": {
        "question": "Могу ли я синхронизировать свои данные между iPhone и Mac?",
        "answer": "Да, вы можете легко переносить данные плёночной фотографии между iPhone и Mac, используя экспорт файлов .frames. Просто экспортируйте свои плёнки с одного устройства и импортируйте их на другое. Хотя автоматическая облачная синхронизация в настоящее время недоступна для сохранения вашей конфиденциальности и владения данными, формат .frames делает ручную синхронизацию быстрой и простой. Будущие обновления могут включать опциональную синхронизацию iCloud для пользователей Pro."
    },
    "zh": {
        "question": "我可以在 iPhone 和 Mac 之间同步数据吗？",
        "answer": "可以，您可以使用 .frames 文件导出功能在 iPhone 和 Mac 之间无缝传输胶片摄影数据。只需从一台设备导出您的胶卷并在另一台设备上导入即可。虽然为了保护您的隐私和数据所有权，目前还没有自动云同步功能，但 .frames 格式使手动同步变得快速而简单。未来的更新可能会为 Pro 用户提供可选的 iCloud 同步功能。"
    },
    "es": {
        "question": "¿Puedo sincronizar mis datos entre iPhone y Mac?",
        "answer": "Sí, puedes transferir sin problemas tus datos de fotografía analógica entre iPhone y Mac usando exportaciones de archivos .frames. Simplemente exporta tus rollos desde un dispositivo e impórtalos en otro. Aunque la sincronización automática en la nube no está disponible actualmente para mantener tu privacidad y propiedad de datos, el formato .frames hace que la sincronización manual sea rápida y sencilla. Las actualizaciones futuras pueden incluir sincronización iCloud opcional para usuarios Pro."
    },
    "sv": {
        "question": "Kan jag synkronisera mina data mellan iPhone och Mac?",
        "answer": "Ja, du kan sömlöst överföra dina filmfotograferingsdata mellan iPhone och Mac med hjälp av .frames-filexporter. Exportera helt enkelt dina rullar från en enhet och importera dem på en annan. Även om automatisk molnsynkronisering inte är tillgänglig för närvarande för att behålla din integritet och dataäganderätt, gör .frames-formatet manuell synkronisering snabb och enkel. Framtida uppdateringar kan inkludera valfri iCloud-synkronisering för Pro-användare."
    },
    "th": {
        "question": "ฉันสามารถซิงค์ข้อมูลระหว่าง iPhone และ Mac ได้หรือไม่?",
        "answer": "ได้ คุณสามารถถ่ายโอนข้อมูลการถ่ายภาพฟิล์มของคุณระหว่าง iPhone และ Mac ได้อย่างราบรื่นโดยใช้การส่งออกไฟล์ .frames เพียงส่งออกฟิล์มของคุณจากอุปกรณ์หนึ่งและนำเข้าไปยังอีกอุปกรณ์หนึ่ง แม้ว่าการซิงค์คลาวด์อัตโนมัติจะยังไม่มีในขณะนี้เพื่อรักษาความเป็นส่วนตัวและความเป็นเจ้าของข้อมูลของคุณ แต่รูปแบบ .frames ทำให้การซิงค์ด้วยตนเองเป็นเรื่องที่รวดเร็วและตรงไปตรงมา การอัปเดตในอนาคตอาจรวมถึงการซิงค์ iCloud แบบเลือกได้สำหรับผู้ใช้ Pro"
    },
    "zh-hant": {
        "question": "我可以在 iPhone 和 Mac 之間同步資料嗎？",
        "answer": "可以，您可以使用 .frames 檔案匯出功能在 iPhone 和 Mac 之間無縫傳輸底片攝影資料。只需從一台裝置匯出您的底片並在另一台裝置上匯入即可。雖然為了保護您的隱私和資料所有權，目前還沒有自動雲端同步功能，但 .frames 格式使手動同步變得快速而簡單。未來的更新可能會為 Pro 使用者提供可選的 iCloud 同步功能。"
    },
    "tr": {
        "question": "Verilerimi iPhone ve Mac arasında senkronize edebilir miyim?",
        "answer": "Evet, .frames dosya dışa aktarımlarını kullanarak film fotoğrafçılığı verilerinizi iPhone ve Mac arasında sorunsuz bir şekilde aktarabilirsiniz. Bir cihazdan rulolarınızı dışa aktarın ve diğerine içe aktarın. Gizliliğinizi ve veri sahipliğinizi korumak için otomatik bulut senkronizasyonu şu anda mevcut olmasa da, .frames formatı manuel senkronizasyonu hızlı ve basit hale getirir. Gelecek güncellemeler Pro kullanıcılar için isteğe bağlı iCloud senkronizasyonu içerebilir."
    },
    "uk": {
        "question": "Чи можу я синхронізувати свої дані між iPhone та Mac?",
        "answer": "Так, ви можете легко переносити дані плівкової фотографії між iPhone та Mac, використовуючи експорт файлів .frames. Просто експортуйте свої плівки з одного пристрою та імпортуйте їх на інший. Хоча автоматична хмарна синхронізація наразі недоступна для збереження вашої конфіденційності та володіння даними, формат .frames робить ручну синхронізацію швидкою та простою. Майбутні оновлення можуть включати опціональну синхронізацію iCloud для користувачів Pro."
    },
    "vi": {
        "question": "Tôi có thể đồng bộ dữ liệu giữa iPhone và Mac không?",
        "answer": "Có, bạn có thể chuyển dữ liệu nhiếp ảnh phim của mình một cách liền mạch giữa iPhone và Mac bằng cách sử dụng xuất tệp .frames. Chỉ cần xuất các cuộn phim của bạn từ một thiết bị và nhập chúng vào thiết bị khác. Mặc dù đồng bộ hóa đám mây tự động hiện không khả dụng để duy trì quyền riêng tư và quyền sở hữu dữ liệu của bạn, định dạng .frames giúp đồng bộ hóa thủ công nhanh chóng và đơn giản. Các bản cập nhật trong tương lai có thể bao gồm đồng bộ hóa iCloud tùy chọn cho người dùng Pro."
    },
    "en": {
        "question": "Can I sync my data between iPhone and Mac?",
        "answer": "Yes, you can seamlessly transfer your film photography data between iPhone and Mac using .frames file exports. Simply export your rolls from one device and import them on another. While automatic cloud sync isn't currently available to maintain your privacy and data ownership, the .frames format makes manual syncing quick and straightforward. Future updates may include optional iCloud sync for Pro users."
    }
}


def add_question7_to_file(file_path, lang_code, dry_run=False):
    """Add question7 to a locale JSON file."""

    if lang_code not in TRANSLATIONS:
        print(f"❌ No translation found for {lang_code}")
        return False

    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Check if question7 already exists
        if 'qa' in data and 'question7' in data['qa']:
            print(f"⚠️  {lang_code}: question7 already exists, skipping")
            return True

        # Add question7
        if 'qa' not in data:
            print(f"❌ {lang_code}: 'qa' section not found")
            return False

        data['qa']['question7'] = TRANSLATIONS[lang_code]

        if dry_run:
            print(f"✓ {lang_code}: Would add question7 (dry run)")
            return True

        # Write back with proper formatting
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')  # Add trailing newline

        print(f"✓ {lang_code}: Added question7")
        return True

    except Exception as e:
        print(f"❌ {lang_code}: Error - {e}")
        return False


def main():
    """Main function to process all locale files."""
    locales_dir = Path(__file__).parent / "sources" / "locales"

    if not locales_dir.exists():
        print(f"❌ Locales directory not found: {locales_dir}")
        sys.exit(1)

    # Test mode or full run
    test_mode = "--test" in sys.argv
    dry_run = "--dry-run" in sys.argv

    if test_mode:
        print("🧪 TEST MODE: Processing French only\n")
        fr_file = locales_dir / "fr.json"
        success = add_question7_to_file(fr_file, "fr", dry_run=dry_run)
        sys.exit(0 if success else 1)

    # Process all files
    print("🚀 Processing all locale files...\n")

    results = {"success": 0, "failed": 0, "skipped": 0}

    for json_file in sorted(locales_dir.glob("*.json")):
        if json_file.name == "global.json":
            continue

        lang_code = json_file.stem
        result = add_question7_to_file(json_file, lang_code, dry_run=dry_run)

        if result:
            results["success"] += 1
        else:
            results["failed"] += 1

    print(f"\n📊 Summary:")
    print(f"   ✓ Success: {results['success']}")
    print(f"   ✗ Failed: {results['failed']}")

    sys.exit(0 if results["failed"] == 0 else 1)


if __name__ == "__main__":
    main()
