#!/usr/bin/env python3
"""
Unified Build Script for Frames Website
Combines homepage, privacy pages, and changelog generation into a single self-contained tool.

Usage:
    python build.py                 # Build everything (default)
    python build.py --homepage      # Build only homepage
    python build.py --privacy       # Build only privacy pages
    python build.py --changelog     # Build only changelog
    python build.py --homepage --privacy  # Build multiple components
"""

import argparse
import json
import math
import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
from PIL import Image

# Import from build_utils
from build_utils import format_date, minify_html, minify_javascript

# Get project root directory (go up from sources/scripts/ to root)
PROJECT_ROOT = Path(__file__).parent.parent.parent
TEMPLATES_DIR = PROJECT_ROOT / "sources" / "templates"
LOCALES_DIR = PROJECT_ROOT / "sources" / "locales"
CHANGELOG_DIR = LOCALES_DIR / "changelog"
OUTPUT_DIR = PROJECT_ROOT
SCHEMA_OUTPUT_DIR = PROJECT_ROOT / "lib" / "schema"

ENTRIES_PER_PAGE = 5


# ============================================================================
# CORE UTILITIES
# ============================================================================

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_global_config():
    """Load global configuration"""
    return load_json(LOCALES_DIR / "global.json")


def load_locale(lang_code):
    """Load locale-specific configuration"""
    return load_json(LOCALES_DIR / f"{lang_code}.json")


def load_css_file(css_name):
    """Load CSS file for inlining"""
    css_path = PROJECT_ROOT / "lib" / "css" / f"{css_name}.css"
    try:
        with open(css_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"⚠ Warning: {css_name}.css not found at {css_path}")
        print(f"  Please compile it first: sass lib/scss/{css_name}.scss lib/css/{css_name}.css --style compressed")
        return ""


def create_jinja_env(autoescape_enabled=True):
    """Create standardized Jinja2 environment"""
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(['html', 'xml']) if autoescape_enabled else False,
        trim_blocks=True,
        lstrip_blocks=True
    )

    # Add custom filter to remove step numbers (e.g., "1. " from beginning of string)
    def regex_replace(s, pattern, replacement):
        import re
        return re.sub(pattern, replacement, s)

    env.filters['regex_replace'] = regex_replace

    return env


def get_lang_config(global_config, lang_code):
    """Get language configuration from global config"""
    lang_config = next((l for l in global_config['languages'] if l['code'] == lang_code), None)
    if not lang_config:
        raise ValueError(f"Language {lang_code} not found in global config")
    return lang_config


def build_base_context(lang_code, global_config, locale_data, available_changelog_languages):
    """Build common context used across all templates"""
    lang_config = get_lang_config(global_config, lang_code)

    return {
        'lang': lang_code,
        'locale_data': locale_data,
        'global_config': global_config,
        'lang_config': lang_config,
        'all_languages': generate_language_list(global_config['languages']),
        'available_changelog_languages': available_changelog_languages
    }


# ============================================================================
# HREFLANG AND LANGUAGE UTILITIES
# ============================================================================

def generate_hreflang_links(languages, base_url="https://withframes.com", page="home"):
    """Generate hreflang alternate links for homepage, privacy, or docs page"""
    links = []

    for lang in languages:
        try:
            locale_data = load_locale(lang['code'])
            if page == "privacy":
                page_path = locale_data['urls']['privacy']
            elif page == "docs":
                page_path = locale_data['urls']['documentation']
            else:
                page_path = ''

            lang_path = lang['path'].strip('/')
            page_path = page_path.strip('/')

            if not lang_path:
                url = f"{base_url}/{page_path}" if page_path else base_url
            else:
                url = f"{base_url}/{lang_path}"
                if page_path:
                    url += f"/{page_path}"

            if not url.endswith('/'):
                url += '/'

            links.append({
                'hreflang': lang['hreflang'],
                'href': url
            })

        except FileNotFoundError:
            continue

    # Add x-default link
    if page == "privacy":
        x_default = f"{base_url}/privacy/"
    elif page == "docs":
        x_default = f"{base_url}/docs/"
    else:
        x_default = f"{base_url}/"
    links.append({
        'hreflang': 'x-default',
        'href': x_default
    })

    return links


def generate_language_list(languages):
    """Generate language list for dropdown"""
    lang_list = []
    for lang in languages:
        try:
            locale_data = load_locale(lang['code'])
            privacy_path = locale_data['urls']['privacy']
            docs_path = locale_data['urls']['documentation']
        except:
            privacy_path = 'privacy/'
            docs_path = 'docs/'

        lang_list.append({
            'code': lang['code'],
            'name': lang['name'],
            'url': lang['path'],
            'privacy_path': privacy_path,
            'docs_path': docs_path
        })
    return lang_list


def detect_available_changelog_languages():
    """Detect which languages have changelog translations"""
    available_languages = []
    if not CHANGELOG_DIR.exists():
        return available_languages

    for lang_dir in CHANGELOG_DIR.iterdir():
        if lang_dir.is_dir() and (lang_dir / "1.0.0-ios.json").exists():
            available_languages.append(lang_dir.name)

    return available_languages


# ============================================================================
# GENERIC RENDERING FUNCTIONS
# ============================================================================

def render_template(template_name, context, autoescape_enabled=True):
    """Generic template rendering function"""
    env = create_jinja_env(autoescape_enabled)
    template = env.get_template(template_name)
    return template.render(context)


def generate_html_page(template_name, lang_code, global_config, locale_data,
                       available_changelog_languages, extra_context=None):
    """Generic HTML page generation"""
    context = build_base_context(lang_code, global_config, locale_data, available_changelog_languages)

    if extra_context:
        context.update(extra_context)

    return render_template(template_name, context)


