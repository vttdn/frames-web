#!/usr/bin/env python3
"""
Remove all generated changelog OG images
"""

import shutil
from pathlib import Path

# Get project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent
OG_IMAGE_BASE = PROJECT_ROOT / "lib" / "img"

def main():
    """Remove all changelog OG images"""
    print("🧹 Cleaning changelog OG images...\n")

    removed_count = 0
    total_size = 0

    # Find all og-image directories
    for lang_dir in OG_IMAGE_BASE.iterdir():
        if not lang_dir.is_dir():
            continue

        og_dir = lang_dir / "changelog" / "og-image"

        if og_dir.exists() and og_dir.is_dir():
            # Calculate size before removal
            for file in og_dir.glob("*.jpg"):
                total_size += file.stat().st_size
                removed_count += 1

            # Remove the directory
            shutil.rmtree(og_dir)
            print(f"✓ Removed: {og_dir.relative_to(PROJECT_ROOT)}")

    # Convert size to MB
    size_mb = total_size / (1024 * 1024)

    print(f"\n📊 Summary:")
    print(f"   🗑️  Images removed: {removed_count}")
    print(f"   💾 Space freed: {size_mb:.2f} MB")

    if removed_count == 0:
        print("\n✨ No OG images found to clean")
    else:
        print(f"\n✨ Done! Removed {removed_count} changelog OG images")

if __name__ == "__main__":
    main()
