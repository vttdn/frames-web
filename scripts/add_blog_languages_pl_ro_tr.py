#!/usr/bin/env python3
"""
Script to add blog configuration for Polish, Romanian, and Turkish languages.
Updates:
1. Individual locale JSON files with blog sections
2. blog.conf with language entries and category translations
3. Creates blog directories for each language
"""

import json
import os
from pathlib import Path

BASE_DIR = Path("/Users/vnn/Documents/Dev/framesWeb/sources/locales")
BLOG_DIR = BASE_DIR / "blog"
BLOG_CONF_PATH = BLOG_DIR / "blog.conf"

# Blog section translations for each language (to add to locale JSON files)
# Meta title max 60 chars, meta description max 160 chars
BLOG_SECTIONS = {
    "pl": {
        "blog": {
            "meta": {
                "title": "Blog - Frames",
                "description": "Odkryj przewodniki po fotografii analogowej, porady dotyczace zdjec, recenzje aparatow i praktyczne sposoby korzystania z aplikacji Frames.",
                "canonical_url": "https://withframes.com/pl/blog/"
            },
            "heading": "Blog",
            "labels": {
                "by_author": "przez",
                "published_on": "Opublikowano",
                "category": "Kategoria",
                "all_posts": "Wszystkie artykuly",
                "in_category": "w",
                "previous": "Poprzedni",
                "next": "Nastepny",
                "contents": "Spis tresci",
                "filed_under": "Kategoria",
                "author": "Autor",
                "updated": "Aktualizacja"
            },
            "pagination": {
                "previous": "Poprzedni",
                "next": "Nastepny",
                "page": "Strona",
                "page_suffix": "",
                "newer_posts": "Nowsze artykuly",
                "older_posts": "Starsze artykuly"
            }
        }
    },
    "ro": {
        "blog": {
            "meta": {
                "title": "Blog - Frames",
                "description": "Descopera ghiduri de fotografie pe film, sfaturi de fotografiere, recenzii de camere si moduri practice de a folosi aplicatia Frames.",
                "canonical_url": "https://withframes.com/ro/blog/"
            },
            "heading": "Blog",
            "labels": {
                "by_author": "de",
                "published_on": "Publicat pe",
                "category": "Categorie",
                "all_posts": "Toate articolele",
                "in_category": "in",
                "previous": "Anterior",
                "next": "Urmator",
                "contents": "Cuprins",
                "filed_under": "Categorie",
                "author": "Autor",
                "updated": "Actualizat"
            },
            "pagination": {
                "previous": "Anterior",
                "next": "Urmator",
                "page": "Pagina",
                "page_suffix": "",
                "newer_posts": "Articole mai noi",
                "older_posts": "Articole mai vechi"
            }
        }
    },
    "tr": {
        "blog": {
            "meta": {
                "title": "Blog - Frames",
                "description": "Film fotografi rehberleri, cekim ipuclari, kamera incelemeleri ve Frames uygulamasini kullanmanin pratik yollarini kesfedin.",
                "canonical_url": "https://withframes.com/tr/blog/"
            },
            "heading": "Blog",
            "labels": {
                "by_author": "yazan",
                "published_on": "Yayinlanma",
                "category": "Kategori",
                "all_posts": "Tum yazilar",
                "in_category": "kategorisinde",
                "previous": "Onceki",
                "next": "Sonraki",
                "contents": "Icindekiler",
                "filed_under": "Kategori",
                "author": "Yazar",
                "updated": "Guncelleme"
            },
            "pagination": {
                "previous": "Onceki",
                "next": "Sonraki",
                "page": "Sayfa",
                "page_suffix": "",
                "newer_posts": "Daha yeni yazilar",
                "older_posts": "Daha eski yazilar"
            }
        }
    }
}

# Blog.conf language entries (meta title max 60 chars, meta description max 160 chars)
BLOG_CONF_LANGUAGES = {
    "pl": {
        "meta": {
            "title": "Wiadomosci o fotografii analogowej - Blog Frames",
            "description": "Artykuly, porady i informacje o fotografii analogowej i aplikacji Frames.",
            "keywords": "fotografia analogowa, fotografia filmowa, blog, porady, przewodniki, aplikacja Frames"
        },
        "heading": "Blog",
        "labels": {
            "by_author": "przez",
            "published_on": "Opublikowano",
            "category": "Kategoria",
            "all_posts": "Wszystkie artykuly",
            "in_category": "w"
        }
    },
    "ro": {
        "meta": {
            "title": "Stiri fotografie pe film - Blog Frames",
            "description": "Articole, sfaturi si informatii despre fotografia pe film si aplicatia Frames.",
            "keywords": "fotografie pe film, fotografie analogica, blog, sfaturi, ghiduri, aplicatia Frames"
        },
        "heading": "Blog",
        "labels": {
            "by_author": "de",
            "published_on": "Publicat pe",
            "category": "Categorie",
            "all_posts": "Toate articolele",
            "in_category": "in"
        }
    },
    "tr": {
        "meta": {
            "title": "Film Fotografi Haberleri - Frames Blog",
            "description": "Film fotografi ve Frames uygulamasi hakkinda makaleler, ipuclari ve bilgiler.",
            "keywords": "film fotografi, analog fotograf, blog, ipuclari, rehberler, Frames uygulamasi"
        },
        "heading": "Blog",
        "labels": {
            "by_author": "yazan",
            "published_on": "Yayinlanma",
            "category": "Kategori",
            "all_posts": "Tum yazilar",
            "in_category": "kategorisinde"
        }
    }
}

