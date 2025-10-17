#!/usr/bin/env python3
"""
Build Validation Script for Frames Website
Validates generated HTML, URLs, and overall build quality.

Usage:
    python test_build.py                    # Run all validations
    python test_build.py --urls             # Check URLs only
    python test_build.py --html             # Validate HTML only
    python test_build.py --quick            # Quick validation (subset of files)
"""

import argparse
import re
import sys
from pathlib import Path
from collections import defaultdict

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent.parent


def validate_urls_in_file(file_path, base_path=PROJECT_ROOT):
    """
    Validate URLs in an HTML file for common issues.
    Returns list of issues found.
    """
    issues = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        relative_path = file_path.relative_to(base_path)

        # Check for double slashes in URLs (excluding protocol://)
        double_slash_pattern = r'(?<!:)//+'
        matches = re.finditer(double_slash_pattern, content)
        for match in matches:
            # Get context around the match
            start = max(0, match.start() - 30)
            end = min(len(content), match.end() + 30)
            context = content[start:end].replace('\n', ' ')
            issues.append({
                'file': str(relative_path),
                'type': 'double_slash',
                'context': context
            })

        # Check for malformed hreflang links
        hreflang_pattern = r'<link[^>]*rel=["\']alternate["\'][^>]*hreflang=["\']([^"\']+)["\'][^>]*href=["\']([^"\']+)["\']'
        for match in re.finditer(hreflang_pattern, content):
            hreflang, href = match.groups()
            if '//' in href.replace('://', ''):
                issues.append({
                    'file': str(relative_path),
                    'type': 'malformed_hreflang',
                    'hreflang': hreflang,
                    'href': href
                })

        # Check for missing trailing slashes in canonical URLs
        canonical_pattern = r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']'
        for match in re.finditer(canonical_pattern, content):
            href = match.group(1)
            if not href.endswith('/') and not href.endswith('.html'):
                issues.append({
                    'file': str(relative_path),
                    'type': 'canonical_no_trailing_slash',
                    'href': href
                })

    except Exception as e:
        issues.append({
            'file': str(file_path.relative_to(base_path)),
            'type': 'read_error',
            'error': str(e)
        })

    return issues


def validate_html_structure(file_path, base_path=PROJECT_ROOT):
    """
    Validate basic HTML structure.
    Returns list of issues found.
    """
    issues = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        relative_path = file_path.relative_to(base_path)

        # Check for required meta tags
        required_metas = [
            (r'<meta[^>]*charset=["\']utf-8["\']', 'missing_charset'),
            (r'<meta[^>]*name=["\']viewport["\']', 'missing_viewport'),
            (r'<title>', 'missing_title'),
        ]

        for pattern, issue_type in required_metas:
            if not re.search(pattern, content, re.IGNORECASE):
                issues.append({
                    'file': str(relative_path),
                    'type': issue_type
                })

        # Check for unclosed tags (basic check)
        # Skip for minified HTML (single line files)
        line_count = content.count('\n')
        if line_count > 10:  # Only check non-minified files
            open_tags = len(re.findall(r'<(?!/)(?!!)[a-z][^>]*(?<!/)>', content, re.IGNORECASE))
            close_tags = len(re.findall(r'</[a-z][^>]*>', content, re.IGNORECASE))
            self_closing = len(re.findall(r'<[^>]*/>', content))

            # This is a rough check, not perfect but catches major issues
            if abs(open_tags - close_tags - self_closing) > 10:
                issues.append({
                    'file': str(relative_path),
                    'type': 'tag_mismatch',
                    'open': open_tags,
                    'close': close_tags,
                    'self_closing': self_closing
                })

    except Exception as e:
        issues.append({
            'file': str(file_path.relative_to(base_path)),
            'type': 'read_error',
            'error': str(e)
        })

    return issues


def validate_date_formatting(file_path, base_path=PROJECT_ROOT):
    """
    Validate that dates are properly formatted in HTML.
    Returns list of issues found.
    """
    issues = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        relative_path = file_path.relative_to(base_path)

        # Check for time tags with datetime attribute but empty content
        time_pattern = r'<time[^>]*datetime=["\']([^"\']+)["\'][^>]*>(.*?)</time>'
        for match in re.finditer(time_pattern, content, re.DOTALL):
            datetime_val, time_content = match.groups()
            time_content = time_content.strip()

            if not time_content:
                issues.append({
                    'file': str(relative_path),
                    'type': 'empty_time_tag',
                    'datetime': datetime_val
                })

            # Check if datetime is in ISO format
            if not re.match(r'^\d{4}-\d{2}-\d{2}', datetime_val):
                issues.append({
                    'file': str(relative_path),
                    'type': 'invalid_datetime_format',
                    'datetime': datetime_val
                })

    except Exception as e:
        issues.append({
            'file': str(file_path.relative_to(base_path)),
            'type': 'read_error',
            'error': str(e)
        })

    return issues