def generate_javascript_file(template_name, lang_code, locale_data, global_config):
    """Generic JavaScript generation function"""
    lang_config = get_lang_config(global_config, lang_code)

    context = {
        'lang': lang_code,
        'locale_data': locale_data,
        'global_config': global_config,
        'lang_config': lang_config
    }

    return render_template(template_name, context, autoescape_enabled=False)


def generate_schema_file(template_name, context):
    """Generic schema generation function"""
    return render_template(template_name, context, autoescape_enabled=False)


# ============================================================================
# SAVE FUNCTIONS
# ============================================================================

def get_output_path(lang_config, locale_data=None, page_type='index'):
    """Determine output path based on page type and language"""
    if page_type == 'index':
        if lang_config['path'] == '/':
            return OUTPUT_DIR / "index.html"
        else:
            path_parts = lang_config['path'].strip('/').split('/')
            output_dir = OUTPUT_DIR / '/'.join(path_parts)
            output_dir.mkdir(parents=True, exist_ok=True)
            return output_dir / "index.html"

    elif page_type == 'privacy':
        privacy_path = locale_data['urls']['privacy'].strip('/')
        if lang_config['path'] == '/':
            output_dir = OUTPUT_DIR / privacy_path
        else:
            lang_path = lang_config['path'].strip('/')
            output_dir = OUTPUT_DIR / lang_path / privacy_path
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir / "index.html"

    elif page_type == 'docs':
        docs_path = locale_data['urls']['documentation'].strip('/')
        if lang_config['path'] == '/':
            output_dir = OUTPUT_DIR / docs_path
        else:
            lang_path = lang_config['path'].strip('/')
            output_dir = OUTPUT_DIR / lang_path / docs_path
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir / "index.html"


def save_html(html, lang_config, locale_data=None, page_type='index', minify=True):
    """Save generated HTML to appropriate location"""
    if minify:
        html = minify_html(html)

    output_path = get_output_path(lang_config, locale_data, page_type)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✓ Generated: {output_path.relative_to(OUTPUT_DIR)}")


def save_schema(schema_json, schema_name, lang_code):
    """Save generated JSON-LD schema to appropriate location"""
    schema_dir = SCHEMA_OUTPUT_DIR / lang_code
    schema_dir.mkdir(parents=True, exist_ok=True)

    schema_path = schema_dir / schema_name
    with open(schema_path, 'w', encoding='utf-8') as f:
        f.write(schema_json)

    print(f"✓ Generated: {schema_path.relative_to(OUTPUT_DIR)}")


def get_javascript_output_path(lang_code, js_type='core'):
    """Get output path for JavaScript files"""
    if js_type == 'core':
        js_dir = PROJECT_ROOT / "lib" / "js" / lang_code
        return js_dir / "core.js"
    elif js_type == 'privacy':
        if lang_code == 'en':
            js_dir = PROJECT_ROOT / "lib" / "js"
        else:
            js_dir = PROJECT_ROOT / "lib" / "js" / lang_code
        return js_dir / "privacy.js"
    elif js_type == 'changelog':
        if lang_code == 'en':
            js_dir = PROJECT_ROOT / "lib" / "js" / "changelog"
        else:
            js_dir = PROJECT_ROOT / "lib" / "js" / lang_code / "changelog"
        return js_dir / "core.js"
    elif js_type == 'docs':
        if lang_code == 'en':
            js_dir = PROJECT_ROOT / "lib" / "js"
        else:
            js_dir = PROJECT_ROOT / "lib" / "js" / lang_code
        return js_dir / "docs.js"


def save_javascript(javascript, lang_code, js_type='core', minify=True):
    """Save generated JavaScript to appropriate location"""
    if minify:
        javascript = minify_javascript(javascript)

    js_path = get_javascript_output_path(lang_code, js_type)
    js_path.parent.mkdir(parents=True, exist_ok=True)

    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(javascript)

    print(f"✓ Generated: {js_path.relative_to(OUTPUT_DIR)}")


# ============================================================================
# HOMEPAGE GENERATION
# ============================================================================

def generate_formatted_reviews(locale_data, lang_code):
    """Generate formatted dates for reviews"""
    formatted_reviews = {}
    for i in range(1, 10):
        review_key = f'review{i}'
        if review_key in locale_data['reviews'] and 'datetime' in locale_data['reviews'][review_key]:
            iso_date = locale_data['reviews'][review_key]['datetime']
            formatted_reviews[review_key] = {
                'formatted_date': format_date(iso_date, lang_code)
            }
    return formatted_reviews


def get_latest_changelog_entries(lang_code, limit=4):
    """Get the latest N changelog entries for homepage display"""
    entries = load_changelog_entries(lang_code)
    latest_entries = []
    for entry in entries[:limit]:
        formatted_entry = format_changelog_entry(entry.copy(), lang_code)
        latest_entries.append(formatted_entry)
    return latest_entries


