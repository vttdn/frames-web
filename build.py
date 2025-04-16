import os, json
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
TEMPLATES_DIR = ROOT / "templates"
LOCALES_DIR = ROOT / "locales"

def render_template(template: str, context: dict) -> str:
    result = template
    for key, value in context.items():
        if isinstance(value, dict):
            for subkey, subval in value.items():
                result = result.replace(f"{{{{ {key}.{subkey} }}}}", subval)
        else:
            result = result.replace(f"{{{{ {key} }}}}", value)
    return result

def build():
    for locale_file in LOCALES_DIR.glob("*.json"):
        lang = locale_file.stem
        with open(locale_file, "r", encoding="utf-8") as f:
            context = json.load(f)

        # Output path for home: root or /lang
        home_path = ROOT if lang == "en" else ROOT / lang
        home_path.mkdir(parents=True, exist_ok=True)

        # Render home
        with open(TEMPLATES_DIR / "home.html", "r", encoding="utf-8") as f:
            home_template = f.read()
        rendered_home = render_template(home_template, context)
        with open(home_path / "index.html", "w", encoding="utf-8") as out_file:
            out_file.write(rendered_home)

        # Render privacy at custom path
        privacy_path = context.get("privacy_path", "privacy")
        full_privacy_path = ROOT / (privacy_path if lang == "en" else f"{lang}/{privacy_path}")
        full_privacy_path.mkdir(parents=True, exist_ok=True)

        with open(TEMPLATES_DIR / "privacy.html", "r", encoding="utf-8") as f:
            privacy_template = f.read()
        rendered_privacy = render_template(privacy_template, context)
        with open(full_privacy_path / "index.html", "w", encoding="utf-8") as out_file:
            out_file.write(rendered_privacy)

        print(f"✅ Built: {lang} → /{'' if lang == 'en' else lang + '/'}index.html and /{privacy_path}/index.html")

if __name__ == "__main__":
    build()
