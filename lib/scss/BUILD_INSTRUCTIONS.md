# CSS Build Instructions

## Overview

The CSS is split into two files for optimal performance:

1. **critical.css** - Inlined in `<head>` (above-the-fold styles)
2. **deferred.css** - Loaded asynchronously (below-the-fold styles)
3. **style.css** - Kept as fallback with all styles

## Build Commands

### Compile Critical CSS (for inlining)

```bash
sass lib/scss/critical.scss lib/css/critical.css --style compressed
```

Or for development with source maps:
```bash
sass lib/scss/critical.scss lib/css/critical.css --style expanded --source-map
```

### Compile Deferred CSS (for async loading)

```bash
sass lib/scss/deferred.scss lib/css/deferred.css --style compressed
```

Or for development:
```bash
sass lib/scss/deferred.scss lib/css/deferred.css --style expanded --source-map
```

### Compile Fallback (all styles)

```bash
sass lib/scss/style.scss lib/css/style.css --style compressed
```

### Compile All Files at Once

```bash
sass lib/scss/critical.scss lib/css/critical.css --style compressed && \
sass lib/scss/deferred.scss lib/css/deferred.css --style compressed && \
sass lib/scss/style.scss lib/css/style.css --style compressed
```

## Watch Mode (Development)

To automatically recompile when files change:

```bash
sass --watch lib/scss:lib/css --style expanded --source-map
```

This will watch all .scss files in lib/scss/ and compile them to lib/css/

## File Structure

```
lib/scss/
├── critical.scss      # Above-the-fold styles (inline in <head>)
├── deferred.scss      # Below-the-fold styles (async load)
├── style.scss         # Complete styles (fallback)
├── _root.scss         # CSS variables
├── _base.scss         # Base styles & resets
├── _utilities.scss    # Utility classes
├── _layout.scss       # Grid system
├── _ratio.scss        # Aspect ratio containers
├── _links.scss        # Link styles
├── _buttons.scss      # Button styles
├── _header.scss       # Header/navigation
├── _hero.scss         # Hero section
├── _dropdown.scss     # Dropdown component
├── _carousel.scss     # Carousel component
├── _reviews.scss      # Reviews section
├── _features.scss     # Features section
├── _pricing.scss      # Pricing section
├── _qa.scss           # Q&A section
├── _footer.scss       # Footer
├── _overlay.scss      # Overlay styles
├── _video-overlay.scss # Video overlay
├── _mobile-menu.scss  # Mobile menu
└── _mixins.scss       # SCSS mixins
```

## Output Files

After compilation, you should have:

```
lib/css/
├── critical.css       # Inline this in <head>
├── critical.css.map   # Source map (dev only)
├── deferred.css       # Load this async
├── deferred.css.map   # Source map (dev only)
├── style.css          # Fallback (keep for noscript)
└── style.css.map      # Source map (dev only)
```

## Implementation in HTML

After compiling, update your template to:

1. **Inline critical.css** in the `<head>` tag
2. **Async load deferred.css**
3. **Keep style.css** as fallback in `<noscript>`

See template update instructions for details.

## Notes

- **Critical CSS** should be small (~10-15KB compressed) for optimal performance
- **Deferred CSS** can be larger as it loads asynchronously
- **Fallback CSS** ensures the site works even if JS is disabled
- Always test after compilation to ensure styles are working correctly
- Use compressed style for production, expanded for development
