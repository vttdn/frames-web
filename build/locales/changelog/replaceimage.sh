#!/bin/bash

# Base directory (current directory)
BASE_DIR="."

# Replace in 1.8.0-macos.json
find "$BASE_DIR" -type f -name "1.8.0-macos.json" | while read -r file; do
    echo "Processing $file"
    sed -i.bak 's/frames-1\.13\.0-1/frames-mac-1.8.0-1/g' "$file"
    rm "$file.bak"  # remove backup if not needed
done

# Replace in 1.7.0-macos.json
find "$BASE_DIR" -type f -name "1.7.0-macos.json" | while read -r file; do
    echo "Processing $file"
    sed -i.bak 's/frames-1\.12\.0-1/frames-mac-1.7.0-1/g' "$file"
    rm "$file.bak"
done

