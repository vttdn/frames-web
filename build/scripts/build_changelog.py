#!/usr/bin/env python3
"""
Changelog Builder for Frames Website
Generates changelog pages from JSON config files with pagination support.
"""

import json
import math
import os
import sys
from pathlib import Path
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
import rjsmin
import htmlmin

# Get project root directory (go up from build/scripts/ to root)
PROJECT_ROOT = Path(__file__).parent.parent.parent
TEMPLATES_DIR = PROJECT_ROOT / "build" / "templates"
LOCALES_DIR = PROJECT_ROOT / "build" / "locales"
CHANGELOG_DIR = LOCALES_DIR / "changelog"

ENTRIES_PER_PAGE = 5

def load_changelog_css():
    """Load changelog CSS content for inlining"""
    changelog_css_path = PROJECT_ROOT / "lib" / "css" / "changelog.css"
    try:
        with open(changelog_css_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"⚠ Warning: changelog.css not found at {changelog_css_path}")
        print("  Please compile it first: sass lib/scss/changelog.scss lib/css/changelog.css --style compressed")
        return ""

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
            continue

    # Sort by release date (newest first)
    entries.sort(key=lambda x: x['release_date'], reverse=True)

    return entries

def format_date(iso_date, lang_code='en'):
    """Format ISO date to human-readable format based on language"""
    dt = datetime.fromisoformat(iso_date.replace('Z', '+00:00'))

    # Localized month abbreviations per language
    month_names = {
        'en': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'de': ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez'],
        'es': ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'],
        'fr': ['janv', 'févr', 'mars', 'avr', 'mai', 'juin', 'juil', 'août', 'sept', 'oct', 'nov', 'déc'],
        'it': ['gen', 'feb', 'mar', 'apr', 'mag', 'giu', 'lug', 'ago', 'set', 'ott', 'nov', 'dic'],
        'nl': ['jan', 'feb', 'mrt', 'apr', 'mei', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'dec'],
        'pt': ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'],
        'pl': ['sty', 'lut', 'mar', 'kwi', 'maj', 'cze', 'lip', 'sie', 'wrz', 'paź', 'lis', 'gru'],
        'sv': ['jan', 'feb', 'mars', 'apr', 'maj', 'juni', 'juli', 'aug', 'sep', 'okt', 'nov', 'dec'],
        'th': ['ม.ค.', 'ก.พ.', 'มี.ค.', 'เม.ย.', 'พ.ค.', 'มิ.ย.', 'ก.ค.', 'ส.ค.', 'ก.ย.', 'ต.ค.', 'พ.ย.', 'ธ.ค.'],
        'id': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'],
        'hi': ['जन', 'फ़र', 'मार्च', 'अप्रैल', 'मई', 'जून', 'जुल', 'अग', 'सित', 'अक्टू', 'नव', 'दिस'],
        'ru': ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек'],
        'uk': ['січ', 'лют', 'бер', 'кві', 'тра', 'чер', 'лип', 'сер', 'вер', 'жов', 'лис', 'гру'],
        'da': ['jan', 'feb', 'mar', 'apr', 'maj', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'dec'],
        'el': ['Ιαν', 'Φεβ', 'Μαρ', 'Απρ', 'Μαϊ', 'Ιουν', 'Ιουλ', 'Αυγ', 'Σεπ', 'Οκτ', 'Νοε', 'Δεκ'],
        'fi': ['tammi', 'helmi', 'maalis', 'huhti', 'touko', 'kesä', 'heinä', 'elo', 'syys', 'loka', 'marras', 'joulu'],
        'nb': ['jan', 'feb', 'mar', 'apr', 'mai', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'des'],
        'ro': ['ian', 'feb', 'mar', 'apr', 'mai', 'iun', 'iul', 'aug', 'sep', 'oct', 'nov', 'dec'],
        'tr': ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'],
        'vi': ['Thg 1', 'Thg 2', 'Thg 3', 'Thg 4', 'Thg 5', 'Thg 6', 'Thg 7', 'Thg 8', 'Thg 9', 'Thg 10', 'Thg 11', 'Thg 12'],
    }

    # Date format patterns per language
    date_formats = {
        'en': '{month} {day}, {year}',
        'de': '{day}. {month} {year}',
        'es': '{day} {month} {year}',
        'fr': '{day} {month} {year}',
        'it': '{day} {month} {year}',
        'nl': '{day} {month} {year}',
        'pt': '{day} {month} {year}',
        'pl': '{day} {month} {year}',
        'sv': '{day} {month} {year}',
        'ja': '{year}年{month}月{day}日',
        'ko': '{year}년 {month}월 {day}일',
        'zh': '{year}年{month}月{day}日',
        'zh-hant': '{year}年{month}月{day}日',
        'th': '{day} {month} {year}',
        'id': '{day} {month} {year}',
        'hi': '{day} {month} {year}',
        'ru': '{day} {month} {year}',
        'uk': '{day} {month} {year}',
        'da': '{day}. {month} {year}',
        'el': '{day} {month} {year}',
        'fi': '{day}. {month} {year}',
        'nb': '{day}. {month} {year}',
        'ro': '{day} {month} {year}',
        'tr': '{day} {month} {year}',
        'vi': '{day} {month} {year}',
    }

    # Get format for language, default to English
    date_format = date_formats.get(lang_code, '{month} {day}, {year}')

    # For Asian languages (ja, ko, zh, zh-hant), use zero-padded numeric month
    if lang_code in ['ja', 'ko', 'zh', 'zh-hant']:
        return date_format.format(
            year=dt.year,
            month=str(dt.month).zfill(2),
            day=str(dt.day).zfill(2)
        )

    # For other languages, use localized month names
    months = month_names.get(lang_code, month_names['en'])
    month_abbr = months[dt.month - 1]

    return date_format.format(
        year=dt.year,
        month=month_abbr,
        day=str(dt.day).zfill(2)
    )

