import os, json
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
TEMPLATES_DIR = ROOT / "library" / "templates"
LOCALES_DIR = ROOT / "library" / "locales"

def render_template(template: str, context: dict) -> str:
    result = template

    # Simple foreach loop rendering: {{ for item in list }} ... {{ endfor }}
    import re
    for_loop_pattern = re.compile(r"{{ for (\w+) in (\w+) }}(.*?){{ endfor }}", re.DOTALL)

    def render_loop(match):
        item_name = match.group(1)
        list_name = match.group(2)
        block = match.group(3)

        rendered = ""
        for item in context.get(list_name, []):
            temp_block = block
            for key, value in item.items():
                temp_block = temp_block.replace(f"{{{{ {item_name}.{key} }}}}", str(value))
            rendered += temp_block
        return rendered

    result = for_loop_pattern.sub(render_loop, result)

    # Simple {{ key }} and {{ key.subkey }} replacements
    for key, value in context.items():
        if isinstance(value, dict):
            for subkey, subval in value.items():
                result = result.replace(f"{{{{ {key}.{subkey} }}}}", str(subval))
        else:
            result = result.replace(f"{{{{ {key} }}}}", str(value))
    return result

def build():
    for locale_file in LOCALES_DIR.glob("*.json"):
        lang = locale_file.stem
        with open(locale_file, "r", encoding="utf-8") as f:
            context = json.load(f)

        # Generate review_microdata if reviews are present
        if "reviews" in context:
            context["review_microdata"] = json.dumps([
                {
                    "@type": "Review",
                    **({"name": r["title"]} if "title" in r else {}),
                    "reviewBody": r["body"],
                    "datePublished": r["date"],
                    "reviewRating": {
                        "@type": "Rating",
                        "ratingValue": r["rating"]
                    },
                    "author": {
                        "@type": "Person",
                        "name": r["author"]
                    }
                } for r in context["reviews"]
            ], ensure_ascii=False, indent=2)
        else:
            context["review_microdata"] = "[]"

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

        # Render JSON templates like faq.json and frames.json
        for json_template_name in ["faq.json", "frames.json"]:
            json_template_path = TEMPLATES_DIR / json_template_name
            if not json_template_path.exists():
                continue

            with open(json_template_path, "r", encoding="utf-8") as f:
                json_template = f.read()

            rendered_json = render_template(json_template, context)

            # Remove <br> tags for JSON output
            rendered_json = rendered_json.replace("<br>", "")

            # Determine output file name and path
            base_name = json_template_name.replace(".json", "")
            output_dir = ROOT / "library" / "data"
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = output_dir / f"{base_name}-{lang}.json"

            with open(output_file, "w", encoding="utf-8") as out_file:
                out_file.write(rendered_json)

            print(f"📦 Built: {lang} → /library/data/{base_name}-{lang}.json")

if __name__ == "__main__":
    build()
