# Changelog Translation Status

## Overview
Professional, fluent, culturally-adapted changelog translations for Frames app across 23 languages.

**Target**: 529 total files (23 files × 23 languages)

## Completed Languages ✅

### 1. German (de) - 23/23 files ✅
- All iOS changelog files (14 files)
- All macOS changelog files (9 files)
- Natural, fluent translations adapted for German photography terminology
- Changelog title: "Changelog"

### 2. Spanish (es) - 23/23 files ✅
- All iOS changelog files (14 files)
- All macOS changelog files (9 files)
- Natural, idiomatic Spanish with proper photography terms
- Changelog title: "Changelog"

## In Progress / Remaining Languages

### High Priority European Languages (10 remaining)
1. **it** (Italiano) - 0/23 - Title: "Changelog"
2. **pt** (Português) - 0/23 - Title: "Changelog"
3. **nl** (Nederlands) - 0/23 - Title: "Changelog"
4. **pl** (Polski) - 0/23 - Title: "Changelog"
5. **sv** (Svenska) - 0/23 - Title: "Changelog"
6. **da** (Dansk) - 0/23 - Title: "Ændringslog"
7. **nb** (Norsk) - 0/23 - Title: "Endringslogg"
8. **fi** (Suomi) - 0/23 - Title: "Muutosloki"
9. **ro** (Română) - 0/23 - Title: "Istoric Modificări"
10. **el** (Ελληνικά) - 0/23 - Title: "Αλλαγές"

### Asian Languages (8 remaining)
1. **ja** (日本語) - 0/23 - Title: "更新履歴"
2. **ko** (한국어) - 0/23 - Title: "변경 내역"
3. **zh** (简体中文) - 0/23 - Title: "更新日志"
4. **zh-hant** (繁體中文) - 0/23 - Title: "更新日誌"
5. **th** (ไทย) - 0/23 - Title: "บันทึกการเปลี่ยนแปลง"
6. **vi** (Tiếng Việt) - 0/23 - Title: "Nhật Ký Thay Đổi"
7. **hi** (हिन्दी) - 0/23 - Title: "परिवर्तन सूची"
8. **id** (Bahasa Indonesia) - 0/23 - Title: "Log Perubahan"

### Slavic Languages (2 remaining)
1. **ru** (Русский) - 0/23 - Title: "Обновления"
2. **uk** (Українська) - 0/23 - Title: "Історія змін"

### Other (1 remaining)
1. **tr** (Türkçe) - 0/23 - Title: "Değişiklik Günlüğü"

## Translation Quality Standards

### What Has Been Done (German & Spanish)
✅ Natural, fluent translations (NOT literal word-for-word)
✅ Idiomatic expressions native speakers actually use
✅ Technical photography terms properly adapted
✅ Alt text translated with SEO optimization (80-100 chars)
✅ Image paths preserved with `{{ lang }}` placeholder
✅ Cultural adaptation for each language
✅ Consistent terminology throughout

### Key Translation Principles Applied
- **Film photography / Analog photography**: Adapted naturally per language
- **Film roll / Film stock**: Photography-specific terminology used
- **Metadata / EXIF**: Often kept or minimally adapted
- **Workflow**: Translated to natural equivalents, not literal
- **Pro users, recorder, nested folders**: Context-appropriate translations

## Next Steps to Complete Remaining 21 Languages

### Option 1: Professional Translation Service (Recommended)
Use the completed German and Spanish translations as reference/style guides:

1. **Reference files**:
   - `/build/locales/changelog/de/` - German examples
   - `/build/locales/changelog/es/` - Spanish examples
   - `/build/locales/changelog/en/` - English source

2. **Provide to translators**:
   - English source files (23 files)
   - German/Spanish as style references
   - This document for translation standards
   - Emphasis on natural, fluent translations

3. **Services to consider**:
   - DeepL Pro (high quality, supports most languages)
   - Professional translation agency specializing in technical/app content
   - Native speaker translators familiar with photography

### Option 2: Automated with Human Review
1. Use DeepL API or similar to generate initial translations
2. Have native speakers review for:
   - Natural phrasing
   - Photography terminology
   - Cultural appropriateness
   - Technical accuracy

### Option 3: Continue Manual Creation
If continuing manually, prioritize in this order:
1. European languages (it, pt, nl, pl, sv, da, nb, fi, ro, el)
2. Asian languages (ja, ko, zh, zh-hant, th, vi, hi, id)
3. Slavic languages (ru, uk)
4. Turkish (tr)

## File Structure Reference

Each language needs 23 files:

### iOS Files (14 files):
- 1.0.0-ios.json
- 1.1.0-ios.json
- 1.2.0-ios.json
- 1.3.0-ios.json
- 1.4.0-ios.json
- 1.5.0-ios.json
- 1.6.0-ios.json
- 1.7.0-ios.json
- 1.8.0-ios.json
- 1.9.0-ios.json
- 1.10.0-ios.json
- 1.11.0-ios.json
- 1.12.0-ios.json
- 1.13.0-ios.json

### macOS Files (9 files):
- 1.0.0-macos.json
- 1.1.0-macos.json
- 1.2.0-macos.json
- 1.3.0-macos.json
- 1.4.0-macos.json
- 1.5.0-macos.json
- 1.6.0-macos.json
- 1.7.0-macos.json
- 1.8.0-macos.json

## Important Notes

### DO NOT Translate:
- Version numbers
- Dates
- URL slugs
- Platform values ("ios", "macos")
- Image paths (keep `{{ lang }}` placeholder)
- Film stock brand names (Kodak Portra, Ilford HP5, etc.)

### DO Translate:
- title
- summary
- All section content (headings, paragraphs, list items)
- Alt text for images
- improvements array items
- fixes (title and description)
- patches descriptions

### Image Path Handling:
Some images use:
- `"/lib/img/shared/changelog/..."` - no {{ lang }} (shared across languages)
- `"/lib/img/{{ lang }}/changelog/..."` - language-specific images

Keep the paths EXACTLY as they appear in English - do not change them.

## Estimated Effort

- **Per language**: ~2-3 hours for professional translator
- **Total remaining**: ~42-63 hours of translation work
- **With automation + review**: ~20-30 hours

## Quality Assurance Checklist

For each completed language:
- [ ] All 23 files created
- [ ] JSON structure valid
- [ ] Translations sound natural to native speakers
- [ ] Photography terminology accurate
- [ ] Alt text appropriate length (80-100 chars)
- [ ] Image paths unchanged
- [ ] Consistent terminology throughout
- [ ] No English text remaining (except brand names)

## Contact & Support

For questions about:
- Translation standards: Reference this document
- Technical structure: See English source files
- Style reference: See completed German/Spanish translations
- Photography terminology: Consult with photography community for natural terms

---

**Last Updated**: 2025-10-11
**Status**: 2/23 languages complete (German, Spanish)
**Remaining**: 21 languages, 483 files
