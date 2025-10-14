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
import rjsmin
import htmlmin

# Get project root directory (go up from build/scripts/ to root)
PROJECT_ROOT = Path(__file__).parent.parent.parent
TEMPLATES_DIR = PROJECT_ROOT / "build" / "templates"
LOCALES_DIR = PROJECT_ROOT / "build" / "locales"
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

def load_privacy_css():
    """Load privacy CSS content for inlining"""
    privacy_css_path = PROJECT_ROOT / "lib" / "css" / "privacy.css"
    try:
        with open(privacy_css_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"⚠ Warning: privacy.css not found at {privacy_css_path}")
        print("  Please compile it first: sass lib/scss/privacy.scss lib/css/privacy.css --style compressed")
        return ""

def generate_hreflang_links(languages, base_url="https://withframes.com", page="home"):
    """Generate hreflang alternate links for homepage or privacy page"""
    links = []

    for lang in languages:
        try:
            locale_data = load_locale(lang['code'])

            # Determine which path to use
            page_path = locale_data['urls']['privacy'] if page == "privacy" else ''

            # Clean up slashes before building
            lang_path = lang['path'].strip('/')
            page_path = page_path.strip('/')

            if not lang_path:
                # Default language (no lang subdirectory)
                url = f"{base_url}/{page_path}" if page_path else base_url
            else:
                url = f"{base_url}/{lang_path}"
                if page_path:
                    url += f"/{page_path}"

            # Ensure trailing slash
            if not url.endswith('/'):
                url += '/'

            links.append({
                'hreflang': lang['hreflang'],
                'href': url
            })

        except FileNotFoundError:
            continue

    return links


    # Add x-default link
    if page == "privacy":
        x_default = f"{base_url}/privacy/"
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
        # Load locale to get privacy path
        try:
            locale_data = load_locale(lang['code'])
            privacy_path = locale_data['urls']['privacy']
        except:
            privacy_path = 'privacy/'

        # Use relative paths for language dropdown
        lang_list.append({
            'code': lang['code'],
            'name': lang['name'],
            'url': lang['path'],
            'privacy_path': privacy_path
        })
    return lang_list

def detect_available_changelog_languages():
    """Detect which languages have changelog translations"""
    changelog_dir = LOCALES_DIR / "changelog"
    available_languages = []

    if not changelog_dir.exists():
        return available_languages

    for lang_dir in changelog_dir.iterdir():
        if lang_dir.is_dir() and (lang_dir / "1.0.0-ios.json").exists():
            available_languages.append(lang_dir.name)

    return available_languages

def minify_html(html_code: str) -> str:
    """Minify HTML: remove whitespace, comments, etc."""
    return htmlmin.minify(
        html_code,
        remove_comments=True,
        remove_empty_space=True,
        reduce_boolean_attributes=True,
        remove_optional_attribute_quotes=False
    )

def generate_html(lang_code, global_config, locale_data, critical_css, available_changelog_languages):
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
        'hreflang_links': generate_hreflang_links(global_config['languages'], page="home"),
        'all_languages': generate_language_list(global_config['languages']),
        'available_changelog_languages': available_changelog_languages,
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
        'currency': locale_data['pricing']['currency'].rstrip('/'),
        'monthly_price': locale_data['pricing']['ios']['price_value_monthly'],
        'yearly_price': locale_data['pricing']['ios']['price_value_yearly'],
        'monthly_label': locale_data['pricing']['label_subscription_monthly'],
        'yearly_label': locale_data['pricing']['label_subscription_yearly'],
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
    for i in range(1, 8):
        review_key = f'review{i}'
        if review_key in locale_data['reviews']:
            context[f'review{i}_author'] = locale_data['reviews'][review_key]['author_name']
            context[f'review{i}_date'] = locale_data['reviews'][review_key]['datetime']
            context[f'review{i}_title'] = f'Review by {locale_data["reviews"][review_key]["author_name"]}'
            context[f'review{i}_descr'] = locale_data['reviews'][review_key]['quote']
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

def generate_privacy_html(lang_code, global_config, locale_data, privacy_css, available_changelog_languages):
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
        'hreflang_links': generate_hreflang_links(global_config['languages'], page="privacy"),
        'all_languages': generate_language_list(global_config['languages']),
        'available_changelog_languages': available_changelog_languages,
        'privacy_css': privacy_css
    }

    # Load and render template
    template = env.get_template('privacy.html')
    html = template.render(context)

    return html

def save_html(html, lang_config, locale_data=None, page_type='index', minify=True):
    """Save generated HTML to appropriate location"""
    
    # Minify HTML if needed
    if minify:
        html = minify_html(html)

    # Determine output path
    if page_type == 'index':
        if lang_config['path'] == '/':
            output_path = OUTPUT_DIR / "index.html"
        else:
            path_parts = lang_config['path'].strip('/').split('/')
            output_dir = OUTPUT_DIR / '/'.join(path_parts)
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / "index.html"
    elif page_type == 'privacy':
        privacy_path = locale_data['urls']['privacy'].strip('/')
        if lang_config['path'] == '/':
            output_dir = OUTPUT_DIR / privacy_path
        else:
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

