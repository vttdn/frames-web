# Changelog System Documentation

## Overview

The changelog system is a standalone build system that generates paginated changelog pages from JSON config files. It's separate from the main homepage/privacy page generation.

## File Structure

```
build/
├── locales/
│   ├── changelog/          # Changelog entry config files
│   │   └── 1.13.json      # Example entry
│   ├── en.json            # Contains changelog UI translations
│   └── global.json
├── scripts/
│   └── build_changelog.py # Standalone changelog builder
└── templates/
    ├── changelog-index.html  # List view with pagination
    └── changelog-entry.html  # Individual entry page

changelog/
├── index.html            # Page 1 of changelog list
├── page-2/              # Page 2 (if needed)
│   └── index.html
├── 1-13/                # Individual version page
│   └── index.html
└── sitemap.xml          # Changelog-specific sitemap

sitemap.xml              # Main sitemap index (references changelog sitemap)
sitemap-main.xml         # Homepage/privacy pages sitemap
```

## Adding a New Changelog Entry

### 1. Create a JSON config file

Location: `build/locales/changelog/{version}.json`

Example: `build/locales/changelog/1.14.json`

```json
{
  "version": "1.14.0",
  "version_short": "1.14",
  "url_slug": "1-14",
  "platform": "ios",
  "release_date": "2025-04-15T10:00:00.000Z",
  "title": "Your Update Title",
  "summary": "Brief summary of the update...",
  "sections": [
    {
      "type": "heading",
      "level": 3,
      "content": "Section Title"
    },
    {
      "type": "paragraph",
      "content": "Text content here...",
      "link": {
        "text": "Optional Link",
        "url": "#"
      }
    },
    {
      "type": "list",
      "items": [
        {
          "title": "Feature Title",
          "description": "Feature description"
        }
      ]
    },
    {
      "type": "media",
      "image": "/lib/img/en/preview1.webp",
      "image_2x": "/lib/img/en/preview1@2x.webp",
      "alt": "Image description",
      "width": "400",
      "height": "300"
    }
  ],
  "improvements": [
    "Simple improvement description",
    "Another improvement"
  ],
  "fixes": [
    {
      "title": "Bug Category",
      "description": "Fix description"
    }
  ],
  "patches": [
    {
      "version": "1.14.1",
      "description": "Patch description"
    }
  ]
}
```

### 2. Field Descriptions

- **version**: Full version number (e.g., "1.14.0")
- **version_short**: Short version for grouping (e.g., "1.14")
- **url_slug**: URL-friendly version (e.g., "1-14") - use hyphens, omit last patch number
- **platform**: Either "ios" or "macos"
- **release_date**: ISO 8601 date format
- **title**: Main changelog title
- **summary**: Brief description (shown in list view)
- **sections**: Array of content blocks (heading, paragraph, list, media)
- **improvements**: Array of simple strings
- **fixes**: Array of objects with title and description
- **patches**: Array of patch versions with descriptions

### 3. Build the Changelog

Run the build script:

```bash
python3 build/scripts/build_changelog.py
```

This will:
- Generate paginated index pages (5 entries per page)
- Generate individual entry pages with prev/next navigation
- Create/update the changelog sitemap
- Sort entries by release date (newest first)

## Configuration

### Entries Per Page

Located in `build/scripts/build_changelog.py`:

```python
ENTRIES_PER_PAGE = 5  # Change this to adjust pagination
```

### UI Translations

Located in `build/locales/en.json` under the `changelog` object:

```json
"changelog": {
  "meta": {
    "title": "Changelog - Frames",
    "description": "...",
    "canonical_url": "https://withframes.com/changelog/"
  },
  "heading": "Changelog",
  "labels": {
    "improvements": "Improvements",
    "fixes": "Fixes",
    "patches": "Patches",
    "platform_ios": "iOS",
    "platform_macos": "macOS",
    "previous": "Previous",
    "next": "Next"
  },
  "pagination": {
    "previous": "Previous",
    "next": "Next",
    "page": "Page"
  }
}
```

## Features

✅ Pagination (5 entries per page)
✅ Platform differentiation (iOS/macOS badge)
✅ Individual entry pages with prev/next navigation
✅ Flexible content sections (headings, paragraphs, lists, media)
✅ Collapsible Improvements/Fixes/Patches sections
✅ Automatic sitemap generation
✅ Language switcher (ready for future translations)
✅ Responsive design (uses existing CSS)

## Future Expansion

To add support for other languages:

1. Add changelog translations to each language file (e.g., `build/locales/fr.json`)
2. Create language-specific entry configs in `build/locales/changelog/fr/`
3. Modify `build_changelog.py` to iterate through all languages

## Notes

- Changelog entries are sorted by `release_date` (newest first)
- URL slugs use hyphens and omit the patch version (e.g., 1.13.1 → 1-13)
- The system is completely separate from the main site generator
- Currently only English is implemented (ready for expansion)
