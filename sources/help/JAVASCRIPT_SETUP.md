# JavaScript Template Setup - Complete ✅

## Overview

JavaScript is now templated per language and deferred for optimal performance.

## What Was Done

### 1. Created JavaScript Template
**File:** `templates/core.js`

Contains all interactive functionality:
- JSON-LD schema injection
- Video overlay control
- Social sharing functionality

Uses Jinja2 variables:
- `{{ lang }}` - Language code for schema paths
- `{{ locale_data.meta.description }}` - Localized meta description for sharing

### 2. Updated Generate Script
**File:** `scripts/generate.py`

Added functions:
- `generate_javascript()` - Renders core.js template with locale data
- `save_javascript()` - Saves to `/lib/js/{lang}/core.js`

### 3. Updated Template
**File:** `templates/index.html`

**Before:**
```html
<script>
  // 70+ lines of inline JavaScript
</script>
```

**After:**
```html
<script defer src="/lib/js/{{ lang }}/core.js"></script>
```

## File Structure

```
templates/
└── core.js                    # JavaScript template

lib/
└── js/
    ├── en/
    │   └── core.js           # Generated English JS
    ├── fr/
    │   └── core.js           # Generated French JS
    ├── de/
    │   └── core.js           # Generated German JS
    └── [other languages]/
        └── core.js
```

## Generated Output

Each language gets its own JavaScript file with localized content:

**Example: `/lib/js/en/core.js`**
```javascript
// Core JavaScript for Frames website
// Language: en
// Auto-generated - do not edit directly

document.addEventListener('DOMContentLoaded', function () {
    const schemaFiles = [
        '/lib/schema/en/frames.json',
        '/lib/schema/en/faq.json'
    ];
    // ... rest of code
});
```

## Performance Benefits

✅ **Deferred Loading** - JavaScript doesn't block HTML parsing
✅ **Cacheable** - Browser can cache per language
✅ **Parallel Download** - Downloads while HTML renders
✅ **No Render Blocking** - Page is interactive faster
✅ **Clean HTML** - No inline scripts, easier to maintain

## How It Works

### Build Process
```
1. Run generator:
   python3 scripts/generate.py

2. For each language:
   → Render core.js template with locale data
   → Save to lib/js/{lang}/core.js
   → Reference in HTML with defer attribute
```

### Browser Behavior
```
1. HTML loads and parses (not blocked by JS)
2. Browser downloads /lib/js/{lang}/core.js in parallel
3. After HTML parsing completes, JS executes
4. Schemas injected, interactivity enabled
```

## JavaScript Functions

### Schema Injection
Loads JSON-LD schemas dynamically:
```javascript
const schemaFiles = [
    '/lib/schema/{{ lang }}/frames.json',
    '/lib/schema/{{ lang }}/faq.json'
];
```

### Video Overlay Control
Stops video when overlay closes:
```javascript
document.getElementById('video-toggle').addEventListener('change', function(e) {
    if (!e.target.checked) {
        const iframe = document.querySelector('.video-container iframe');
        const src = iframe.src;
        iframe.src = src; // Reload to stop
    }
});
```

### Social Sharing
Opens share dialog for various platforms:
```javascript
function shareOn(platform) {
    const url = encodeURIComponent(window.location.href);
    const title = encodeURIComponent(document.title);
    const text = encodeURIComponent('{{ locale_data.meta.description }}');
    // ... platform-specific URLs
}
```

## Testing

After running `python3 scripts/generate.py`:

1. **Check files exist:**
   ```bash
   ls lib/js/*/core.js
   ```

2. **Verify in browser:**
   - Open DevTools → Network tab
   - Look for `core.js` loading with `defer` attribute
   - Check it doesn't block page rendering

3. **Test functionality:**
   - Video overlay stop/start
   - Social sharing buttons
   - JSON-LD schemas in `<head>`

## Maintenance

### To modify JavaScript:
1. Edit `templates/core.js`
2. Run `python3 scripts/generate.py`
3. All language versions regenerate automatically

### To add new functionality:
1. Add to `templates/core.js`
2. Use `{{ lang }}` or `{{ locale_data.* }}` for localized content
3. Regenerate with build script

## SEO Impact

✅ **Positive** - Deferred JS doesn't affect SEO
✅ **Lighthouse** - Better performance scores
✅ **Core Web Vitals** - Improved FCP and LCP
✅ **Crawlability** - Content available immediately

## Comparison

| Metric | Before (Inline) | After (Deferred) |
|--------|-----------------|------------------|
| HTML blocking | Yes | No |
| Cacheable | No | Yes |
| Maintainability | Low | High |
| Per-language | Manual | Automatic |
| File size | ~2.5KB inline | ~2.5KB cached |

## Next Steps

The setup is complete! JavaScript will now:
- ✅ Be generated per language automatically
- ✅ Load deferred (non-blocking)
- ✅ Be browser-cacheable
- ✅ Use localized content

Just run `python3 scripts/generate.py` and all JavaScript files will be created/updated.