def minify_javascript(js_code: str) -> str:
    """Minify JavaScript and strip comments."""
    return rjsmin.jsmin(js_code)
    
def generate_javascript(lang_code, locale_data, global_config):
    """Generate JavaScript file for a specific language"""

    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True
    )

    # Get language config
    lang_config = next((l for l in global_config['languages'] if l['code'] == lang_code), None)
    if not lang_config:
        raise ValueError(f"Language {lang_code} not found in global config")

    # Prepare context
    context = {
        'lang': lang_code,
        'locale_data': locale_data,
        'global_config': global_config,
        'lang_config': lang_config  # ← ADD THIS
    }

    # Load and render template
    template = env.get_template('core.js')
    javascript = template.render(context)

    return javascript


import rjsmin

def save_javascript(javascript, lang_code, minify=True):
    """Save generated JavaScript to appropriate location"""
    # Optionally minify JS
    if minify:
        javascript = rjsmin.jsmin(javascript)

    # Create language-specific js directory
    js_dir = PROJECT_ROOT / "lib" / "js" / lang_code
    js_dir.mkdir(parents=True, exist_ok=True)

    # Write JavaScript file
    js_path = js_dir / "core.js"
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(javascript)

    print(f"✓ Generated: {js_path.relative_to(OUTPUT_DIR)}")

def generate_privacy_javascript(lang_code, locale_data, global_config):
    """Generate JavaScript file for privacy page"""

    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True
    )

    # Get language config
    lang_config = next((l for l in global_config['languages'] if l['code'] == lang_code), None)
    if not lang_config:
        raise ValueError(f"Language {lang_code} not found in global config")

    context = {
        'lang': lang_code,
        'locale_data': locale_data,
        'global_config': global_config,
        'lang_config': lang_config  # ← ADD THIS
    }

    template = env.get_template('privacy.js')
    javascript = template.render(context)

    return javascript



def save_privacy_javascript(javascript, lang_code):
    """Save generated privacy JavaScript to appropriate location"""
    # Create language-specific js directory
    if lang_code == 'en':
        js_dir = PROJECT_ROOT / "lib" / "js"
    else:
        js_dir = PROJECT_ROOT / "lib" / "js" / lang_code
    js_dir.mkdir(parents=True, exist_ok=True)

    # Write JavaScript file
    js_path = js_dir / "privacy.js"
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(javascript)

    print(f"✓ Generated: {js_path.relative_to(OUTPUT_DIR)}")

def generate_home_sitemap(languages):
    """Generate sitemap for all homepage URLs"""
    from datetime import datetime

    sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    base_url = "https://withframes.com"
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Add each language's homepage
    for lang in languages:
        if lang['code'] == 'en':
            url = f"{base_url}/"
            priority = "1.0"
        else:
            url = f"{base_url}{lang['path']}"
            priority = "0.9"

        sitemap_lines.append('  <url>')
        sitemap_lines.append(f'    <loc>{url}</loc>')
        sitemap_lines.append(f'    <lastmod>{current_date}</lastmod>')
        sitemap_lines.append('    <changefreq>weekly</changefreq>')
        sitemap_lines.append(f'    <priority>{priority}</priority>')
        sitemap_lines.append('  </url>')

    sitemap_lines.append('</urlset>')

    sitemap_content = '\n'.join(sitemap_lines)

    # Save to root directory
    sitemap_path = PROJECT_ROOT / "sitemap-home.xml"
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

    print(f"✓ Generated: sitemap-home.xml")
    return sitemap_path

def generate_privacy_sitemap(languages):
    """Generate sitemap for all privacy page URLs"""
    from datetime import datetime

    sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    base_url = "https://withframes.com"
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Add each language's privacy page
    for lang in languages:
        # Load locale to get privacy URL
        try:
            locale_data = load_locale(lang['code'])
            privacy_url = locale_data['urls']['privacy']

            # Ensure URL starts with /
            if not privacy_url.startswith('/'):
                privacy_url = '/' + privacy_url

            if lang['code'] == 'en':
                url = f"{base_url}/{privacy_url.lstrip('/')}"
                priority = "0.8"
            else:
                url = f"{base_url}/{lang['code']}/{privacy_url.lstrip('/')}"
                priority = "0.7"

            sitemap_lines.append('  <url>')
            sitemap_lines.append(f'    <loc>{url}</loc>')
            sitemap_lines.append(f'    <lastmod>{current_date}</lastmod>')
            sitemap_lines.append('    <changefreq>yearly</changefreq>')
            sitemap_lines.append(f'    <priority>{priority}</priority>')
            sitemap_lines.append('  </url>')
        except FileNotFoundError:
            continue

    sitemap_lines.append('</urlset>')

    sitemap_content = '\n'.join(sitemap_lines)

    # Save to root directory
    sitemap_path = PROJECT_ROOT / "sitemap-privacy.xml"
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

    print(f"✓ Generated: sitemap-privacy.xml")
    return sitemap_path

