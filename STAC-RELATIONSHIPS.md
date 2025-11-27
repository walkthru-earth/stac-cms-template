# STAC Relationship Management Guide

This guide explains how to properly manage relationships between Catalogs, Collections, and Items in the STAC CMS.

## Understanding STAC Relationships

STAC uses a hierarchical structure with bidirectional links:

```
Catalog (root)
  ├─ Sub-Catalog (optional)
  │   └─ Collection
  └─ Collection
      ├─ Item 1
      ├─ Item 2
      └─ Item 3
```

## Relationship Types

### ✅ Automatic (Handled by CMS)
- **Item → Collection**: Use the "Collection" relation dropdown in Items

### ⚠️ Manual (You Must Add Links)
- **Collection → Items**: Add "item" links in Collection
- **Collection → Catalog**: Add "parent" link in Collection
- **Catalog → Collections**: Add "child" links in Catalog
- **Catalog → Sub-catalogs**: Add "child" links in parent Catalog

---

## Step-by-Step Workflows

### Creating a Complete STAC Hierarchy

#### 1. Create Root Catalog

1. Go to "STAC Catalogs" → "New STAC Catalog"
2. Fill in:
   - **ID**: `my-catalog`
   - **Title**: "My Data Catalog"
   - **Description**: Describe your catalog
3. Add required links:
   ```yaml
   Links:
     - Relation Type: Self
       URL: https://walkthru.earth/stac-cms-template/catalog/my-catalog.json
       Title: My Data Catalog

     - Relation Type: Root
       URL: ./my-catalog.json
       Title: My Data Catalog
   ```
4. Save

#### 2. Create Collection

1. Go to "STAC Collections" → "New STAC Collection"
2. Fill in:
   - **ID**: `my-collection`
   - **Title**: "My Collection"
   - **Description**, **License**, **Extent**, etc.
3. **Use Helper Field**:
   - **Parent Catalog (Quick Add)**: Select "My Data Catalog"
4. Add required links:
   ```yaml
   Links:
     - Relation Type: Self
       URL: https://walkthru.earth/stac-cms-template/collections/my-collection.json
       Title: My Collection

     - Relation Type: Root
       URL: ../catalog/my-catalog.json
       Title: My Data Catalog

     - Relation Type: Parent
       URL: ../catalog/my-catalog.json
       Title: My Data Catalog
   ```
5. Save

#### 3. Go Back to Catalog - Add Child Link

**⚠️ IMPORTANT**: The catalog doesn't know about the collection yet!

1. Go to "STAC Catalogs" → Edit "My Data Catalog"
2. In the **Links** section, add:
   ```yaml
   - Relation Type: Child
     URL: ./collections/my-collection.json
     Title: My Collection
   ```
3. Save

#### 4. Create Item

1. Go to "STAC Items" → "New STAC Item"
2. Fill in:
   - **ID**: `my-item-001`
   - **Geometry**: Draw on map
   - **Bounding Box**: Set coordinates
   - **Properties**: Title, datetime, etc.
3. **✅ Use Automatic Relation**:
   - **Collection**: Select "My Collection" from dropdown
   - This automatically stores collection ID and creates collection link!
4. Add recommended links:
   ```yaml
   Links:
     - Relation Type: Self
       URL: https://walkthru.earth/stac-cms-template/items/my-item-001.json
       Title: My Item 001

     - Relation Type: Root
       URL: ../catalog/my-catalog.json
       Title: My Data Catalog

     - Relation Type: Parent
       URL: ../collections/my-collection.json
       Title: My Collection

     - Relation Type: Collection
       URL: ../collections/my-collection.json
       Title: My Collection
   ```
5. Save

#### 5. Go Back to Collection - Add Item Link

**⚠️ IMPORTANT**: The collection doesn't know about the item yet!

1. Go to "STAC Collections" → Edit "My Collection"
2. Check the **Items in This Collection (Quick Reference)** helper - it shows all items
3. In the **Links** section, add:
   ```yaml
   - Relation Type: Item
     URL: ../items/my-item-001.json
     Type: application/geo+json
     Title: My Item 001
   ```
4. Save

---

## Quick Reference Table

| Relationship | Automatic | Manual | How to Add |
|--------------|-----------|--------|------------|
| **Item → Collection** | ✅ Yes | ❌ No | Use "Collection" dropdown in Item |
| **Collection → Item** | ❌ No | ✅ Yes | Add "item" link in Collection |
| **Collection → Catalog** | ❌ No | ✅ Yes | Add "parent" link in Collection |
| **Catalog → Collection** | ❌ No | ✅ Yes | Add "child" link in Catalog |
| **Catalog → Sub-catalog** | ❌ No | ✅ Yes | Add "child" link in parent Catalog |
| **Sub-catalog → Parent** | ❌ No | ✅ Yes | Add "parent" link in sub-catalog |

---

## Link Type Reference

### For Items

