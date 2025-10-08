#!/usr/bin/env python3
"""
Frames Website Generator
Generates localized HTML files from templates and locale JSON files.
"""

import json
import os
import sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Get project root directory
PROJECT_ROOT = Path(__file__).parent.parent
TEMPLATES_DIR = PROJECT_ROOT / "templates"
LOCALES_DIR = PROJECT_ROOT / "locales"
OUTPUT_DIR = PROJECT_ROOT
SCHEMA_OUTPUT_DIR = PROJECT_ROOT / "lib" / "schema"

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

def load_critical_css():
    """Load critical CSS content for inlining"""
    critical_css_path = PROJECT_ROOT / "lib" / "css" / "critical.css"
    try:
        with open(critical_css_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"⚠ Warning: critical.css not found at {critical_css_path}")
        print("  Please compile it first: sass lib/scss/critical.scss lib/css/critical.css --style compressed")
        return ""

def generate_hreflang_links(languages, base_url="https://withframes.com"):
    """Generate hreflang alternate links"""
    links = []
    for lang in languages:
        url = f"{base_url}{lang['path']}" if lang['path'] != '/' else base_url + '/'
        links.append({
            'hreflang': lang['hreflang'],
            'href': url
        })
    # Add x-default
    links.append({
        'hreflang': 'x-default',
        'href': base_url + '/'
    })
    return links

def generate_language_list(languages):
    """Generate language list for dropdown"""
    lang_list = []
    for lang in languages:
        # Use relative paths for language dropdown
        lang_list.append({
            'code': lang['code'],
            'name': lang['name'],
            'url': lang['path']
        })
    return lang_list

def generate_html(lang_code, global_config, locale_data, critical_css):
    """Generate HTML for a specific language"""

    # Setup Jinja2 environment
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks=True,
        lstrip_blocks=True
    )

    # Get language config
    lang_config = next((l for l in global_config['languages'] if l['code'] == lang_code), None)
    if not lang_config:
        raise ValueError(f"Language {lang_code} not found in global config")

    # Prepare template context
    context = {
        'lang': lang_code,
        'locale_data': locale_data,
        'global_config': global_config,
        'lang_config': lang_config,
        'hreflang_links': generate_hreflang_links(global_config['languages']),
        'all_languages': generate_language_list(global_config['languages']),
        'critical_css': critical_css
    }

    # Load and render template
    template = env.get_template('index.html')
    html = template.render(context)

    return html

def generate_schema(template_name, lang_code, global_config, locale_data):
    """Generate JSON-LD schema for a specific language"""

    # Setup Jinja2 environment
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=False,  # Don't escape JSON
        trim_blocks=True,
        lstrip_blocks=True
    )

    # Prepare context with flattened data for easier template access
    context = {
        'lang': lang_code,
        'canonical_url': locale_data['meta']['canonical_url'].rstrip('/'),
        'ios_appname': locale_data['footer']['product']['frames_ios'],
        'mac_appname': locale_data['footer']['product']['frames_macos'],
        'seo_meta_title': locale_data['meta']['title'],
        'seo_meta_description': locale_data['meta']['description'],
        'seo_meta_keywords': 'film photography app, analog photography, EXIF metadata, film camera notes, photography workflow, film photography organization',
        'appstore_url': locale_data['urls']['appstore_ios'],
        'macappstore_url': locale_data['urls']['appstore_macos'],
        'video_title': locale_data['video']['title'],
        'video_description': locale_data['video']['description'],
        'global_urls': global_config['urls'],
        'app_version_ios': global_config['app_version_ios'],
        'app_version_macos': global_config['app_version_macos']
    }

    # Add review data
    for i in range(1, 6):
        review_key = f'review{i}'
        if review_key in locale_data['reviews']:
            context[f'review{i}_author'] = locale_data['reviews'][review_key]['author_name']
            context[f'review{i}_date'] = locale_data['reviews'][review_key]['datetime']
            context[f'review{i}_title'] = f'Review by {locale_data["reviews"][review_key]["author_name"]}'
            context[f'review{i}_descr'] = locale_data['reviews'][review_key]['quote']
            context[f'review{i}_rating'] = '5'

    # Add additional placeholder reviews (6-7) with same data as review 1-2
    for i in range(6, 8):
        source_idx = ((i - 1) % 5) + 1
        context[f'review{i}_author'] = context[f'review{source_idx}_author']
        context[f'review{i}_date'] = context[f'review{source_idx}_date']
        context[f'review{i}_title'] = context[f'review{source_idx}_title']
        context[f'review{i}_descr'] = context[f'review{source_idx}_descr']
        context[f'review{i}_rating'] = '5'

    # Add FAQ data
    for i in range(1, 7):
        question_key = f'question{i}'
        if question_key in locale_data['qa']:
            context[f'faq_question{i}'] = locale_data['qa'][question_key]['question']
            context[f'faq_answer{i}'] = locale_data['qa'][question_key]['answer']

    # Load and render template
    template = env.get_template(template_name)
    schema_json = template.render(context)

    return schema_json