def main():
    """Main generation function"""
    print("Frames Website Generator")
    print("=" * 50)

    # Load global config
    try:
        global_config = load_global_config()
        print(f"✓ Loaded global config")
    except FileNotFoundError:
        print("✗ Error: global.json not found in build/locales/")
        sys.exit(1)

    # Detect available changelog languages
    available_changelog_languages = detect_available_changelog_languages()
    print(f"✓ Detected {len(available_changelog_languages)} languages with changelog translations: {', '.join(sorted(available_changelog_languages))}")

    # Load critical CSS for inlining
    critical_css = load_critical_css()
    if critical_css:
        print(f"✓ Loaded critical CSS ({len(critical_css)} bytes)")
    else:
        print("⚠ No critical CSS loaded - templates will use fallback")

    # Load privacy CSS for inlining
    privacy_css = load_privacy_css()
    if privacy_css:
        print(f"✓ Loaded privacy CSS ({len(privacy_css)} bytes)")
    else:
        print("⚠ No privacy CSS loaded - templates will use fallback")

    # Generate for each language
    for lang in global_config['languages']:
        lang_code = lang['code']

        try:
            # Load locale data
            locale_data = load_locale(lang_code)
            print(f"✓ Loaded locale: {lang_code}")

            # Generate index HTML
            html = generate_html(lang_code, global_config, locale_data, critical_css, available_changelog_languages)
            save_html(html, lang, locale_data, 'index')

            # Generate privacy HTML
            privacy_html = generate_privacy_html(lang_code, global_config, locale_data, privacy_css, available_changelog_languages)
            save_html(privacy_html, lang, locale_data, 'privacy')

            # Generate and save JSON-LD schemas
            for schema_template in ['frames.json', 'faq.json']:
                schema_json = generate_schema(schema_template, lang_code, global_config, locale_data)
                save_schema(schema_json, schema_template, lang_code)

            # Generate Organization, SoftwareCompany and WebPage schemas for homepage and privacy
            organization_context = {
                'global_urls': global_config['urls'],
                'appstore_url': locale_data['urls']['appstore_ios'],
                'macappstore_url': locale_data['urls']['appstore_macos'],
                'company_description': locale_data['company']['description']
            }
            org_env = Environment(
                loader=FileSystemLoader(TEMPLATES_DIR),
                autoescape=False,
                trim_blocks=True,
                lstrip_blocks=True
            )
            org_template = org_env.get_template('organization.json')
            organization_json = org_template.render(organization_context)
            save_schema(organization_json, 'organization.json', lang_code)

            # WebPage schema for homepage
            homepage_webpage_context = {
                'lang': lang_code,
                'canonical_url': locale_data['meta']['canonical_url'].rstrip('/') + '/',
                'seo_meta_title': locale_data['meta']['title'],
                'seo_meta_description': locale_data['meta']['description']
            }
            webpage_template = org_env.get_template('webpage.json')
            homepage_webpage_json = webpage_template.render(homepage_webpage_context)
            save_schema(homepage_webpage_json, 'webpage-homepage.json', lang_code)

            # WebPage schema for privacy page
            privacy_webpage_context = {
                'lang': lang_code,
                'canonical_url': locale_data['privacy']['meta']['canonical_url'].rstrip('/') + '/',
                'seo_meta_title': locale_data['privacy']['meta']['title'],
                'seo_meta_description': locale_data['privacy']['meta']['description']
            }
            privacy_webpage_json = webpage_template.render(privacy_webpage_context)
            save_schema(privacy_webpage_json, 'webpage-privacy.json', lang_code)

            # Generate and save JavaScript
            javascript = generate_javascript(lang_code, locale_data, global_config)
            save_javascript(javascript, lang_code)

            # Generate and save privacy page JavaScript
            privacy_javascript = generate_privacy_javascript(lang_code, locale_data, global_config)
            save_privacy_javascript(privacy_javascript, lang_code)

        except FileNotFoundError:
            print(f"✗ Warning: {lang_code}.json not found, skipping...")
            continue
        except Exception as e:
            print(f"✗ Error generating {lang_code}: {e}")
            continue

    # Generate sitemaps
    print("\nGenerating sitemaps...")
    generate_home_sitemap(global_config['languages'])
    generate_privacy_sitemap(global_config['languages'])

    print("=" * 50)
    print("Generation complete!")

if __name__ == "__main__":
    main()
