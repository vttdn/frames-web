#!/usr/bin/env python3
"""
Translate the newhome section from en.json to all other language files.
"""

import json
import re
import sys
from pathlib import Path

import anthropic

PROJECT_ROOT = Path(__file__).parent.parent.parent
LOCALES_DIR = PROJECT_ROOT / "sources" / "locales"

LANGS = {
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "es": "Spanish",
    "fi": "Finnish",
    "fr": "French",
    "hi": "Hindi",
    "id": "Indonesian",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "nb": "Norwegian Bokmål",
    "nl": "Dutch",
    "pl": "Polish",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "sv": "Swedish",
    "th": "Thai",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "vi": "Vietnamese",
    "zh-hant": "Traditional Chinese",
    "zh": "Simplified Chinese",
}

PROMPT_TEMPLATE = """You are a professional translator and marketing copywriter specializing in consumer tech and analog photography products. You have deep familiarity with film photography terminology across languages.

Translate the following JSON from English into {language}. The text is marketing copy for Frames, an iOS and macOS app that helps film photographers log their rolls, record shooting data, and embed metadata into their scans.

Rules:
- Do not translate literally. Adapt copy to read naturally and fluently, preserving length, tone, and intent.
- Tone is calm, minimal, and editorial — not corporate or overly enthusiastic.
- Sentence case for all titles: only capitalize the first word, unless it is a proper noun or acronym (EXIF, iOS, macOS).
- No em dashes. Use commas, periods, or short sentences instead.
- "recorder" refers to a data-logging interface inside the app where photographers input shooting settings frame by frame. It is not an audio or video recorder. Choose a word in your language that conveys logging, noting, or capturing data, not sound or video recording. The same applies to the verb "record" throughout: it always means to log or note down information, never to record audio or video.
- Keep untranslated: EXIF, XMP, CSV, TXT, GPS, iOS, macOS, Apple Photos, Adobe Lightroom, Google Photos, Capture One, Darkroom, Frames.
- Film photography terms (roll, frame, film stock, exposure, aperture, shutter speed) should use the most natural and established equivalent in your language, as used by film photography communities.
- Return only valid JSON with identical structure and keys. No explanations, no markdown code fences.

JSON to translate:
{newhome_json}"""


def extract_json(text: str) -> str:
    """Strip markdown fences if the model returns them."""
    text = text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]+?)\s*```", text)
    if match:
        return match.group(1).strip()
    return text


def translate(client: anthropic.Anthropic, language: str, newhome_json: str) -> dict:
    prompt = PROMPT_TEMPLATE.format(language=language, newhome_json=newhome_json)
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8192,
        messages=[{"role": "user", "content": prompt}],
    )
    raw = message.content[0].text
    cleaned = extract_json(raw)
    return json.loads(cleaned)


def main():
    client = anthropic.Anthropic()

    en_path = LOCALES_DIR / "en.json"
    en_data = json.loads(en_path.read_text(encoding="utf-8"))
    newhome_en = en_data["newhome"]
    newhome_json = json.dumps(newhome_en, ensure_ascii=False, indent=2)

    errors = []

    for code, language in LANGS.items():
        path = LOCALES_DIR / f"{code}.json"
        if not path.exists():
            print(f"{code}: file not found, skipping")
            continue

        data = json.loads(path.read_text(encoding="utf-8"))

        if "newhome" in data:
            print(f"{code}: already has newhome, skipping")
            continue

        print(f"{code} ({language}): translating...", end=" ", flush=True)
        try:
            translated = translate(client, language, newhome_json)
            data["newhome"] = translated
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print("done")
        except json.JSONDecodeError as e:
            print(f"JSON parse error: {e}")
            errors.append(code)
        except Exception as e:
            print(f"error: {e}")
            errors.append(code)

    if errors:
        print(f"\nFailed languages: {errors}")
        sys.exit(1)
    else:
        print("\nAll languages translated successfully.")


if __name__ == "__main__":
    main()