def generate_homepage_schemas(lang_code, global_config, locale_data):
    """Generate all schemas for homepage"""
    schemas_to_generate = [
        ('schemas/software.json', {}),
        ('schemas/video.json', {}),
        ('schemas/faq.json', {}),
        ('schemas/organization.json', {
            'global_urls': global_config['urls'],
            'appstore_url': locale_data['urls']['appstore_ios'],
            'macappstore_url': locale_data['urls']['appstore_macos'],
            'company_description': locale_data['company']['description']
        }),
        ('schemas/webpage-homepage.json', {
            'lang': lang_code,
            'canonical_url': locale_data['meta']['canonical_url'].rstrip('/') + '/',
            'seo_meta_title': locale_data['meta']['title'],
            'seo_meta_description': locale_data['meta']['description']
        }),
        ('schemas/howto.json', {})
    ]

    for schema_name, extra_context in schemas_to_generate:
        context = {
            'lang': lang_code,
            'canonical_url': locale_data['meta']['canonical_url'].rstrip('/'),
            'currency': locale_data['pricing']['currency'].rstrip('/'),
            'monthly_price': locale_data['pricing']['ios']['price_value_monthly'],
            'yearly_price': locale_data['pricing']['ios']['price_value_yearly'],
            'monthly_label': locale_data['pricing']['label_subscription_monthly'],
            'yearly_label': locale_data['pricing']['label_subscription_yearly'],
            'ios_appname': locale_data['footer']['product']['frames_ios'],
            'mac_appname': locale_data['footer']['product']['frames_macos'],
            'seo_meta_title': locale_data['meta']['title'],
            'seo_meta_description': locale_data['meta']['description'],
            'appstore_url': locale_data['urls']['appstore_ios'],
            'macappstore_url': locale_data['urls']['appstore_macos'],
            'video_title': locale_data['video']['title'],
            'video_description': locale_data['video']['description'],
            'global_urls': global_config['urls'],
            'app_version_ios': global_config['app_version_ios'],
            'app_version_macos': global_config['app_version_macos'],
            'keywords': locale_data['meta']['keywords']
        }

        # Add review data
        for i in range(1, 10):
            review_key = f'review{i}'
            if review_key in locale_data['reviews']:
                context[f'review{i}_author'] = locale_data['reviews'][review_key]['author_name']
                context[f'review{i}_date'] = locale_data['reviews'][review_key]['datetime']
                context[f'review{i}_title'] = locale_data['reviews'][review_key]['title']
                context[f'review{i}_descr'] = locale_data['reviews'][review_key]['quote']
                context[f'review{i}_rating'] = '5'

        # Add FAQ data
        for i in range(1, 9):
            question_key = f'question{i}'
            if question_key in locale_data['qa']:
                context[f'faq_question{i}'] = locale_data['qa'][question_key]['question']
                context[f'faq_answer{i}'] = locale_data['qa'][question_key]['answer']

        # Add howto data
        if 'howto' in locale_data:
            context['locale_data'] = locale_data

        context.update(extra_context)

        # Use correct template name
        template_map = {
            'schemas/webpage-homepage.json': 'schemas/webpage.json'
        }
        template_name = template_map.get(schema_name, schema_name)

        schema_json = generate_schema_file(template_name, context)
        # Remove 'schemas/' prefix from schema_name for saving
        output_name = schema_name.replace('schemas/', '')
        save_schema(schema_json, output_name, lang_code)


def build_homepage(global_config, languages):
    """Build homepage for all languages"""
    print("\n" + "=" * 50)
    print("Building Homepages")
    print("=" * 50)

    critical_css = load_css_file('critical')
    if critical_css:
        print(f"✓ Loaded critical CSS ({len(critical_css)} bytes)")
    else:
        print("⚠ No critical CSS loaded - templates will use fallback")

    available_changelog_languages = detect_available_changelog_languages()
    print(f"✓ Detected {len(available_changelog_languages)} languages with changelog translations")

    for lang in languages:
        lang_code = lang['code']
        try:
            locale_data = load_locale(lang_code)
            print(f"✓ Loaded locale: {lang_code}")

            # Generate HTML
            extra_context = {
                'hreflang_links': generate_hreflang_links(global_config['languages'], page="home"),
                'critical_css': critical_css,
                'formatted_reviews': generate_formatted_reviews(locale_data, lang_code),
                'latest_changelog_entries': get_latest_changelog_entries(lang_code)
            }
            html = generate_html_page('index.html', lang_code, global_config, locale_data,
                                     available_changelog_languages, extra_context)
            save_html(html, lang, locale_data, 'index')

            # Generate schemas
            generate_homepage_schemas(lang_code, global_config, locale_data)

            # Generate JavaScript
            javascript = generate_javascript_file('js/core.js', lang_code, locale_data, global_config)
            save_javascript(javascript, lang_code, 'core')

        except FileNotFoundError:
            print(f"✗ Warning: {lang_code}.json not found, skipping...")
        except Exception as e:
            print(f"✗ Error generating {lang_code}: {e}")

    print("\nGenerating homepage sitemap...")
    generate_sitemap(languages, 'home')


# ============================================================================
# PRIVACY PAGES GENERATION
# ============================================================================

def build_privacy(global_config, languages):
    """Build privacy pages for all languages"""
    print("\n" + "=" * 50)
    print("Building Privacy Pages")
    print("=" * 50)

    privacy_css = load_css_file('privacy')
    if privacy_css:
        print(f"✓ Loaded privacy CSS ({len(privacy_css)} bytes)")
    else:
        print("⚠ No privacy CSS loaded - templates will use fallback")

    available_changelog_languages = detect_available_changelog_languages()

    for lang in languages:
        lang_code = lang['code']
        try:
            locale_data = load_locale(lang_code)
            print(f"✓ Loaded locale: {lang_code}")

            # Generate HTML
            extra_context = {
                'hreflang_links': generate_hreflang_links(global_config['languages'], page="privacy"),
                'privacy_css': privacy_css
            }
            html = generate_html_page('privacy.html', lang_code, global_config, locale_data,
                                     available_changelog_languages, extra_context)
            save_html(html, lang, locale_data, 'privacy')

            # Generate WebPage schema
            webpage_context = {
                'lang': lang_code,
                'canonical_url': locale_data['privacy']['meta']['canonical_url'].rstrip('/') + '/',
                'seo_meta_title': locale_data['privacy']['meta']['title'],
                'seo_meta_description': locale_data['privacy']['meta']['description'],
                'keywords': locale_data['meta']['keywords']
            }
            webpage_json = generate_schema_file('schemas/webpage.json', webpage_context)
            save_schema(webpage_json, 'webpage-privacy.json', lang_code)

            # Generate Breadcrumb schema
            breadcrumb_context = {
                'lang': lang_code,
                'button_home': locale_data['privacy']['button_home'],
                'privacy_heading': locale_data['privacy']['heading'],
                'canonical_url': locale_data['privacy']['meta']['canonical_url'].rstrip('/') + '/'
            }
            breadcrumb_json = generate_schema_file('schemas/breadcrumb-privacy.json', breadcrumb_context)
            save_schema(breadcrumb_json, 'breadcrumb-privacy.json', lang_code)

            # Generate JavaScript
            javascript = generate_javascript_file('js/privacy.js', lang_code, locale_data, global_config)
            save_javascript(javascript, lang_code, 'privacy')

        except FileNotFoundError:
            print(f"✗ Warning: {lang_code}.json not found, skipping...")
        except Exception as e:
            print(f"✗ Error generating privacy for {lang_code}: {e}")

    print("\nGenerating privacy sitemap...")
    generate_sitemap(languages, 'privacy')


