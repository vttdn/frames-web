# Template Update Guide - Critical CSS Implementation

## Overview

This guide explains how to update `templates/index.html` to use the new critical CSS inlining strategy for optimal performance.

## Current Implementation

```html
<head>
    <!-- ... other head elements ... -->
    <link rel="stylesheet" href="/lib/css/style.css" media="print" onload="this.media='all'">
    <noscript>
        <link rel="stylesheet" href="/lib/css/style.css">
    </noscript>
</head>
```

## New Implementation

Replace the CSS loading section with:

```html
<head>
    <!-- ... other head elements ... -->

    <!-- Critical CSS - Inlined for immediate render -->
    <style>
        /* Paste the contents of /lib/css/critical.css here */
        /* This will be ~10-15KB of compressed CSS */
        /* Example content (replace with actual compiled CSS): */
        :root{--color-black:#0C0B14;--color-white:#ECECED;...}
        html{scroll-behavior:smooth}
        body{color:var(--color-primary);...}
        /* ... rest of critical.css content ... */
    </style>

    <!-- Deferred CSS - Loaded asynchronously for below-the-fold content -->
    <link rel="stylesheet" href="/lib/css/deferred.css" media="print" onload="this.media='all'">

    <!-- Fallback for browsers without JavaScript -->
    <noscript>
        <link rel="stylesheet" href="/lib/css/style.css">
    </noscript>
</head>
```

## Step-by-Step Instructions

### Step 1: Compile CSS Files

First, compile the SCSS files to CSS:

```bash
# Compile critical CSS (compressed for inlining)
sass lib/scss/critical.scss lib/css/critical.css --style compressed

# Compile deferred CSS (compressed for async loading)
sass lib/scss/deferred.scss lib/css/deferred.css --style compressed

# Compile fallback CSS (compressed)
sass lib/scss/style.scss lib/css/style.css --style compressed
```

### Step 2: Copy Critical CSS Content

1. Open `/lib/css/critical.css`
2. Copy the **entire contents** of the file
3. Open `templates/index.html`
4. Find the current CSS loading section in `<head>`
5. Replace it with the new implementation shown above
6. Paste the critical.css content inside the `<style>` tags

### Step 3: Update Deferred CSS Path

Ensure the deferred CSS link points to the correct path:

```html
<link rel="stylesheet" href="/lib/css/deferred.css" media="print" onload="this.media='all'">
```

The `media="print"` trick ensures the CSS is downloaded asynchronously, and `onload="this.media='all'"` applies it once loaded.

### Step 4: Keep Fallback for No-JS

Keep the noscript fallback for users without JavaScript:

```html
<noscript>
    <link rel="stylesheet" href="/lib/css/style.css">
</noscript>
```

## Complete Example

Here's what the full `<head>` section should look like:

```html
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>{{ locale_data.meta.title }}</title>
    <meta name="description" content="{{ locale_data.meta.description }}">
    <link rel="canonical" href="{{ locale_data.meta.canonical_url }}">

    {% for link in hreflang_links %}
    <link rel="alternate" hreflang="{{ link.hreflang }}" href="{{ link.href }}">
    {% endfor %}

    <!-- Critical CSS - Inlined -->
    <style>
        /* Paste compiled critical.css content here */
    </style>

    <!-- Deferred CSS - Async loaded -->
    <link rel="stylesheet" href="/lib/css/deferred.css" media="print" onload="this.media='all'">

    <!-- Fallback CSS for no-JS -->
    <noscript>
        <link rel="stylesheet" href="/lib/css/style.css">
    </noscript>

    <!-- Rest of head elements -->
    <meta name="twitter:card" content="{{ locale_data.meta.twitter_card }}">
    <!-- ... -->
</head>
```

## Automation Option (Advanced)

If you want to automate the critical CSS inlining during the build process, you can:

1. **Option A: Python Script Integration**
   - Modify `scripts/generate.py` to read `critical.css` and inject it into the template
   - Use Jinja2 to include the CSS file content

2. **Option B: Jinja2 Include**
   ```html
   <style>
   {% include '../lib/css/critical.css' %}
   </style>
   ```
   Note: You'll need to configure Jinja2 to allow including CSS files.

3. **Option C: Template Variable**
   - Load critical.css in generate.py
   - Pass it as a template variable
   ```python
   with open('lib/css/critical.css', 'r') as f:
       critical_css = f.read()
   context['critical_css'] = critical_css
   ```
   - Use in template:
   ```html
   <style>{{ critical_css|safe }}</style>
   ```

## Manual Copy-Paste Method (Simplest)

For now, the simplest approach is:

1. Compile SCSS to CSS
2. Copy `critical.css` content
3. Paste into `<style>` tag in template
4. Regenerate site with `python3 scripts/generate.py`

**When to update:** Whenever you modify any SCSS files that are imported in `critical.scss`, you'll need to recompile and update the inlined CSS.

## Performance Benefits

This implementation provides:

- ✅ **Faster First Contentful Paint (FCP)** - Critical styles load immediately
- ✅ **Eliminates render-blocking CSS** - Deferred styles don't block rendering
- ✅ **Better Lighthouse scores** - Optimized CSS delivery
- ✅ **Progressive rendering** - Page is usable before all CSS loads
- ✅ **Graceful degradation** - Fallback for no-JS environments

## Testing

After implementing, verify:

1. **Visual check** - Page looks correct on load
2. **Network tab** - Critical CSS is inlined (no request), deferred.css loads async
3. **Lighthouse** - Check performance score improvement
4. **No-JS test** - Disable JavaScript and verify fallback works

## Troubleshooting

**Issue: Styles not applying**
- Verify critical.css is properly compiled
- Check for CSS syntax errors in inlined styles
- Ensure deferred.css path is correct

**Issue: Flash of unstyled content**
- Critical CSS might be missing some styles
- Check which components are visible on initial load
- Add missing styles to critical.scss

**Issue: Large critical CSS file**
- Review what's included in critical.scss
- Consider splitting further if needed
- Target should be <15KB compressed

## Maintenance

Remember to:
- Recompile CSS after any SCSS changes
- Update inlined critical CSS in template
- Test across different pages/languages
- Monitor performance metrics