def generate_language_list(languages):
    """Generate language list for dropdown"""
    lang_list = []
    for lang in languages:
        lang_list.append({
            'code': lang['code'],
            'name': lang['name'],
            'url': lang['path']
        })
    return lang_list

def get_current_build_date():
    """Get current date in ISO format for schema dateModified"""
    return datetime.now().strftime('%Y-%m-%dT%H:%M:%S+00:00')

def get_first_image_from_entry(entry):
    """Extract the first image from an entry's sections"""
    if 'sections' not in entry:
        return None, None, None

    for section in entry['sections']:
        if section.get('type') == 'media' and 'image' in section:
            return (
                section['image'],
                section.get('width', '400'),
                section.get('height', '300')
            )
    return None, None, None

def generate_schema(template_name, context):
    """Generate JSON-LD schema from template"""
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True
    )

    template = env.get_template(template_name)
    return template.render(context)

def generate_hreflang_links(languages, page_type='index', page_number=1, url_slug=None, base_url="https://withframes.com"):
    """Generate hreflang alternate links for changelog pages"""
    links = []
    for lang in languages:
        # Build the URL based on page type
        if page_type == 'index':
            # Changelog index page
            if lang['code'] == 'en':
                url_path = '/changelog/'
            else:
                url_path = f"/{lang['code']}/changelog/"

            # Add pagination if not first page
            if page_number > 1:
                url_path = url_path.rstrip('/') + f"/page-{page_number}/"

        elif page_type == 'entry':
            # Individual changelog entry
            if lang['code'] == 'en':
                url_path = f'/changelog/{url_slug}/'
            else:
                url_path = f"/{lang['code']}/changelog/{url_slug}/"

        url = f"{base_url}{url_path}"
        links.append({
            'hreflang': lang['hreflang'],
            'href': url
        })

    # Add x-default (always points to English version)
    if page_type == 'index':
        x_default_path = '/changelog/' if page_number == 1 else f'/changelog/page-{page_number}/'
    else:
        x_default_path = f'/changelog/{url_slug}/'

    links.append({
        'hreflang': 'x-default',
        'href': base_url + x_default_path
    })

    return links

def save_schema(schema_json, schema_name, lang_code, page_type='page', page_number=None, url_slug=None):
    """Save generated JSON-LD schema to appropriate location"""
    # Create language-specific schema directory
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

    # Write schema file
    schema_path = schema_dir / schema_name
    with open(schema_path, 'w', encoding='utf-8') as f:
        f.write(schema_json)