# ============================================================================
# DOCUMENTATION PAGES GENERATION
# ============================================================================

def build_docs(global_config, languages):
    """Build documentation pages for all languages"""
    print("\n" + "=" * 50)
    print("Building Documentation Pages")
    print("=" * 50)

    docs_css = load_css_file('docs')
    if docs_css:
        print(f"✓ Loaded docs CSS ({len(docs_css)} bytes)")
    else:
        print("⚠ No docs CSS loaded - templates will use fallback")

    available_changelog_languages = detect_available_changelog_languages()

    for lang in languages:
        lang_code = lang['code']
        try:
            locale_data = load_locale(lang_code)
            print(f"✓ Loaded locale: {lang_code}")

            # Generate HTML
            extra_context = {
                'hreflang_links': generate_hreflang_links(global_config['languages'], page="docs"),
                'docs_css': docs_css
            }
            html = generate_html_page('docs.html', lang_code, global_config, locale_data,
                                     available_changelog_languages, extra_context)
            save_html(html, lang, locale_data, 'docs')

            # Generate WebPage schema
            webpage_context = {
                'lang': lang_code,
                'canonical_url': locale_data['docs']['meta']['canonical_url'].rstrip('/') + '/',
                'seo_meta_title': locale_data['docs']['meta']['title'],
                'seo_meta_description': locale_data['docs']['meta']['description'],
                'keywords': locale_data['meta']['keywords']
            }
            webpage_json = generate_schema_file('schemas/webpage.json', webpage_context)
            save_schema(webpage_json, 'webpage-docs.json', lang_code)

            # Generate Breadcrumb schema
            breadcrumb_context = {
                'lang': lang_code,
                'button_home': locale_data['privacy']['button_home'],
                'docs_heading': locale_data['header']['navigation']['documentation'],
                'canonical_url': locale_data['docs']['meta']['canonical_url'].rstrip('/') + '/'
            }
            breadcrumb_json = generate_schema_file('schemas/breadcrumb-docs.json', breadcrumb_context)
            save_schema(breadcrumb_json, 'breadcrumb-docs.json', lang_code)

            # Generate Video schema
            video_context = {
                'video_title': locale_data['video']['title'],
                'video_description': locale_data['video']['description'],
                'keywords': locale_data['meta']['keywords'],
                'global_urls': global_config['urls']
            }
            video_json = generate_schema_file('schemas/video.json', video_context)
            save_schema(video_json, 'video.json', lang_code)

            # Generate JavaScript
            javascript = generate_javascript_file('js/docs.js', lang_code, locale_data, global_config)
            save_javascript(javascript, lang_code, 'docs')

        except FileNotFoundError:
            print(f"✗ Warning: {lang_code}.json not found, skipping...")
        except Exception as e:
            print(f"✗ Error generating docs for {lang_code}: {e}")

    print("\nGenerating docs sitemap...")
    generate_sitemap(languages, 'docs')


# ============================================================================
# CHANGELOG GENERATION
# ============================================================================

def load_changelog_entries(lang_code='en'):
    """Load all changelog entries and sort by date (newest first)"""
    entries = []
    lang_changelog_dir = CHANGELOG_DIR / lang_code

    if not lang_changelog_dir.exists():
        print(f"✗ Changelog directory not found: {lang_changelog_dir}")
        return entries

    for entry_file in lang_changelog_dir.glob("*.json"):
        try:
            entry_data = load_json(entry_file)
            entries.append(entry_data)
        except Exception as e:
            print(f"✗ Error loading {entry_file}: {e}")

    entries.sort(key=lambda x: x['release_date'], reverse=True)
    return entries


def get_current_build_date():
    """Get current date in ISO format for schema dateModified"""
    return datetime.now().strftime('%Y-%m-%dT%H:%M:%S+00:00')


def get_first_image_from_entry(entry):
    """Extract the first image and alt text from an entry's sections"""
    if 'sections' not in entry:
        return None, None

    for section in entry['sections']:
        if section.get('type') == 'media' and 'image' in section:
            return (
                section['image'],
                section.get('alt', '')
            )
    return None, None


def process_entry_images(entry, lang_code):
    """Process language-specific image paths in entry"""
    if 'sections' in entry:
        for section in entry['sections']:
            if section.get('type') == 'media':
                if 'image' in section and '{{ lang }}' in section['image']:
                    section['image'] = section['image'].replace('{{ lang }}', lang_code)
                if 'image_2x' in section and '{{ lang }}' in section['image_2x']:
                    section['image_2x'] = section['image_2x'].replace('{{ lang }}', lang_code)
    return entry


def format_changelog_entry(entry, lang_code):
    """Add formatted date and process images for entry"""
    entry['formatted_date'] = format_date(entry['release_date'], lang_code)
    return process_entry_images(entry, lang_code)


def resolve_source_image_path(image_path, lang_code):
    """Resolve the actual filesystem path for a changelog image"""
    relative_path = image_path.lstrip('/')
    path_obj = Path(relative_path)
    base_name = path_obj.stem
    extension = path_obj.suffix
    image_2x_name = f"{base_name}@2x{extension}"

    # Try language-specific version first
    lang_specific_path = PROJECT_ROOT / "lib" / "img" / lang_code / "changelog" / image_2x_name
    if lang_specific_path.exists():
        return lang_specific_path

    # Try shared version
    shared_path = PROJECT_ROOT / "lib" / "img" / "shared" / "changelog" / image_2x_name
    if shared_path.exists():
        return shared_path

    # Fallback to original path
    original_path = PROJECT_ROOT / relative_path
    if original_path.exists():
        return original_path

    return None


