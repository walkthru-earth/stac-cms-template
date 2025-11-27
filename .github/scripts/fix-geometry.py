#!/usr/bin/env python3
"""
Fix STAC Items by converting stringified geometry to JSON objects and cleaning empty fields.

Sveltia CMS map widget stores geometry as stringified GeoJSON, but STAC
requires geometry to be a proper JSON object. This script:
1. Converts stringified geometry to JSON objects
2. Removes empty string values from optional fields
"""

import json
import sys
from pathlib import Path
from typing import Any


def remove_empty_strings(obj: Any) -> Any:
    """
    Recursively remove keys with empty string values from dictionaries.

    Args:
        obj: The object to clean (dict, list, or primitive)

    Returns:
        Cleaned object
    """
    if isinstance(obj, dict):
        return {
            k: remove_empty_strings(v)
            for k, v in obj.items()
            if v != ""  # Remove empty strings
        }
    elif isinstance(obj, list):
        return [remove_empty_strings(item) for item in obj]
    else:
        return obj


def fix_stac_item(file_path: Path) -> bool:
    """
    Fix STAC Item by:
    1. Parsing stringified geometry
    2. Removing empty optional fields

    Args:
        file_path: Path to the STAC Item JSON file

    Returns:
        True if file was modified, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_data = f.read()
            data = json.loads(original_data)

        # Check if this is a STAC Item
        if data.get('type') != 'Feature':
            print(f"⚠️  Skipping {file_path.name}: Not a STAC Item (type != 'Feature')")
            return False

        modified = False
        fixes_applied = []

        # Fix 1: Parse stringified geometry
        geometry = data.get('geometry')
        if geometry and isinstance(geometry, str):
            try:
                parsed_geometry = json.loads(geometry)
                data['geometry'] = parsed_geometry
                modified = True
                fixes_applied.append("geometry")
            except json.JSONDecodeError as e:
                print(f"❌ Error parsing geometry in {file_path.name}: {e}", file=sys.stderr)
                return False

        # Fix 2: Remove empty strings from optional fields
        cleaned_data = remove_empty_strings(data)

        # Check if cleaning made changes
        if json.dumps(cleaned_data, sort_keys=True) != json.dumps(data, sort_keys=True):
            modified = True
            fixes_applied.append("empty fields")
            data = cleaned_data

        # Write back if modified
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                f.write('\n')  # Add trailing newline

            print(f"✅ Fixed {file_path.name}: {', '.join(fixes_applied)}")
            return True
        else:
            print(f"✓  {file_path.name}: Already valid")
            return False

    except Exception as e:
        print(f"❌ Error processing {file_path.name}: {e}", file=sys.stderr)
        return False


def main():
    """Process all STAC Item files in the items/ directory."""
    items_dir = Path('items')

    if not items_dir.exists():
        print(f"❌ Items directory not found: {items_dir}")
        sys.exit(1)

    json_files = list(items_dir.glob('*.json'))

    if not json_files:
        print("ℹ️  No JSON files found in items/")
        return

    print(f"🔍 Processing {len(json_files)} STAC Item(s)...\n")

    modified_count = 0
    for file_path in sorted(json_files):
        if fix_stac_item(file_path):
            modified_count += 1

    print(f"\n📊 Summary: {modified_count} file(s) modified")

    if modified_count > 0:
        sys.exit(2)  # Exit with code 2 to signal files were modified


if __name__ == '__main__':
    main()
