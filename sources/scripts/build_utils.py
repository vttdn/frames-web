#!/usr/bin/env python3
"""
Shared utilities for Frames Website Build System
Contains common functions used across all build scripts.
"""

import json
from pathlib import Path
import htmlmin
import rjsmin


# Project paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
TEMPLATES_DIR = PROJECT_ROOT / "build" / "templates"
LOCALES_DIR = PROJECT_ROOT / "build" / "locales"
OUTPUT_DIR = PROJECT_ROOT
SCHEMA_OUTPUT_DIR = PROJECT_ROOT / "lib" / "schema"


def load_json(filepath):
    """Load JSON file with UTF-8 encoding"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_global_config():
    """Load global configuration from locales/global.json"""
    return load_json(LOCALES_DIR / "global.json")


def load_locale(lang_code):
    """Load locale-specific configuration from locales/{lang_code}.json"""
    return load_json(LOCALES_DIR / f"{lang_code}.json")


def minify_html(html_code: str) -> str:
    """
    Minify HTML: remove whitespace, comments, etc.

    Args:
        html_code: Raw HTML string

    Returns:
        Minified HTML string
    """
    return htmlmin.minify(
        html_code,
        remove_comments=True,
        remove_empty_space=True,
        reduce_boolean_attributes=True,
        remove_optional_attribute_quotes=False,
        keep_pre=True,
        pre_tags=('pre', 'code', 'textarea')
    )


def minify_javascript(js_code: str) -> str:
    """
    Minify JavaScript and strip comments.

    Args:
        js_code: Raw JavaScript string

    Returns:
        Minified JavaScript string
    """
    return rjsmin.jsmin(js_code)


def save_html(html, output_path, minify=True):
    """
    Save HTML file to disk with optional minification.
    Creates parent directories if they don't exist.

    Args:
        html: HTML content string
        output_path: Path object or string for output file
        minify: Whether to minify HTML before saving (default: True)

    Returns:
        Path object of saved file
    """
    output_path = Path(output_path)

    # Minify HTML if requested
    if minify:
        html = minify_html(html)

    # Create parent directories
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    return output_path


def save_json(data, output_path):
    """
    Save JSON data to disk.
    Creates parent directories if they don't exist.

    Args:
        data: Dictionary or JSON-serializable object
        output_path: Path object or string for output file

    Returns:
        Path object of saved file
    """
    output_path = Path(output_path)

    # Create parent directories
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return output_path


def save_schema(schema_json, output_path):
    """
    Save JSON-LD schema to disk.
    Creates parent directories if they don't exist.

    Args:
        schema_json: Schema JSON string (already rendered from template)
        output_path: Path object or string for output file

    Returns:
        Path object of saved file
    """
    output_path = Path(output_path)

    # Create parent directories
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(schema_json)

    return output_path


def save_javascript(javascript, output_path, minify=True):
    """
    Save JavaScript file to disk with optional minification.
    Creates parent directories if they don't exist.

    Args:
        javascript: JavaScript content string
        output_path: Path object or string for output file
        minify: Whether to minify JS before saving (default: True)

    Returns:
        Path object of saved file
    """
    output_path = Path(output_path)

    # Minify JavaScript if requested
    if minify:
        javascript = minify_javascript(javascript)

    # Create parent directories
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(javascript)

    return output_path


def build_url(*parts, base_url="https://withframes.com", trailing_slash=True):
    """
    Build a clean URL from parts with double-slash prevention.

    Args:
        *parts: URL path parts to join (strings or None)
        base_url: Base URL (default: "https://withframes.com")
        trailing_slash: Whether to ensure trailing slash (default: True)

    Returns:
        Clean URL string with no double slashes

    Examples:
        >>> build_url('en', 'changelog')
        'https://withframes.com/en/changelog/'

        >>> build_url('', 'privacy')  # Empty string handled
        'https://withframes.com/privacy/'

        >>> build_url(None, 'changelog')  # None values filtered out
        'https://withframes.com/changelog/'

        >>> build_url('en/', '/privacy/')  # Slashes normalized
        'https://withframes.com/en/privacy/'
    """
    # Filter out None and empty string parts
    clean_parts = [str(p).strip('/') for p in parts if p]

    # Join parts with single slash
    path = '/'.join(clean_parts)

    # Build full URL
    if path:
        url = f"{base_url.rstrip('/')}/{path}"
    else:
        url = base_url.rstrip('/')

    # Add trailing slash if requested
    if trailing_slash and not url.endswith('/'):
        url += '/'

    # Final safety check: replace any double slashes (except in protocol)
    # Split by :// to preserve protocol, fix path, then rejoin
    if '://' in url:
        protocol, rest = url.split('://', 1)
        rest = rest.replace('//', '/')
        url = f"{protocol}://{rest}"

    return url


def build_path(*parts, trailing_slash=True):
    """
    Build a clean relative path from parts with double-slash prevention.

    Args:
        *parts: Path parts to join (strings or None)
        trailing_slash: Whether to ensure trailing slash (default: True)

    Returns:
        Clean path string starting with / and no double slashes

    Examples:
        >>> build_path('en', 'changelog')
        '/en/changelog/'

        >>> build_path('', 'privacy')
        '/privacy/'

        >>> build_path('en/', '/privacy/')
        '/en/privacy/'
    """
    # Filter out None and empty string parts
    clean_parts = [str(p).strip('/') for p in parts if p]

    # Join parts with single slash
    if clean_parts:
        path = '/' + '/'.join(clean_parts)
    else:
        path = '/'

    # Add trailing slash if requested
    if trailing_slash and not path.endswith('/'):
        path += '/'

    # Final safety check: replace any double slashes
    while '//' in path:
        path = path.replace('//', '/')

    return path


def format_date(iso_date, lang_code='en'):
    """
    Format ISO date to human-readable format based on language.

    Args:
        iso_date: ISO format date string (e.g., "2025-07-12" or "2025-07-12T10:00:00Z")
        lang_code: Language code for localization (default: 'en')

    Returns:
        Formatted date string in the language's format

    Examples:
        >>> format_date('2025-07-12', 'en')
        'Jul 12, 2025'

        >>> format_date('2025-07-12', 'de')
        '12. Jul 2025'

        >>> format_date('2025-07-12', 'ja')
        '2025年07月12日'
    """
    from datetime import datetime

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