# Blog.conf category (gear) translations (meta title max 60 chars, meta description max 160 chars)
BLOG_CONF_CATEGORIES = {
    "pl": {
        "slug": "sprzet",
        "name": "Sprzet",
        "meta_title": "Sprzet do fotografii analogowej | Blog Frames",
        "meta_description": "Nowe aparaty, filmy, obiektywy i akcesoria dla fotografow analogowych. Recenzje i poradniki zakupowe."
    },
    "ro": {
        "slug": "echipament",
        "name": "Echipament",
        "meta_title": "Echipament fotografie pe film | Blog Frames",
        "meta_description": "Camere noi, filme, obiective si accesorii pentru fotografi analogici. Recenzii si ghiduri de cumparare."
    },
    "tr": {
        "slug": "ekipman",
        "name": "Ekipman",
        "meta_title": "Film Fotografi Ekipmani | Frames Blog",
        "meta_description": "Analog fotografcilar icin yeni kameralar, filmler, lensler ve aksesuarlar. Incelemeler ve satin alma rehberleri."
    }
}


def update_locale_json(lang_code: str, blog_section: dict) -> bool:
    """Add blog section to a locale JSON file."""
    file_path = BASE_DIR / f"{lang_code}.json"

    if not file_path.exists():
        print(f"  Warning: {file_path} does not exist, skipping.")
        return False

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Check if blog section already exists with full structure
        if "blog" in data and "meta" in data.get("blog", {}):
            print(f"  Blog section already exists in {lang_code}.json, skipping.")
            return True

        # Add blog section
        data["blog"] = blog_section["blog"]

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"  Added blog section to {lang_code}.json")
        return True

    except Exception as e:
        print(f"  Error updating {lang_code}.json: {e}")
        return False


def update_blog_conf() -> bool:
    """Update blog.conf with new language entries."""
    try:
        with open(BLOG_CONF_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Add language entries
        for lang_code, lang_data in BLOG_CONF_LANGUAGES.items():
            if lang_code not in data["languages"]:
                data["languages"][lang_code] = lang_data
                print(f"  Added {lang_code} to blog.conf languages")
            else:
                print(f"  {lang_code} already exists in blog.conf languages, skipping.")

        # Add category entries for gear
        for lang_code, cat_data in BLOG_CONF_CATEGORIES.items():
            if lang_code not in data["categories"]["gear"]:
                data["categories"]["gear"][lang_code] = cat_data
                print(f"  Added {lang_code} to blog.conf categories.gear")
            else:
                print(f"  {lang_code} already exists in blog.conf categories.gear, skipping.")

        with open(BLOG_CONF_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print("  blog.conf updated successfully")
        return True

    except Exception as e:
        print(f"  Error updating blog.conf: {e}")
        return False


def create_blog_directories() -> bool:
    """Create blog directories for each language."""
    languages = ["pl", "ro", "tr"]

    for lang in languages:
        dir_path = BLOG_DIR / lang
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"  Created directory: {dir_path}")
        else:
            print(f"  Directory already exists: {dir_path}")

    return True


def main():
    print("=" * 60)
    print("Adding blog configuration for Polish, Romanian,")
    print("and Turkish languages")
    print("=" * 60)

    print("\n1. Updating locale JSON files with blog sections...")
    for lang_code, blog_section in BLOG_SECTIONS.items():
        update_locale_json(lang_code, blog_section)

    print("\n2. Updating blog.conf...")
    update_blog_conf()

    print("\n3. Creating blog directories...")
    create_blog_directories()

    print("\n" + "=" * 60)
    print("Configuration complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("- Create translated article files in each blog directory")
    print("- Article filename: 2025-11-11-buy-new-film-cameras-2025.json")
    print("=" * 60)


if __name__ == "__main__":
    main()
