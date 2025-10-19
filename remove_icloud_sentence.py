#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to remove the last sentence about iCloud sync from question7 answers.
"""

import json
import sys
from pathlib import Path

# Sentence patterns to remove (last sentence in various languages)
SENTENCES_TO_REMOVE = [
    "Future updates may include optional iCloud sync for Pro users.",
    "Fremtidige opdateringer kan inkludere valgfri iCloud-synkronisering for Pro-brugere.",
    "Toekomstige updates kunnen optionele iCloud-synchronisatie voor Pro-gebruikers bevatten.",
    "Tulevat päivitykset voivat sisältää valinnaisen iCloud-synkronoinnin Pro-käyttäjille.",
    "Les futures mises à jour pourront inclure une synchronisation iCloud optionnelle pour les utilisateurs Pro.",
    "Zukünftige Updates könnten eine optionale iCloud-Synchronisierung für Pro-Benutzer enthalten.",
    "Μελλοντικές ενημερώσεις μπορεί να περιλαμβάνουν προαιρετικό συγχρονισμό iCloud για χρήστες Pro.",
    "भविष्य के अपडेट में Pro उपयोगकर्ताओं के लिए वैकल्पिक iCloud सिंक शामिल हो सकता है।",
    "Pembaruan di masa mendatang mungkin menyertakan sinkronisasi iCloud opsional untuk pengguna Pro.",
    "Gli aggiornamenti futuri potrebbero includere la sincronizzazione iCloud opzionale per gli utenti Pro.",
    "将来のアップデートでは、Proユーザー向けにオプションのiCloud同期が含まれる可能性があります。",
    "향후 업데이트에는 Pro 사용자를 위한 선택적 iCloud 동기화가 포함될 수 있습니다.",
    "Fremtidige oppdateringer kan inkludere valgfri iCloud-synkronisering for Pro-brukere.",
    "Przyszłe aktualizacje mogą obejmować opcjonalną synchronizację iCloud dla użytkowników Pro.",
    "Atualizações futuras podem incluir sincronização iCloud opcional para usuários Pro.",
    "Actualizările viitoare ar putea include sincronizare iCloud opțională pentru utilizatorii Pro.",
    "Будущие обновления могут включать опциональную синхронизацию iCloud для пользователей Pro.",
    "未来的更新可能会为 Pro 用户提供可选的 iCloud 同步功能。",
    "Las actualizaciones futuras pueden incluir sincronización iCloud opcional para usuarios Pro.",
    "Framtida uppdateringar kan inkludera valfri iCloud-synkronisering för Pro-användare.",
    "การอัปเดตในอนาคตอาจรวมถึงการซิงค์ iCloud แบบเลือกได้สำหรับผู้ใช้ Pro",
    "未來的更新可能會為 Pro 使用者提供可選的 iCloud 同步功能。",
    "Gelecek güncellemeler Pro kullanıcılar için isteğe bağlı iCloud senkronizasyonu içerebilir.",
    "Майбутні оновлення можуть включати опціональну синхронізацію iCloud для користувачів Pro.",
    "Các bản cập nhật trong tương lai có thể bao gồm đồng bộ hóa iCloud tùy chọn cho người dùng Pro."
]


def remove_icloud_sentence(file_path, lang_code, dry_run=False):
    """Remove the iCloud sentence from question7 answer."""
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Check if question7 exists
        if 'qa' not in data or 'question7' not in data['qa']:
            print(f"⚠️  {lang_code}: question7 not found, skipping")
            return True

        original_answer = data['qa']['question7']['answer']
        modified_answer = original_answer

        # Try to remove the sentence
        found = False
        for sentence in SENTENCES_TO_REMOVE:
            if sentence in modified_answer:
                # Remove the sentence and any extra space before it
                modified_answer = modified_answer.replace(' ' + sentence, '').replace(sentence, '')
                found = True
                break

        if not found:
            print(f"⚠️  {lang_code}: iCloud sentence not found (may already be removed)")
            return True

        if modified_answer == original_answer:
            print(f"⚠️  {lang_code}: No change made")
            return True

        if dry_run:
            print(f"✓ {lang_code}: Would remove iCloud sentence (dry run)")
            return True

        # Update the answer
        data['qa']['question7']['answer'] = modified_answer

        # Write back with proper formatting
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')

        print(f"✓ {lang_code}: Removed iCloud sentence")
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

    dry_run = "--dry-run" in sys.argv

    print("🚀 Removing iCloud sentence from all locale files...\n")

    results = {"success": 0, "failed": 0}

    for json_file in sorted(locales_dir.glob("*.json")):
        if json_file.name == "global.json":
            continue

        lang_code = json_file.stem
        result = remove_icloud_sentence(json_file, lang_code, dry_run=dry_run)

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