def collect_html_files(quick=False):
    """Collect all HTML files to validate"""
    files = []

    # Homepage files
    files.append(PROJECT_ROOT / "index.html")

    # Language-specific homepages and privacy pages
    languages = ['de', 'fr', 'es', 'ja', 'zh', 'zh-hant']  # Sample for quick mode
    if not quick:
        languages = ['da', 'de', 'el', 'es', 'fi', 'fr', 'hi', 'id', 'it', 'ja', 'ko',
                    'nb', 'nl', 'pl', 'pt', 'ro', 'ru', 'sv', 'th', 'tr', 'uk', 'vi', 'zh', 'zh-hant']

    for lang in languages:
        lang_dir = PROJECT_ROOT / lang
        if lang_dir.exists():
            files.append(lang_dir / "index.html")
            files.append(lang_dir / "privacy" / "index.html")

            # Changelog files (just index pages for quick mode)
            changelog_dir = lang_dir / "changelog"
            if changelog_dir.exists():
                files.append(changelog_dir / "index.html")
                if not quick:
                    # Include all changelog pages
                    files.extend(changelog_dir.glob("*/index.html"))

    # Privacy for English
    files.append(PROJECT_ROOT / "privacy" / "index.html")

    # Changelog for English
    changelog_dir = PROJECT_ROOT / "changelog"
    if changelog_dir.exists():
        files.append(changelog_dir / "index.html")
        if not quick:
            files.extend(changelog_dir.glob("*/index.html"))

    # Filter out non-existent files and return
    return [f for f in files if f.exists()]


def run_validations(check_urls=True, check_html=True, check_dates=True, quick=False):
    """Run all validations and return results"""

    print("Frames Build Validation")
    print("=" * 60)

    if quick:
        print("Running in QUICK mode (subset of files)")

    files = collect_html_files(quick=quick)
    print(f"Validating {len(files)} HTML files...\n")

    all_issues = defaultdict(list)
    files_checked = 0

    for file_path in files:
        issues = []

        if check_urls:
            issues.extend(validate_urls_in_file(file_path))

        if check_html:
            issues.extend(validate_html_structure(file_path))

        if check_dates:
            issues.extend(validate_date_formatting(file_path))

        if issues:
            for issue in issues:
                all_issues[issue['type']].append(issue)

        files_checked += 1

    # Print results
    print("\n" + "=" * 60)
    print("VALIDATION RESULTS")
    print("=" * 60)

    if not all_issues:
        print("✅ All validations passed!")
        print(f"   Checked {files_checked} files with no issues found.")
        return True

    # Group and display issues
    print(f"❌ Found {sum(len(v) for v in all_issues.values())} issues:\n")

    for issue_type, issues in sorted(all_issues.items()):
        print(f"  [{issue_type}] - {len(issues)} occurrence(s)")

        # Show first few examples
        for issue in issues[:3]:
            print(f"    → {issue['file']}")
            if 'context' in issue:
                print(f"      Context: ...{issue['context']}...")
            if 'href' in issue:
                print(f"      URL: {issue['href']}")
            if 'error' in issue:
                print(f"      Error: {issue['error']}")

        if len(issues) > 3:
            print(f"    ... and {len(issues) - 3} more")
        print()

    return False


def main():
    """Main validation function with CLI argument parsing"""
    parser = argparse.ArgumentParser(
        description='Validate Frames website build output',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python test_build.py              Run all validations
  python test_build.py --urls       Check URLs only
  python test_build.py --html       Validate HTML only
  python test_build.py --quick      Quick validation (subset)
        """
    )

    parser.add_argument('--urls', action='store_true', help='Check URLs only')
    parser.add_argument('--html', action='store_true', help='Validate HTML structure only')
    parser.add_argument('--dates', action='store_true', help='Validate date formatting only')
    parser.add_argument('--quick', action='store_true', help='Quick validation (subset of files)')

    args = parser.parse_args()

    # If no specific check requested, run all
    run_all = not (args.urls or args.html or args.dates)

    check_urls = run_all or args.urls
    check_html = run_all or args.html
    check_dates = run_all or args.dates

    success = run_validations(
        check_urls=check_urls,
        check_html=check_html,
        check_dates=check_dates,
        quick=args.quick
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