def generate_privacy_html(lang_code, global_config, locale_data, critical_css):
    """Generate privacy page HTML for a specific language"""

    # Setup Jinja2 environment
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks=True,
        lstrip_blocks=True
    )

    # Get language config
    lang_config = next((l for l in global_config['languages'] if l['code'] == lang_code), None)
    if not lang_config:
        raise ValueError(f"Language {lang_code} not found in global config")

    # Prepare template context
    context = {
        'lang': lang_code,
        'locale_data': locale_data,
        'global_config': global_config,
        'lang_config': lang_config,
        'hreflang_links': generate_hreflang_links(global_config['languages']),
        'all_languages': generate_language_list(global_config['languages']),
        'critical_css': critical_css
    }

    # Load and render template
    template = env.get_template('privacy.html')
    html = template.render(context)

    return html

def save_html(html, lang_config, locale_data=None, page_type='index'):
    """Save generated HTML to appropriate location"""
    # Determine output path
    if page_type == 'index':
        if lang_config['path'] == '/':
            output_path = OUTPUT_DIR / "index.html"
        else:
            # Remove leading/trailing slashes and create directory
            path_parts = lang_config['path'].strip('/').split('/')
            output_dir = OUTPUT_DIR / '/'.join(path_parts)
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / "index.html"
    elif page_type == 'privacy':
        # Get privacy path from locale data
        privacy_path = locale_data['urls']['privacy'].strip('/')
        if lang_config['path'] == '/':
            output_dir = OUTPUT_DIR / privacy_path
        else:
            # Combine language path with privacy path
            lang_path = lang_config['path'].strip('/')
            output_dir = OUTPUT_DIR / lang_path / privacy_path
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "index.html"

    # Write HTML file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✓ Generated: {output_path.relative_to(OUTPUT_DIR)}")

def save_schema(schema_json, schema_name, lang_code):
    """Save generated JSON-LD schema to appropriate location"""
    # Create language-specific schema directory
    schema_dir = SCHEMA_OUTPUT_DIR / lang_code
    schema_dir.mkdir(parents=True, exist_ok=True)

    # Write schema file
    schema_path = schema_dir / schema_name
    with open(schema_path, 'w', encoding='utf-8') as f:
        f.write(schema_json)

    print(f"✓ Generated: {schema_path.relative_to(OUTPUT_DIR)}")

def main():
    """Main generation function"""
    print("Frames Website Generator")
    print("=" * 50)

    # Load global config
    try:
        global_config = load_global_config()
        print(f"✓ Loaded global config")
    except FileNotFoundError:
        print("✗ Error: global.json not found in locales/")
        sys.exit(1)

    # Load critical CSS for inlining
    critical_css = load_critical_css()
    if critical_css:
        print(f"✓ Loaded critical CSS ({len(critical_css)} bytes)")
    else:
        print("⚠ No critical CSS loaded - templates will use fallback")

    # Generate for each language
    for lang in global_config['languages']:
        lang_code = lang['code']

        try:
            # Load locale data
            locale_data = load_locale(lang_code)
            print(f"✓ Loaded locale: {lang_code}")

            # Generate index HTML
            html = generate_html(lang_code, global_config, locale_data, critical_css)
            save_html(html, lang, locale_data, 'index')

            # Generate privacy HTML
            privacy_html = generate_privacy_html(lang_code, global_config, locale_data, critical_css)
            save_html(privacy_html, lang, locale_data, 'privacy')

            # Generate and save JSON-LD schemas
            for schema_template in ['frames.json', 'faq.json']:
                schema_json = generate_schema(schema_template, lang_code, global_config, locale_data)
                save_schema(schema_json, schema_template, lang_code)

        except FileNotFoundError:
            print(f"✗ Warning: {lang_code}.json not found, skipping...")
            continue
        except Exception as e:
            print(f"✗ Error generating {lang_code}: {e}")
            continue

    print("=" * 50)
    print("Generation complete!")

if __name__ == "__main__":
    main()
