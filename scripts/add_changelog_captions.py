#!/usr/bin/env python3
"""
Walks every changelog JSON under sources/locales/changelog/{lang}/ and adds a
localized "caption" to any media section that does not already have one.

Caption format: "Frames {platform_label} {version_short} update", localized
per language. "Frames", "macOS", and "iOS" stay literal — only the "update"
word and word order vary.
"""

import json
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent / "sources" / "locales" / "changelog"

CAPTION_TEMPLATES: dict[str, str] = {
    "da": "Frames {platform_label} {version_short}-opdatering",
    "de": "Frames {platform_label} {version_short} Update",
    "el": "Ενημέρωση Frames {platform_label} {version_short}",
    "en": "Frames {platform_label} {version_short} update",
    "es": "Actualización de Frames {platform_label} {version_short}",
    "fi": "Frames {platform_label} {version_short} -päivitys",
    "fr": "Mise à jour Frames {platform_label} {version_short}",
    "hi": "Frames {platform_label} {version_short} अपडेट",
    "id": "Pembaruan Frames {platform_label} {version_short}",
    "it": "Aggiornamento Frames {platform_label} {version_short}",
    "ja": "Frames {platform_label} {version_short} アップデート",
    "ko": "Frames {platform_label} {version_short} 업데이트",
    "nb": "Frames {platform_label} {version_short}-oppdatering",
    "nl": "Frames {platform_label} {version_short}-update",
    "pl": "Aktualizacja Frames {platform_label} {version_short}",
    "pt": "Atualização do Frames {platform_label} {version_short}",
    "ro": "Actualizare Frames {platform_label} {version_short}",
    "ru": "Обновление Frames {platform_label} {version_short}",
    "sv": "Frames {platform_label} {version_short}-uppdatering",
    "th": "อัปเดต Frames {platform_label} {version_short}",
    "tr": "Frames {platform_label} {version_short} güncellemesi",
    "uk": "Оновлення Frames {platform_label} {version_short}",
    "vi": "Bản cập nhật Frames {platform_label} {version_short}",
    "zh": "Frames {platform_label} {version_short} 更新",
    "zh-hant": "Frames {platform_label} {version_short} 更新",
}


def process_file(filepath: Path, template: str) -> tuple[int, bool]:
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    platform = data.get("platform")
    version_short = data.get("version_short")
    if platform is None or version_short is None:
        print(f"  skipped {filepath.name} — missing platform or version_short")
        return (0, False)

    platform_label = "macOS" if platform == "macos" else "iOS"
    caption = template.format(platform_label=platform_label, version_short=version_short)

    added = 0
    for section in data.get("sections", []):
        if section.get("type") == "media" and "caption" not in section:
            section["caption"] = caption
            added += 1

    if added == 0:
        return (0, False)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    return (added, True)


def main() -> None:
    total_files = 0
    total_captions = 0

    for lang, template in CAPTION_TEMPLATES.items():
        lang_dir = BASE_PATH / lang
        if not lang_dir.is_dir():
            print(f"[{lang}] directory not found, skipping")
            continue

        for filepath in sorted(lang_dir.glob("*.json")):
            added, modified = process_file(filepath, template)
            if modified:
                print(f"[{lang}] {filepath.name} — added {added} caption(s)")
                total_files += 1
                total_captions += added
            else:
                print(f"[{lang}] {filepath.name} — skipped (no media without caption)")

    print(f"\nDone. Modified {total_files} files, added {total_captions} captions.")


if __name__ == "__main__":
    main()