def generate_changelog_index(lang_code, global_config, locale_data, entries, page_number, total_pages, available_languages, all_entries, changelog_css):
    """Generate changelog index page with pagination"""

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

    # Add formatted dates to entries and process language-specific image paths
    for entry in entries:
        entry['formatted_date'] = format_date(entry['release_date'], lang_code)
        # Process sections to replace {{ lang }} in image paths
        if 'sections' in entry:
            for section in entry['sections']:
                if section.get('type') == 'media':
                    if 'image' in section and '{{ lang }}' in section['image']:
                        section['image'] = section['image'].replace('{{ lang }}', lang_code)
                    if 'image_2x' in section and '{{ lang }}' in section['image_2x']:
                        section['image_2x'] = section['image_2x'].replace('{{ lang }}', lang_code)

    # Generate and save JSON-LD schemas
    build_date = get_current_build_date()
    canonical_url = f"https://withframes.com{'/' + lang_code if lang_code != 'en' else ''}/changelog/"
    if page_number > 1:
        canonical_url += f"page-{page_number}/"

    # Blog schema (only on first page)
    if page_number == 1:
        blog_context = {
            'lang': lang_code,
            'canonical_url': canonical_url.rstrip('/') + '/',
            'page_title': locale_data['changelog']['meta']['title'],
            'page_description': locale_data['changelog']['meta']['description'],
            'entries': all_entries,  # Use all entries for the blog schema
            'build_date': build_date
        }
        blog_schema = generate_schema('blog.json', blog_context)
        save_schema(blog_schema, 'blog.json', lang_code, 'changelog-index', page_number)

    # Breadcrumb schema
    breadcrumb_context = {
        'lang': lang_code,
        'changelog_heading': locale_data['changelog']['heading'],
        'canonical_url': canonical_url.rstrip('/') + '/',
        'entry_title': None,
        'page_number': page_number if page_number > 1 else None
    }
    breadcrumb_schema = generate_schema('breadcrumb.json', breadcrumb_context)
    save_schema(breadcrumb_schema, 'breadcrumb.json', lang_code, 'changelog-index', page_number)

    # Organization schema
    org_context = {
        'global_urls': global_config['urls'],
        'appstore_url': locale_data['urls']['appstore_ios'],
        'macappstore_url': locale_data['urls']['appstore_macos'],
        'company_description': locale_data['company']['description']
    }
    organization_schema = generate_schema('organization.json', org_context)
    save_schema(organization_schema, 'organization.json', lang_code, 'changelog-index', page_number)

    # Prepare template context
    context = {
        'lang': lang_code,
        'locale_data': locale_data,
        'global_config': global_config,
        'lang_config': lang_config,
        'hreflang_links': generate_hreflang_links(global_config['languages'], page_type='index', page_number=page_number),
        'all_languages': generate_language_list(global_config['languages']),
        'available_changelog_languages': available_languages,
        'entries': entries,
        'page_number': page_number,
        'total_pages': total_pages,
        'changelog_css': changelog_css
    }

    # Load and render template
    template = env.get_template('changelog-index.html')
    html = template.render(context)

    return html