| Relation | Required | Purpose | Example href |
|----------|----------|---------|--------------|
| **self** | Strongly Recommended | This item's URL | `https://example.com/items/item-1.json` |
| **root** | Recommended | Root catalog | `../catalog.json` |
| **parent** | Recommended | Parent collection or catalog | `../collections/my-collection.json` |
| **collection** | Required (if in collection) | Parent collection | `../collections/my-collection.json` |

### For Collections

| Relation | Required | Purpose | Example href |
|----------|----------|---------|--------------|
| **self** | Strongly Recommended | This collection's URL | `https://example.com/collections/my-collection.json` |
| **root** | Strongly Recommended | Root catalog | `../catalog.json` |
| **parent** | Recommended | Parent catalog | `../catalog.json` |
| **item** | Required for each item | Items in this collection | `../items/item-1.json` |
| **child** | Optional | Sub-collections | `../collections/sub-collection.json` |

### For Catalogs

| Relation | Required | Purpose | Example href |
|----------|----------|---------|--------------|
| **self** | Strongly Recommended | This catalog's URL | `https://example.com/catalog.json` |
| **root** | Strongly Recommended | Root catalog (can be self) | `./catalog.json` |
| **parent** | Recommended (if sub-catalog) | Parent catalog | `../catalog.json` |
| **child** | Recommended | Child catalogs or collections | `./collections/my-collection.json` |

---

## Common Patterns

### Pattern 1: Flat Structure (Single Catalog)

```
catalog/root.json
collections/
  ├─ aerial-imagery.json
  └─ satellite-data.json
items/
  ├─ aerial-001.json
  ├─ aerial-002.json
  ├─ satellite-001.json
  └─ satellite-002.json
```

**Links needed**:
- Root catalog → child links to both collections
- Each collection → parent link to root catalog
- Each collection → item links to its items
- Each item → collection link (automatic via dropdown)

### Pattern 2: Hierarchical (Multiple Catalogs)

```
catalog/
  ├─ root.json
  ├─ north-america.json
  └─ europe.json
collections/
  ├─ usa-imagery.json
  └─ eu-imagery.json
items/
  ├─ usa-001.json
  └─ eu-001.json
```

**Links needed**:
- Root catalog → child links to sub-catalogs
- Each sub-catalog → parent link to root, child links to collections
- Each collection → parent link to sub-catalog
- Each collection → item links to its items
- Each item → collection link (automatic via dropdown)

---

## Tips & Best Practices

### Use Helper Fields

The CMS provides helper relation fields to make management easier:

**In Catalogs**:
- "Child Collections (Quick Add)" - see all collections, helps you know what to link
- "Child Catalogs (Quick Add)" - see all sub-catalogs
- "Parent Catalog (Optional)" - select parent if this is a sub-catalog

**In Collections**:
- "Parent Catalog (Quick Add)" - select parent catalog
- "Items in This Collection (Quick Reference)" - shows all items that reference this collection

### Relative vs Absolute URLs

**Relative paths** (recommended for portability):
```
../catalog.json
./collections/my-collection.json
../items/my-item.json
```

**Absolute URLs** (required for `self` links):
```
https://walkthru.earth/stac-cms-template/catalog.json
```

### Link Titles

Always set the `title` field in links to match the title of the linked entity. This helps with:
- Better UX in STAC browsers
- Consistent metadata
- Easier debugging

### Media Types

- **application/json** - For Catalogs and Collections
- **application/geo+json** - For Items
- **text/html** - For documentation links

---

## Troubleshooting

### "My collection doesn't show items in STAC Browser"

**Problem**: Collection doesn't have `item` links to its items.

**Solution**: Go to the collection, add "item" links for each item in the Links section.

### "My items show up in the collection dropdown but not in the helper"

**Problem**: The helper uses filters to show items where `collection` field equals the collection ID.

**Solution**: Make sure you've selected the collection in the Item's "Collection" dropdown field.

### "Navigation broken in STAC Browser"

**Problem**: Missing `self`, `root`, or `parent` links.

**Solution**: Ensure all entities have:
- `self` link (absolute URL)
- `root` link (to main catalog)
- `parent` link (if not root)

---

## Multi-Catalog Support

Yes, you can have **multiple catalogs**!

### Independent Catalogs (Option 1)
```
catalog/
  ├─ aerial-catalog.json (root 1)
  ├─ satellite-catalog.json (root 2)
  └─ lidar-catalog.json (root 3)
```

Each catalog is independent, no cross-references needed.

### Hierarchical Catalogs (Option 2)
```
catalog/
  ├─ root.json (main root)
  ├─ catalog-a.json (sub-catalog)
  └─ catalog-b.json (sub-catalog)
```

Main root catalog has `child` links to sub-catalogs.
Sub-catalogs have `parent` links to root.

---

## Further Reading

- [STAC Specification](https://stacspec.org/)
- [STAC Best Practices](https://github.com/radiantearth/stac-spec/blob/master/best-practices.md)
- [STAC Link Relations](https://github.com/radiantearth/stac-spec/blob/master/commons/links.md)
- [Sveltia CMS Documentation](https://github.com/sveltia/sveltia-cms)