def generate_og_image(source_image_path, output_path, bg_color=(28, 28, 30)):
    """Generate OG image from source PNG with transparency"""
    try:
        if output_path.exists():
            return True

        img = Image.open(source_image_path)

        # Convert RGBA to RGB by compositing on background color
        if img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, bg_color)
            if img.mode == 'P':
                img = img.convert('RGBA')
            if img.mode == 'RGBA':
                background.paste(img, mask=img.split()[3])
            else:
                background.paste(img)
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')

        # Scale to 600px width
        target_width = 600
        target_height = 315
        aspect_ratio = img.height / img.width
        scaled_height = int(target_width * aspect_ratio)
        img = img.resize((target_width, scaled_height), Image.Resampling.LANCZOS)

        # Crop or pad vertically to center at 315px height
        if scaled_height > target_height:
            # Crop vertically from center
            crop_top = (scaled_height - target_height) // 2
            crop_bottom = crop_top + target_height
            img = img.crop((0, crop_top, target_width, crop_bottom))
        elif scaled_height < target_height:
            # Pad vertically to center (edge case for very wide images)
            canvas = Image.new('RGB', (target_width, target_height), bg_color)
            paste_y = (target_height - scaled_height) // 2
            canvas.paste(img, (0, paste_y))
            img = canvas

        output_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(output_path, 'JPEG', quality=85, optimize=True)

        return True

    except Exception as e:
        print(f"⚠ Warning: Failed to generate OG image {output_path.name}: {e}")
        return False


def generate_changelog_og_image(lang_code, image_path, filename):
    """Generate OG image for changelog"""
    if not image_path:
        return '/og-image.jpg'

    source_path = resolve_source_image_path(image_path, lang_code)
    if not source_path:
        print(f"⚠ Warning: Source image not found: {image_path}")
        return '/og-image.jpg'

    output_dir = PROJECT_ROOT / "lib" / "img" / lang_code / "changelog" / "og-image"
    output_path = output_dir / filename

    success = generate_og_image(source_path, output_path)

    if success:
        return f"/lib/img/{lang_code}/changelog/og-image/{filename}"
    else:
        return '/og-image.jpg'


def generate_all_changelog_og_images(entries, lang_code):
    """Generate OG images for all changelog entries upfront"""
    for entry in entries:
        first_image, alt_text = get_first_image_from_entry(entry)
        if first_image:
            og_filename = f"{entry['url_slug']}-og-image.jpg"
            og_image_url = generate_changelog_og_image(lang_code, first_image, og_filename)
            entry['og_image_url'] = og_image_url
            entry['og_image_alt'] = alt_text
        else:
            entry['og_image_url'] = '/og-image.jpg'
            entry['og_image_alt'] = ''


def generate_changelog_hreflang_links(languages, page_type='index', page_number=1, url_slug=None, base_url="https://withframes.com"):
    """Generate hreflang alternate links for changelog pages"""
    links = []
    for lang in languages:
        if page_type == 'index':
            if lang['code'] == 'en':
                url_path = '/changelog/'
            else:
                url_path = f"/{lang['code']}/changelog/"

            if page_number > 1:
                url_path = url_path.rstrip('/') + f"/page-{page_number}/"

        elif page_type == 'entry':
            if lang['code'] == 'en':
                url_path = f'/changelog/{url_slug}/'
            else:
                url_path = f"/{lang['code']}/changelog/{url_slug}/"

        url = f"{base_url}{url_path}"
        links.append({
            'hreflang': lang['hreflang'],
            'href': url
        })

    # Add x-default
    if page_type == 'index':
        x_default_path = '/changelog/' if page_number == 1 else f'/changelog/page-{page_number}/'
    else:
        x_default_path = f'/changelog/{url_slug}/'

    links.append({
        'hreflang': 'x-default',
        'href': base_url + x_default_path
    })

    return links


def save_changelog_schema(schema_json, schema_name, lang_code, page_type='page', page_number=None, url_slug=None):
    """Save generated JSON-LD schema to appropriate location"""
    schema_base_dir = PROJECT_ROOT / "lib" / "schema"

    if page_type == 'changelog-index':
        if page_number == 1:
            schema_dir = schema_base_dir / lang_code / "changelog"
        else:
            schema_dir = schema_base_dir / lang_code / "changelog" / f"page-{page_number}"
    elif page_type == 'changelog-entry':
        schema_dir = schema_base_dir / lang_code / "changelog" / url_slug
    else:
        schema_dir = schema_base_dir / lang_code

    schema_dir.mkdir(parents=True, exist_ok=True)

    schema_path = schema_dir / schema_name
    with open(schema_path, 'w', encoding='utf-8') as f:
        f.write(schema_json)