def generate_changelog_entry(lang_code, global_config, locale_data, entry, prev_entry, next_entry, available_languages, changelog_css):
    """Generate individual changelog entry page"""

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

    # Add formatted date to entry and process language-specific image paths
    entry['formatted_date'] = format_date(entry['release_date'], lang_code)
    if 'sections' in entry:
        for section in entry['sections']:
            if section.get('type') == 'media':
                if 'image' in section and '{{ lang }}' in section['image']:
                    section['image'] = section['image'].replace('{{ lang }}', lang_code)
                if 'image_2x' in section and '{{ lang }}' in section['image_2x']:
                    section['image_2x'] = section['image_2x'].replace('{{ lang }}', lang_code)

    if prev_entry:
        prev_entry['formatted_date'] = format_date(prev_entry['release_date'], lang_code)
    if next_entry:
        next_entry['formatted_date'] = format_date(next_entry['release_date'], lang_code)

    # Generate and save JSON-LD schemas
    build_date = get_current_build_date()
    canonical_url = f"https://withframes.com{'/' + lang_code if lang_code != 'en' else ''}/changelog/{entry['url_slug']}/"

    # Get first image from entry
    first_image, image_width, image_height = get_first_image_from_entry(entry)

    # BlogPosting schema
    blogposting_context = {
        'lang': lang_code,
        'canonical_url': canonical_url,
        'entry': entry,
        'build_date': build_date,
        'first_image': first_image,
        'image_width': image_width,
        'image_height': image_height
    }
    blogposting_schema = generate_schema('blogposting.json', blogposting_context)
    save_schema(blogposting_schema, 'blogposting.json', lang_code, 'changelog-entry', url_slug=entry['url_slug'])

    # Breadcrumb schema
    breadcrumb_context = {
        'lang': lang_code,
        'changelog_heading': locale_data['changelog']['heading'],
        'canonical_url': canonical_url,
        'entry_title': entry['title']
    }
    breadcrumb_schema = generate_schema('breadcrumb.json', breadcrumb_context)
    save_schema(breadcrumb_schema, 'breadcrumb.json', lang_code, 'changelog-entry', url_slug=entry['url_slug'])

    # Organization schema
    org_context = {
        'global_urls': global_config['urls'],
        'appstore_url': locale_data['urls']['appstore_ios'],
        'macappstore_url': locale_data['urls']['appstore_macos'],
        'company_description': locale_data['company']['description']
    }
    organization_schema = generate_schema('organization.json', org_context)
    save_schema(organization_schema, 'organization.json', lang_code, 'changelog-entry', url_slug=entry['url_slug'])

    # Prepare template context
    context = {
        'lang': lang_code,
        'locale_data': locale_data,
        'global_config': global_config,
        'lang_config': lang_config,
        'hreflang_links': generate_hreflang_links(global_config['languages'], page_type='entry', url_slug=entry['url_slug']),
        'all_languages': generate_language_list(global_config['languages']),
        'available_changelog_languages': available_languages,
        'entry': entry,
        'prev_entry': prev_entry,
        'next_entry': next_entry,
        'changelog_css': changelog_css
    }

    # Load and render template
    template = env.get_template('changelog-entry.html')
    html = template.render(context)

    return html

def save_changelog_index(html, page_number, lang_code='en'):
    """Save changelog index page"""
    # Determine output directory based on language
    if lang_code == 'en':
        output_base = PROJECT_ROOT / "changelog"
        path_prefix = "changelog"
    else:
        output_base = PROJECT_ROOT / lang_code / "changelog"
        path_prefix = f"{lang_code}/changelog"

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

def minify_html(html_code: str) -> str:
    return htmlmin.minify(
        html_code,
        remove_comments=True,
        remove_empty_space=True,
        reduce_boolean_attributes=True,
        remove_optional_attribute_quotes=True,
        keep_pre=True,
        pre_tags=('pre', 'code', 'textarea'),
    )


        
def minify_javascript(js_code: str) -> str:
    """Minify JavaScript and strip comments."""
    return rjsmin.jsmin(js_code)

def save_changelog_entry(html, entry, lang_code='en'):
    """Save individual changelog entry page"""
    # Determine output directory based on language
    if lang_code == 'en':
        output_base = PROJECT_ROOT / "changelog"
        path_prefix = "changelog"
    else:
        output_base = PROJECT_ROOT / lang_code / "changelog"
        path_prefix = f"{lang_code}/changelog"

    output_dir = output_base / entry['url_slug']
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "index.html"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✓ Generated: {path_prefix}/{entry['url_slug']}/index.html")

def generate_changelog_javascript(lang_code, locale_data, global_config):
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True
    )

    # Get lang_config for this language
    lang_config = next((l for l in global_config['languages'] if l['code'] == lang_code), None)
    if not lang_config:
        raise ValueError(f"Language {lang_code} not found in global config")

    context = {
        'lang': lang_code,
        'locale_data': locale_data,
        'global_config': global_config,
        'lang_config': lang_config  # ← ADD THIS
    }

    template = env.get_template('changelog.js')
    javascript = template.render(context)

    return minify_javascript(javascript)



def save_changelog_javascript(javascript, lang_code='en'):
    """Save generated JavaScript to appropriate location"""
    # Create language-specific js directory for changelog
    if lang_code == 'en':
        js_dir = PROJECT_ROOT / "lib" / "js" / "changelog"
    else:
        js_dir = PROJECT_ROOT / "lib" / "js" / lang_code / "changelog"

    js_dir.mkdir(parents=True, exist_ok=True)

    # Write JavaScript file
    js_path = js_dir / "core.js"
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(javascript)

    if lang_code == 'en':
        print(f"✓ Generated: lib/js/changelog/core.js")
    else:
        print(f"✓ Generated: lib/js/{lang_code}/changelog/core.js")

