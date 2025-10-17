#!/bin/bash

# Adjust path to your project root
CSS_DIR="../lib/css"

for f in "$CSS_DIR"/*.css; do
  [ -e "$f" ] || continue  # skip if no files match
  npx postcss "$f" --use cssnano --config ../postcss.config.cjs --replace
  npx lightningcss --minify --targets '>= 1%, last 2 versions' "$f" -o "$f"
done

