#!/usr/bin/env python3
"""
Script to add blog configuration for Hindi, Traditional Chinese, Thai, and Greek languages.
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
    "hi": {
        "blog": {
            "meta": {
                "title": "ब्लॉग - Frames",
                "description": "फिल्म फोटोग्राफी गाइड, शूटिंग टिप्स, कैमरा रिव्यू, एनालॉग वर्कफ्लो सलाह और Frames ऐप का उपयोग करने के तरीके खोजें।",
                "canonical_url": "https://withframes.com/hi/blog/"
            },
            "heading": "ब्लॉग",
            "labels": {
                "by_author": "द्वारा",
                "published_on": "प्रकाशित",
                "category": "श्रेणी",
                "all_posts": "सभी लेख",
                "in_category": "में",
                "previous": "पिछला",
                "next": "अगला",
                "contents": "विषय-सूची",
                "filed_under": "श्रेणी",
                "author": "लेखक",
                "updated": "अपडेट"
            },
            "pagination": {
                "previous": "पिछला",
                "next": "अगला",
                "page": "पृष्ठ",
                "page_suffix": "",
                "newer_posts": "नए लेख",
                "older_posts": "पुराने लेख"
            }
        }
    },
    "zh-hant": {
        "blog": {
            "meta": {
                "title": "部落格 - Frames",
                "description": "探索底片攝影指南、拍攝技巧、相機評測、類比工作流程建議，以及如何有效使用 Frames 應用程式。",
                "canonical_url": "https://withframes.com/zh-hant/blog/"
            },
            "heading": "部落格",
            "labels": {
                "by_author": "作者",
                "published_on": "發布於",
                "category": "分類",
                "all_posts": "所有文章",
                "in_category": "分類於",
                "previous": "上一篇",
                "next": "下一篇",
                "contents": "目錄",
                "filed_under": "分類",
                "author": "作者",
                "updated": "更新"
            },
            "pagination": {
                "previous": "上一頁",
                "next": "下一頁",
                "page": "第",
                "page_suffix": "頁",
                "newer_posts": "較新文章",
                "older_posts": "較舊文章"
            }
        }
    },
    "th": {
        "blog": {
            "meta": {
                "title": "บล็อก - Frames",
                "description": "ค้นพบคู่มือการถ่ายภาพฟิล์ม เคล็ดลับการถ่ายภาพ รีวิวกล้อง คำแนะนำเวิร์กโฟลว์อนาล็อก และวิธีใช้แอป Frames",
                "canonical_url": "https://withframes.com/th/blog/"
            },
            "heading": "บล็อก",
            "labels": {
                "by_author": "โดย",
                "published_on": "เผยแพร่เมื่อ",
                "category": "หมวดหมู่",
                "all_posts": "บทความทั้งหมด",
                "in_category": "ใน",
                "previous": "ก่อนหน้า",
                "next": "ถัดไป",
                "contents": "สารบัญ",
                "filed_under": "หมวดหมู่",
                "author": "ผู้เขียน",
                "updated": "อัปเดต"
            },
            "pagination": {
                "previous": "ก่อนหน้า",
                "next": "ถัดไป",
                "page": "หน้า",
                "page_suffix": "",
                "newer_posts": "บทความใหม่กว่า",
                "older_posts": "บทความเก่ากว่า"
            }
        }
    },
    "el": {
        "blog": {
            "meta": {
                "title": "Blog - Frames",
                "description": "Ανακαλύψτε οδηγούς φωτογραφίας φιλμ, συμβουλές λήψης, κριτικές καμερών και πρακτικούς τρόπους χρήσης του Frames.",
                "canonical_url": "https://withframes.com/el/blog/"
            },
            "heading": "Blog",
            "labels": {
                "by_author": "από",
                "published_on": "Δημοσιεύτηκε",
                "category": "Κατηγορία",
                "all_posts": "Όλα τα άρθρα",
                "in_category": "στην",
                "previous": "Προηγούμενο",
                "next": "Επόμενο",
                "contents": "Περιεχόμενα",
                "filed_under": "Κατηγορία",
                "author": "Συγγραφέας",
                "updated": "Ενημέρωση"
            },
            "pagination": {
                "previous": "Προηγούμενο",
                "next": "Επόμενο",
                "page": "Σελίδα",
                "page_suffix": "",
                "newer_posts": "Νεότερα άρθρα",
                "older_posts": "Παλαιότερα άρθρα"
            }
        }
    }
}

# Blog.conf language entries (meta title max 60 chars, meta description max 160 chars)
BLOG_CONF_LANGUAGES = {
    "hi": {
        "meta": {
            "title": "फिल्म फोटोग्राफी समाचार - Frames ब्लॉग",
            "description": "फिल्म फोटोग्राफी और Frames ऐप के बारे में लेख, टिप्स और जानकारी।",
            "keywords": "फिल्म फोटोग्राफी, एनालॉग फोटोग्राफी, ब्लॉग, टिप्स, गाइड, Frames ऐप"
        },
        "heading": "ब्लॉग",
        "labels": {
            "by_author": "द्वारा",
            "published_on": "प्रकाशित",
            "category": "श्रेणी",
            "all_posts": "सभी लेख",
            "in_category": "में"
        }
    },
    "zh-hant": {
        "meta": {
            "title": "底片攝影新聞 - Frames 部落格",
            "description": "關於底片攝影和 Frames 應用程式的文章、技巧和見解。",
            "keywords": "底片攝影, 類比攝影, 部落格, 技巧, 指南, Frames 應用程式"
        },
        "heading": "部落格",
        "labels": {
            "by_author": "作者",
            "published_on": "發布於",
            "category": "分類",
            "all_posts": "所有文章",
            "in_category": "分類於"
        }
    },
    "th": {
        "meta": {
            "title": "ข่าวการถ่ายภาพฟิล์ม - Frames Blog",
            "description": "บทความ เคล็ดลับ และข้อมูลเชิงลึกเกี่ยวกับการถ่ายภาพฟิล์มและแอป Frames",
            "keywords": "การถ่ายภาพฟิล์ม, การถ่ายภาพอนาล็อก, บล็อก, เคล็ดลับ, คู่มือ, แอป Frames"
        },
        "heading": "บล็อก",
        "labels": {
            "by_author": "โดย",
            "published_on": "เผยแพร่เมื่อ",
            "category": "หมวดหมู่",
            "all_posts": "บทความทั้งหมด",
            "in_category": "ใน"
        }
    },
    "el": {
        "meta": {
            "title": "Νέα Φωτογραφίας Φιλμ - Frames Blog",
            "description": "Άρθρα, συμβουλές και πληροφορίες για τη φωτογραφία φιλμ και την εφαρμογή Frames.",
            "keywords": "φωτογραφία φιλμ, αναλογική φωτογραφία, blog, συμβουλές, οδηγοί, εφαρμογή Frames"
        },
        "heading": "Blog",
        "labels": {
            "by_author": "από",
            "published_on": "Δημοσιεύτηκε",
            "category": "Κατηγορία",
            "all_posts": "Όλα τα άρθρα",
            "in_category": "στην"
        }
    }
}

# Blog.conf category (gear) translations (meta title max 60 chars, meta description max 160 chars)
BLOG_CONF_CATEGORIES = {
    "hi": {
        "slug": "upkaran",
        "name": "उपकरण",
        "meta_title": "फिल्म फोटोग्राफी उपकरण - कैमरा और फिल्म | Frames",
        "meta_description": "एनालॉग फोटोग्राफरों के लिए नए कैमरे, फिल्म स्टॉक, लेंस और उपकरण। रिव्यू और खरीदारी गाइड।"
    },
    "zh-hant": {
        "slug": "qicai",
        "name": "器材",
        "meta_title": "底片攝影器材 - 相機與底片 | Frames 部落格",
        "meta_description": "類比攝影師的新相機、底片、鏡頭和器材。評測和選購指南。"
    },
    "th": {
        "slug": "upakon",
        "name": "อุปกรณ์",
        "meta_title": "อุปกรณ์ถ่ายภาพฟิล์ม - กล้องและฟิล์ม | Frames",
        "meta_description": "กล้องใหม่ ฟิล์ม เลนส์ และอุปกรณ์สำหรับช่างภาพอนาล็อก รีวิวและคู่มือการซื้อ"
    },
    "el": {
        "slug": "exoplismos",
        "name": "Εξοπλισμός",
        "meta_title": "Εξοπλισμός Φωτογραφίας Φιλμ | Frames Blog",
        "meta_description": "Νέες κάμερες, φιλμ, φακοί και εξοπλισμός για αναλογικούς φωτογράφους. Κριτικές και οδηγοί αγοράς."
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
    languages = ["hi", "zh-hant", "th", "el"]

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
    print("Adding blog configuration for Hindi, Traditional Chinese,")
    print("Thai, and Greek languages")
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
