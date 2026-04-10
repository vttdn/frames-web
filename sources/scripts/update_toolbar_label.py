#!/usr/bin/env python3
"""
Update newhome.section3.highlight1.title from "Control bar" to "Toolbar"
in en.json and all other locales.
"""

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
LOCALES_DIR = PROJECT_ROOT / "sources" / "locales"

KEY_PATH = ["newhome", "section3", "highlight1", "title"]

TRANSLATIONS = {
    "en":      "Toolbar",
    "da":      "Værktøjslinje",
    "de":      "Symbolleiste",
    "el":      "Γραμμή εργαλείων",
    "es":      "Barra de herramientas",
    "fi":      "Työkalupalkki",
    "fr":      "Barre d'outils",
    "hi":      "टूलबार",
    "id":      "Bilah alat",
    "it":      "Barra degli strumenti",
    "ja":      "ツールバー",
    "ko":      "툴바",
    "nb":      "Verktøylinje",
    "nl":      "Werkbalk",
    "pl":      "Pasek narzędzi",
    "pt":      "Barra de ferramentas",
    "ro":      "Bara de instrumente",
    "ru":      "Панель инструментов",
    "sv":      "Verktygsfält",
    "th":      "แถบเครื่องมือ",
    "tr":      "Araç çubuğu",
    "uk":      "Панель інструментів",
    "vi":      "Thanh công cụ",
    "zh-hant": "工具列",
    "zh":      "工具栏",
}


def get_nested(data: dict, path: list):
    for key in path:
        data = data[key]
    return data


def set_nested(data: dict, path: list, value: str):
    for key in path[:-1]:
        data = data[key]
    data[path[-1]] = value


def main():
    errors = []

    for code, new_value in TRANSLATIONS.items():
        path = LOCALES_DIR / f"{code}.json"
        if not path.exists():
            print(f"{code}: file not found, skipping")
            errors.append(code)
            continue

        data = json.loads(path.read_text(encoding="utf-8"))
        old_value = get_nested(data, KEY_PATH)
        set_nested(data, KEY_PATH, new_value)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{code}: '{old_value}' → '{new_value}'")

    if errors:
        print(f"\nFailed: {errors}")
        sys.exit(1)
    else:
        print("\nAll locales updated successfully.")


if __name__ == "__main__":
    main()