def generate_changelog_schemas(lang_code, locale_data, global_config, page_type, **kwargs):
    """Generate schemas for changelog pages"""
    build_date = get_current_build_date()

    # Extract only the parameters save_changelog_schema needs
    page_number = kwargs.get('page_number')
    url_slug = kwargs.get('url_slug')

    # Common organization schema
    org_context = {
        'global_urls': global_config['urls'],
        'appstore_url': locale_data['urls']['appstore_ios'],
        'macappstore_url': locale_data['urls']['appstore_macos'],
        'company_description': locale_data['company']['description']
    }
    organization_schema = generate_schema_file('schemas/organization.json', org_context)
    save_changelog_schema(organization_schema, 'organization.json', lang_code, page_type, page_number, url_slug)

    # Breadcrumb schema
    breadcrumb_context = {
        'lang': lang_code,
        'button_home': locale_data['privacy']['button_home'],
        'changelog_heading': locale_data['changelog']['heading'],
        'canonical_url': kwargs.get('canonical_url'),
        'entry_title': kwargs.get('entry_title'),
        'page_number': kwargs.get('page_number') if kwargs.get('page_number', 1) > 1 else None
    }
    breadcrumb_schema = generate_schema_file('schemas/breadcrumb.json', breadcrumb_context)
    save_changelog_schema(breadcrumb_schema, 'breadcrumb.json', lang_code, page_type, page_number, url_slug)

    # Page-specific schemas
    if page_type == 'changelog-index' and kwargs.get('page_number', 1) == 1:
        blog_context = {
            'lang': lang_code,
            'canonical_url': kwargs['canonical_url'],
            'page_title': locale_data['changelog']['meta']['title'],
            'page_description': locale_data['changelog']['meta']['description'],
            'entries': kwargs.get('all_entries', []),
            'build_date': build_date,
            'keywords': locale_data['meta']['keywords']
        }
        blog_schema = generate_schema_file('schemas/blog.json', blog_context)
        save_changelog_schema(blog_schema, 'blog.json', lang_code, page_type, page_number, url_slug)

    elif page_type == 'changelog-entry':
        entry = kwargs.get('entry')

        blogposting_context = {
            'lang': lang_code,
            'canonical_url': kwargs['canonical_url'],
            'entry': entry,
            'build_date': build_date,
            'og_image_url': entry.get('og_image_url', '/og-image.jpg'),
            'og_image_alt': entry.get('og_image_alt', ''),
            'keywords': locale_data['meta']['keywords']
        }
        blogposting_schema = generate_schema_file('schemas/blogposting.json', blogposting_context)
        save_changelog_schema(blogposting_schema, 'blogposting.json', lang_code, page_type, page_number, url_slug)


def save_changelog_html(html, page_type, lang_code='en', page_number=None, entry=None):
    """Save changelog HTML to appropriate location"""
    if lang_code == 'en':
        output_base = PROJECT_ROOT / "changelog"
        path_prefix = "changelog"
    else:
        output_base = PROJECT_ROOT / lang_code / "changelog"
        path_prefix = f"{lang_code}/changelog"

    if page_type == 'index':
        if page_number == 1:
            output_path = output_base / "index.html"
            output_base.mkdir(parents=True, exist_ok=True)
        else:
            output_dir = output_base / f"page-{page_number}"
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / "index.html"

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"✓ Generated: {path_prefix}/{'index.html' if page_number == 1 else f'page-{page_number}/index.html'}")

    elif page_type == 'entry':
        output_dir = output_base / entry['url_slug']
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "index.html"

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"✓ Generated: {path_prefix}/{entry['url_slug']}/index.html")


def build_changelog_pages(global_config):
    """Build changelog pages for all languages"""
    print("\n" + "=" * 50)
    print("Building Changelog")
    print("=" * 50)

    changelog_css = load_css_file('changelog')
    if changelog_css:
        print(f"✓ Loaded changelog CSS ({len(changelog_css)} bytes)")
    else:
        print("⚠ No changelog CSS loaded - templates will use fallback")

    available_languages = []
    for lang_dir in CHANGELOG_DIR.iterdir():
        if lang_dir.is_dir() and (lang_dir / "1.0.0-ios.json").exists():
            available_languages.append(lang_dir.name)

    print(f"✓ Detected {len(available_languages)} languages with changelog translations: {', '.join(sorted(available_languages))}")

    for lang_code in available_languages:
        print(f"\n--- Generating changelog for {lang_code} ---")

        try:
            locale_data = load_locale(lang_code)
            print(f"✓ Loaded locale: {lang_code}")

            entries = load_changelog_entries(lang_code)

            if not entries:
                print(f"⚠ No changelog entries found for {lang_code}")
                continue

            print(f"✓ Loaded {len(entries)} changelog entries")

            # Generate OG images for all entries upfront
            generate_all_changelog_og_images(entries, lang_code)
            print(f"✓ Generated OG images for changelog entries")

            total_pages = math.ceil(len(entries) / ENTRIES_PER_PAGE)
            print(f"✓ Total pages: {total_pages}")

            # Generate index pages
            for page in range(1, total_pages + 1):
                start_idx = (page - 1) * ENTRIES_PER_PAGE
                end_idx = start_idx + ENTRIES_PER_PAGE
                page_entries = [format_changelog_entry(e.copy(), lang_code) for e in entries[start_idx:end_idx]]

                canonical_url = f"https://withframes.com{'/' + lang_code if lang_code != 'en' else ''}/changelog/"
                if page > 1:
                    canonical_url += f"page-{page}/"

                extra_context = {
                    'hreflang_links': generate_changelog_hreflang_links(global_config['languages'], page_type='index', page_number=page),
                    'entries': page_entries,
                    'page_number': page,
                    'total_pages': total_pages,
                    'changelog_css': changelog_css
                }

                html = generate_html_page('changelog-index.html', lang_code, global_config, locale_data,
                                         available_languages, extra_context)
                html = minify_html(html)
                save_changelog_html(html, 'index', lang_code, page_number=page)

                # Generate schemas
                generate_changelog_schemas(lang_code, locale_data, global_config, 'changelog-index',
                                         page_number=page, canonical_url=canonical_url,
                                         all_entries=entries)

            # Generate individual entry pages
            for i, entry in enumerate(entries):
                entry = format_changelog_entry(entry.copy(), lang_code)
                prev_entry = format_changelog_entry(entries[i - 1].copy(), lang_code) if i > 0 else None
                next_entry = format_changelog_entry(entries[i + 1].copy(), lang_code) if i < len(entries) - 1 else None

                canonical_url = f"https://withframes.com{'/' + lang_code if lang_code != 'en' else ''}/changelog/{entry['url_slug']}/"

                extra_context = {
                    'hreflang_links': generate_changelog_hreflang_links(global_config['languages'], page_type='entry', url_slug=entry['url_slug']),
                    'entry': entry,
                    'prev_entry': prev_entry,
                    'next_entry': next_entry,
                    'changelog_css': changelog_css,
                    'og_image_url': entry.get('og_image_url', '/og-image.jpg')
                }

                html = generate_html_page('changelog-entry.html', lang_code, global_config, locale_data,
                                         available_languages, extra_context)
                html = minify_html(html)
                save_changelog_html(html, 'entry', lang_code, entry=entry)

                # Generate schemas
                generate_changelog_schemas(lang_code, locale_data, global_config, 'changelog-entry',
                                         canonical_url=canonical_url, entry=entry,
                                         url_slug=entry['url_slug'], entry_title=entry['title'])

            # Generate sitemap
            generate_changelog_sitemap(entries, lang_code)

            # Generate RSS feed
            generate_rss_feed(entries, lang_code, locale_data)

            # Generate JavaScript
            javascript = generate_javascript_file('js/changelog.js', lang_code, locale_data, global_config)
            save_javascript(javascript, lang_code, 'changelog')

        except FileNotFoundError:
            print(f"✗ Warning: {lang_code}.json not found, skipping...")
        except Exception as e:
            print(f"✗ Error generating changelog for {lang_code}: {e}")
            import traceback
            traceback.print_exc()

    print("\nGenerating changelog sitemap index...")
    generate_changelog_sitemap_index(available_languages)