def generate_sitemap(entries, lang_code='en'):
    """Generate changelog-specific sitemap"""
    sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    base_url = "https://withframes.com"

    # Get current date for lastmod
    current_date = datetime.now().strftime('%Y-%m-%d')

    # URL path prefix based on language
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
        # Use current build date as lastmod
        sitemap_lines.append(f'    <lastmod>{current_date}</lastmod>')
        sitemap_lines.append('    <changefreq>monthly</changefreq>')
        sitemap_lines.append('    <priority>0.6</priority>')
        sitemap_lines.append('  </url>')

    sitemap_lines.append('</urlset>')

    sitemap_content = '\n'.join(sitemap_lines)

    # Save sitemap
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

    # Add each language's changelog sitemap
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

    # Save to root directory
    sitemap_path = PROJECT_ROOT / "sitemap-changelog.xml"
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

    print(f"✓ Generated: sitemap-changelog.xml")

    return sitemap_path

def main():
    """Main generation function"""
    print("Changelog Builder for Frames")
    print("=" * 50)

    # Load global config
    try:
        global_config = load_global_config()
        print(f"✓ Loaded global config")
    except FileNotFoundError:
        print("✗ Error: global.json not found in build/locales/")
        sys.exit(1)

    # Load changelog CSS for inlining
    changelog_css = load_changelog_css()
    if changelog_css:
        print(f"✓ Loaded changelog CSS ({len(changelog_css)} bytes)")
    else:
        print("⚠ No changelog CSS loaded - templates will use fallback")

    # Detect which languages have changelog translations
    available_languages = []
    for lang_dir in CHANGELOG_DIR.iterdir():
        if lang_dir.is_dir() and (lang_dir / "1.0.0-ios.json").exists():
            available_languages.append(lang_dir.name)

    print(f"✓ Detected {len(available_languages)} languages with changelog translations: {', '.join(sorted(available_languages))}")

    # Generate changelogs only for languages with translations
    languages_to_generate = available_languages

    for lang_code in languages_to_generate:
        print(f"\n--- Generating changelog for {lang_code} ---")

        try:
            # Load locale data
            locale_data = load_locale(lang_code)
            print(f"✓ Loaded locale: {lang_code}")

            # Load all changelog entries
            entries = load_changelog_entries(lang_code)

            if not entries:
                print(f"⚠ No changelog entries found for {lang_code}")
                continue

            print(f"✓ Loaded {len(entries)} changelog entries")

            # Calculate pagination
            total_pages = math.ceil(len(entries) / ENTRIES_PER_PAGE)
            print(f"✓ Total pages: {total_pages}")

            # Generate index pages with pagination
            for page in range(1, total_pages + 1):
                start_idx = (page - 1) * ENTRIES_PER_PAGE
                end_idx = start_idx + ENTRIES_PER_PAGE
                page_entries = entries[start_idx:end_idx]

                html = generate_changelog_index(
                    lang_code,
                    global_config,
                    locale_data,
                    page_entries,
                    page,
                    total_pages,
                    available_languages,
                    entries,  # Pass all entries for Blog schema
                    changelog_css
                )
                html = minify_html(html)
                save_changelog_index(html, page, lang_code)

            # Generate individual entry pages with prev/next navigation
            for i, entry in enumerate(entries):
                prev_entry = entries[i - 1] if i > 0 else None
                next_entry = entries[i + 1] if i < len(entries) - 1 else None

                html = generate_changelog_entry(
                    lang_code,
                    global_config,
                    locale_data,
                    entry,
                    prev_entry,
                    next_entry,
                    available_languages,
                    changelog_css
                )
                html = minify_html(html)
                save_changelog_entry(html, entry, lang_code)

            # Generate sitemap
            generate_sitemap(entries, lang_code)

            # Generate and save JavaScript
            javascript = generate_changelog_javascript(lang_code, locale_data, global_config)
            save_changelog_javascript(javascript, lang_code)

        except FileNotFoundError:
            print(f"✗ Warning: {lang_code}.json not found, skipping...")
        except Exception as e:
            print(f"✗ Error generating changelog for {lang_code}: {e}")
            import traceback
            traceback.print_exc()

    # Generate changelog sitemap index
    print("\nGenerating changelog sitemap index...")
    generate_changelog_sitemap_index(available_languages)

    print("\n" + "=" * 50)
    print("Changelog generation complete!")

if __name__ == "__main__":
    main()
