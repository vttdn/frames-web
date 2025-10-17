#!/bin/bash
set -euo pipefail

# Adjust path to your project root
CSS_DIR="../../lib/css"

# Check if directory exists
if [ ! -d "$CSS_DIR" ]; then
  echo "Error: CSS directory not found at $CSS_DIR"
  exit 1
fi

# Process each CSS file
for f in "$CSS_DIR"/*.css; do
  [ -e "$f" ] || continue  # Skip if no files match
  echo "Optimizing $f..."
  npx postcss "$f" --use cssnano --config postcss.config.cjs --replace
  npx lightningcss --minify --targets '>= 1%, last 2 versions' "$f" -o "$f"
done

echo "✅ All done!"