# ============================================================================
# SITEMAP GENERATION
# ============================================================================

def generate_sitemap(languages, sitemap_type):
    """Generic sitemap generation"""
    sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    base_url = "https://withframes.com"
    current_date = datetime.now().strftime('%Y-%m-%d')

    for lang in languages:
        try:
            if sitemap_type == 'home':
                if lang['code'] == 'en':
                    url = f"{base_url}/"
                    priority = "1.0"
                else:
                    url = f"{base_url}{lang['path']}"
                    priority = "0.9"
                changefreq = 'weekly'

            elif sitemap_type == 'privacy':
                locale_data = load_locale(lang['code'])
                privacy_url = locale_data['urls']['privacy']
                if not privacy_url.startswith('/'):
                    privacy_url = '/' + privacy_url

                if lang['code'] == 'en':
                    url = f"{base_url}/{privacy_url.lstrip('/')}"
                    priority = "0.8"
                else:
                    url = f"{base_url}/{lang['code']}/{privacy_url.lstrip('/')}"
                    priority = "0.7"
                changefreq = 'yearly'

            elif sitemap_type == 'docs':
                locale_data = load_locale(lang['code'])
                docs_url = locale_data['urls']['documentation']
                if not docs_url.startswith('/'):
                    docs_url = '/' + docs_url

                if lang['code'] == 'en':
                    url = f"{base_url}/{docs_url.lstrip('/')}"
                    priority = "0.8"
                else:
                    url = f"{base_url}/{lang['code']}/{docs_url.lstrip('/')}"
                    priority = "0.7"
                changefreq = 'monthly'

            sitemap_lines.append('  <url>')
            sitemap_lines.append(f'    <loc>{url}</loc>')
            sitemap_lines.append(f'    <lastmod>{current_date}</lastmod>')
            sitemap_lines.append(f'    <changefreq>{changefreq}</changefreq>')
            sitemap_lines.append(f'    <priority>{priority}</priority>')
            sitemap_lines.append('  </url>')

        except FileNotFoundError:
            continue

    sitemap_lines.append('</urlset>')
    sitemap_content = '\n'.join(sitemap_lines)

    sitemap_path = PROJECT_ROOT / f"sitemap-{sitemap_type}.xml"
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

    print(f"✓ Generated: sitemap-{sitemap_type}.xml")
    return sitemap_path


def generate_rss_feed(entries, lang_code, locale_data):
    """Generate RSS feed for changelog"""
    from email.utils import formatdate
    from xml.sax.saxutils import escape

    base_url = "https://withframes.com"

    # Build canonical URL for changelog
    if lang_code == 'en':
        canonical_url = f"{base_url}/changelog/"
        feed_url = f"{base_url}/changelog/rss/index.rss"
    else:
        canonical_url = f"{base_url}/{lang_code}/changelog/"
        feed_url = f"{base_url}/{lang_code}/changelog/rss/index.rss"

    # Format entries for RSS
    rss_entries = []
    for entry in entries:
        # Convert ISO date to RFC 822 format for RSS
        release_date = datetime.fromisoformat(entry['release_date'].replace('Z', '+00:00'))
        pub_date = formatdate(release_date.timestamp(), usegmt=True)

        # Build entry canonical URL
        if lang_code == 'en':
            entry_url = f"{base_url}/changelog/{entry['url_slug']}/"
        else:
            entry_url = f"{base_url}/{lang_code}/changelog/{entry['url_slug']}/"

        rss_entries.append({
            'title': escape(entry['title']),
            'summary': escape(entry['summary']),
            'canonical_url': entry_url,
            'pub_date': pub_date
        })

    # Get current build date in RFC 822 format
    build_date = formatdate(datetime.now().timestamp(), usegmt=True)

    # Render RSS template
    context = {
        'lang': lang_code,
        'locale_data': locale_data,
        'canonical_url': canonical_url,
        'feed_url': feed_url,
        'build_date': build_date,
        'entries': rss_entries
    }

    rss_content = render_template('rss/feed.xml', context, autoescape_enabled=False)

    # Save RSS feed
    if lang_code == 'en':
        rss_dir = PROJECT_ROOT / "changelog" / "rss"
    else:
        rss_dir = PROJECT_ROOT / lang_code / "changelog" / "rss"

    rss_dir.mkdir(parents=True, exist_ok=True)

    rss_path = rss_dir / "index.rss"
    with open(rss_path, 'w', encoding='utf-8') as f:
        f.write(rss_content)

    print(f"✓ Generated RSS feed: {rss_path.relative_to(PROJECT_ROOT)}")


def generate_changelog_sitemap(entries, lang_code='en'):
    """Generate changelog-specific sitemap"""
    sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    base_url = "https://withframes.com"
    current_date = datetime.now().strftime('%Y-%m-%d')

    if lang_code == 'en':
        url_prefix = "/changelog"
        output_base = PROJECT_ROOT / "changelog"
        path_prefix = "changelog"
    else:
        url_prefix = f"/{lang_code}/changelog"
        output_base = PROJECT_ROOT / lang_code / "changelog"
        path_prefix = f"{lang_code}/changelog"

    # Add changelog index
    sitemap_lines.append('  <url>')
    sitemap_lines.append(f'    <loc>{base_url}{url_prefix}/</loc>')
    sitemap_lines.append(f'    <lastmod>{current_date}</lastmod>')
    sitemap_lines.append('    <changefreq>weekly</changefreq>')
    sitemap_lines.append('    <priority>0.8</priority>')
    sitemap_lines.append('  </url>')

    # Add pagination pages
    total_pages = math.ceil(len(entries) / ENTRIES_PER_PAGE)
    for page in range(2, total_pages + 1):
        sitemap_lines.append('  <url>')
        sitemap_lines.append(f'    <loc>{base_url}{url_prefix}/page-{page}/</loc>')
        sitemap_lines.append(f'    <lastmod>{current_date}</lastmod>')
        sitemap_lines.append('    <changefreq>weekly</changefreq>')
        sitemap_lines.append('    <priority>0.7</priority>')
        sitemap_lines.append('  </url>')

    # Add individual entries
    for entry in entries:
        sitemap_lines.append('  <url>')
        sitemap_lines.append(f'    <loc>{base_url}{url_prefix}/{entry["url_slug"]}/</loc>')
        sitemap_lines.append(f'    <lastmod>{current_date}</lastmod>')
        sitemap_lines.append('    <changefreq>monthly</changefreq>')
        sitemap_lines.append('    <priority>0.6</priority>')
        sitemap_lines.append('  </url>')

    sitemap_lines.append('</urlset>')
    sitemap_content = '\n'.join(sitemap_lines)

    output_base.mkdir(parents=True, exist_ok=True)
    sitemap_path = output_base / "sitemap.xml"
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

    print(f"✓ Generated: {path_prefix}/sitemap.xml")
    return sitemap_path


def generate_changelog_sitemap_index(available_languages):
    """Generate sitemap index for all changelog sitemaps"""
    sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_lines.append('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    base_url = "https://withframes.com"
    current_date = datetime.now().strftime('%Y-%m-%d')

    for lang_code in sorted(available_languages):
        if lang_code == 'en':
            sitemap_url = f"{base_url}/changelog/sitemap.xml"
        else:
            sitemap_url = f"{base_url}/{lang_code}/changelog/sitemap.xml"

        sitemap_lines.append('  <sitemap>')
        sitemap_lines.append(f'    <loc>{sitemap_url}</loc>')
        sitemap_lines.append(f'    <lastmod>{current_date}</lastmod>')
        sitemap_lines.append('  </sitemap>')

    sitemap_lines.append('</sitemapindex>')
    sitemap_content = '\n'.join(sitemap_lines)

    sitemap_path = PROJECT_ROOT / "sitemap-changelog.xml"
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

    print(f"✓ Generated: sitemap-changelog.xml")
    return sitemap_path


# ============================================================================
# MAIN FUNCTION WITH CLI
# ============================================================================

def main():
    """Main build function with CLI argument parsing"""
    parser = argparse.ArgumentParser(
        description='Unified build script for Frames website',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python build.py                    Build everything
  python build.py --homepage         Build only homepage
  python build.py --privacy          Build only privacy pages
  python build.py --docs             Build only documentation pages
  python build.py --changelog        Build only changelog
  python build.py --homepage --privacy   Build homepage and privacy
        """
    )

    parser.add_argument('--homepage', action='store_true', help='Build homepage')
    parser.add_argument('--privacy', action='store_true', help='Build privacy pages')
    parser.add_argument('--docs', action='store_true', help='Build documentation pages')
    parser.add_argument('--changelog', action='store_true', help='Build changelog')

    args = parser.parse_args()

    # If no arguments provided, build everything
    build_all = not (args.homepage or args.privacy or args.docs or args.changelog)

    print("Frames Website Builder")
    print("=" * 50)

    # Run CSS optimization first
    print("\n🎨 Optimizing CSS...")
    optimize_css_script = PROJECT_ROOT / "sources" / "scripts" / "optimize_css.sh"
    if optimize_css_script.exists():
        try:
            result = subprocess.run(
                ["bash", str(optimize_css_script)],
                cwd=PROJECT_ROOT,
                capture_output=True,
                text=True,
                check=True
            )
            print("✓ CSS optimization completed")
            if result.stdout:
                print(result.stdout.strip())
        except subprocess.CalledProcessError as e:
            print(f"⚠ Warning: CSS optimization failed: {e}")
            if e.stderr:
                print(e.stderr.strip())
    else:
        print(f"⚠ Warning: optimize_css.sh not found at {optimize_css_script}")

    # Load global config
    try:
        global_config = load_global_config()
        print(f"✓ Loaded global config")
    except FileNotFoundError:
        print("✗ Error: global.json not found in build/locales/")
        sys.exit(1)

    languages = global_config['languages']

    # Build requested components
    if build_all or args.homepage:
        build_homepage(global_config, languages)

    if build_all or args.privacy:
        build_privacy(global_config, languages)

    if build_all or args.docs:
        build_docs(global_config, languages)

    if build_all or args.changelog:
        build_changelog_pages(global_config)

    print("\n" + "=" * 50)
    print("Build complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
