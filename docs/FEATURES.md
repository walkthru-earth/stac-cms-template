# STAC CMS Features

Complete guide to CMS features and capabilities.

---

## 🗺️ Map Widget

Draw geometries directly on an interactive map powered by Leaflet + Terra Draw:

### Supported Geometry Types
- **Point** - Single coordinates
- **LineString** - Linear features (roads, paths)
- **Polygon** - Areas (default for STAC Items)
- **MultiPoint** - Multiple points
- **MultiLineString** - Multiple lines
- **MultiPolygon** - Complex areas

### Map Features
- Pan and zoom controls
- Geocoding search (Nominatim)
- Draw, edit, and delete geometries
- Configurable decimal precision
- Mobile-friendly interface
- Automatic coordinate validation

---

## 📝 STAC Fields

All STAC-required fields are pre-configured and ready to use:

### Core Fields
- ✅ **ID** - Unique identifier (string)
- ✅ **Type** - Auto-set to "Feature" (hidden field)
- ✅ **STAC Version** - Auto-set to "1.1.0" (hidden field)
- ✅ **Geometry** - Visual map editor with automatic object conversion
- ✅ **Bbox** - Auto-calculated from geometry (can override manually)
- ✅ **Properties** - Nested object with datetime, title, description, etc.
- ✅ **Links** - Array of relationships (root, parent, collection, self)
- ✅ **Assets** - Downloadable files with roles and media types
- ✅ **Collection** - Reference to parent collection (relation widget)

### Properties Fields
- **datetime** - Required acquisition/creation timestamp (ISO 8601)
- **title** - Human-readable title
- **description** - Detailed description
- **start_datetime** - For time ranges
- **end_datetime** - For time ranges
- **created** - Metadata creation date
- **updated** - Metadata update date

### Link Relation Types
- **self** - This item's URL (strongly recommended)
- **root** - Root catalog (recommended)
- **parent** - Parent catalog/collection (recommended)
- **collection** - Parent collection (required for items)
- **item** - Child items (for collections)
- **child** - Child catalogs/collections (for catalogs)
- **derived_from** - Source data
- **license** - License information

---

## ✅ Automatic Validation

### GitHub Actions Integration

Every commit and pull request triggers automatic validation:

```yaml
# Validates on:
- Every push to main branch
- Every pull request
- Any changes to *.json files
```

**Validation Process**:
1. Install `uv` (10-100x faster than pip)
2. Install `stac-validator`
3. Validate all items/*.json
4. Validate all collections/*.json
5. Validate all catalog/*.json
6. Auto-copy catalog/root.json → catalog.json
7. Block merge if validation fails

### Local Validation

**Using uv (recommended)**:
```bash
# One-time setup
curl -LsSf https://astral.sh/uv/install.sh | sh
uv tool install stac-validator

# Validate files
uvx stac-validator items/my-item.json
uvx stac-validator collections/my-collection.json
uvx stac-validator catalog/root.json

# Validate all
find . -name "*.json" -not -path "./node_modules/*" -exec uvx stac-validator {} \;
```

**Using pip (slower)**:
```bash
pip install stac-validator
stac-validator items/my-item.json
```

**Why uv?**
- ⚡ 10-100x faster than pip
- 🔒 Better dependency resolution
- 📦 Minimal disk space
- ✅ Industry best practice

---

## 🔄 Custom Format Handler

### Geometry Conversion

The map widget stores geometry as **STRING**, but STAC requires **OBJECT**.

Our custom format handler (`admin/stac-format.js`) automatically converts:

**On Load (Git → CMS)**:
```javascript
// File in Git: geometry as object
{ "geometry": {"type": "Polygon", "coordinates": [...]} }

// Converted to string for map widget
{ "geometry": "{\"type\":\"Polygon\",\"coordinates\":[...]}" }
```

**On Save (CMS → Git)**:
```javascript
// CMS has: geometry as string
{ "geometry": "{\"type\":\"Polygon\",\"coordinates\":[...]}" }

// Converted to object for STAC compliance
{ "geometry": {"type": "Polygon", "coordinates": [...]} }
```

Files in Git are **always STAC-compliant** ✅

### Bbox Auto-Calculation

The format handler also calculates bbox from geometry:

```javascript
// Input: User draws polygon
{
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[-122.5, 37.7], [-122.4, 37.8], ...]]
  }
}

// Output: Bbox automatically calculated
{
  "geometry": {...},
  "bbox": [-122.5, 37.7, -122.4, 37.8]  // [minLon, minLat, maxLon, maxLat]
}
```

**Benefits**:
- No manual calculation needed
- Prevents human error
- Always matches geometry
- STAC best practice

---

## 🔗 Relationship Management

### Automatic Relations

**Item → Collection** (✅ Automatic):
- Use the "Collection" dropdown in items
- Automatically creates `collection` field
- Automatically adds collection link

### Manual Relations

All other relationships require manual linking:

**Collection → Items**:
- Add "item" links in collection
- Must be done manually for each item

**Collection → Catalog**:
- Add "parent" link in collection pointing to catalog
- Add "child" link in catalog pointing to collection

**Catalog → Sub-catalogs**:
- Add "child" links in parent catalog
- Add "parent" link in sub-catalog

### Helper Fields

The CMS provides helper relation widgets to make linking easier:

**In Collections**:
- "Items in This Collection" - Shows all items that reference this collection
- "Parent Catalog" - Dropdown to select parent catalog

**In Catalogs**:
- "Child Collections" - Shows all collections to link to
- "Child Catalogs" - Shows all sub-catalogs to link to

See [STAC-RELATIONSHIPS.md](STAC-RELATIONSHIPS.md) for complete guide.

---

## 📦 Repository Structure

```
stac-cms-template/
├── admin/
│   ├── index.html          # CMS entry point
│   ├── config.yml          # Complete STAC configuration
│   └── stac-format.js      # Custom geometry + bbox handler
├── catalog/
│   └── root.json           # Editable root catalog (CMS managed)
├── collections/
│   └── *.json              # STAC Collections
├── items/
│   └── *.json              # STAC Items
├── assets/
│   └── *.*                 # Media uploads (images, thumbnails)
├── .github/workflows/
│   └── validate-stac.yml   # Auto-validation
├── catalog.json            # Published root (auto-copied)
└── docs/                   # Documentation
```

**Key Points**:
- 🌟 `catalog.json` at root - Published catalog (auto-copied from catalog/root.json)
- 📝 `catalog/root.json` - Editable version (managed via CMS)
- 📚 `docs/` - All documentation
- 🎨 `admin/` - CMS interface
- 📦 STAC data in standard folders

---

## 🌐 Deployment Options

### GitHub Pages (Recommended)

**Already configured!** Just enable in repository settings.

**URLs**:
- Catalog: `https://YOUR-ORG.github.io/YOUR-REPO/catalog.json`
- CMS: `https://YOUR-ORG.github.io/YOUR-REPO/admin/`

**Setup**:
1. Settings → Pages
2. Source: `main` branch
3. Directory: `/` (root)
4. Save

### Netlify

1. Connect GitHub repository
2. Build settings: **None** (static site)
3. Publish directory: `/`
4. Deploy

### Vercel

1. Import GitHub repository
2. Framework: **Other**
3. Build: Leave empty
4. Deploy

### Cloudflare Pages

1. Connect repository
2. Build command: (empty)
3. Output directory: `/`
4. Deploy

All platforms work out of the box! ✨

---

## 🎨 UI Features

### Built-in Sveltia CMS Features

- **Dark Mode** - Automatic theme switching
- **Mobile Friendly** - Responsive design
- **i18n Ready** - Multi-language support
- **Search** - Find items quickly
- **Filters** - Filter by collection, date, etc.
- **Preview** - Preview JSON before saving
- **Drafts** - Editorial workflow support
- **Media Library** - Upload and manage assets

### Workflow Modes

**Simple Workflow** (default):
- Save → Commits directly to main
- Fast and simple

**Editorial Workflow**:
```yaml
publish_mode: editorial_workflow
```
- Draft → In Review → Publish
- Creates pull requests
- Review before merge

---

## 🔒 Security & Authentication

### GitHub OAuth

**Required for production use**:
1. Create GitHub OAuth App
2. Configure callback URL
3. Set client ID/secret

See [SETUP_GUIDE.md](SETUP_GUIDE.md#step-4-set-up-github-oauth) for details.

### OAuth Proxy

This template uses:
```yaml
base_url: https://opensensor-auth.walkthru-earth.workers.dev
```

You can deploy your own Cloudflare Worker or use Netlify Identity.

### Test Mode

For local testing without authentication:
```yaml
backend:
  name: test-repo
```

No OAuth needed! Perfect for development.

---

## 🧩 STAC Extensions

The template supports adding STAC extensions via config customization:

### Example: EO Extension

```yaml
# In admin/config.yml - add to items fields:
- label: 'Cloud Cover'
  name: 'properties.eo:cloud_cover'
  widget: 'number'
  value_type: 'float'
  min: 0
  max: 100
  hint: 'Percentage of cloud cover (0-100)'

- label: 'Bands'
  name: 'properties.eo:bands'
  widget: 'list'
  fields:
    - {label: 'Name', name: 'name', widget: 'string'}
    - {label: 'Common Name', name: 'common_name', widget: 'string'}
```

### Popular Extensions

- **EO** - Electro-Optical imagery
- **SAR** - Synthetic Aperture Radar
- **Projection** - Map projections
- **View** - Viewing geometry
- **Scientific** - Scientific data
- **Datacube** - Data cubes

See [STAC Extensions](https://stac-extensions.github.io/) for complete list.

---

## 📊 Performance

### Bundle Size
- **Sveltia CMS**: ~500 KB
- **Leaflet**: ~140 KB
- **Total**: < 700 KB

**3x smaller than Decap CMS** (1.5 MB)

### Load Times
- **First load**: < 2 seconds
- **Cached load**: < 500ms
- **No build step**: Instant deployment

### Validation Speed
- **uv**: 10-100x faster than pip
- **Typical validation**: < 2 seconds per file
- **CI/CD time**: 15-30 seconds total

---

## 🔧 Customization

### Adding Custom Fields

Edit `admin/config.yml`:

```yaml
collections:
  - name: stac-items
    fields:
      # Add after existing fields
      - label: 'My Custom Field'
        name: 'properties.custom_field'
        widget: 'string'
        required: false
        hint: 'Your custom field description'
```

### Changing Geometry Type

```yaml
- label: 'Geometry'
  name: 'geometry'
  widget: 'map'
  type: 'Point'  # Change to: LineString, Polygon, etc.
```

### Adding Media Transformations

```yaml
media_folder: assets
public_folder: /YOUR-REPO/assets
media_library:
  max_file_size: 5120000  # 5 MB
```

---

## 🎓 Learning Resources

- [STAC Specification](https://stacspec.org/)
- [STAC Best Practices](https://github.com/radiantearth/stac-spec/blob/master/best-practices.md)
- [Sveltia CMS Docs](https://github.com/sveltia/sveltia-cms)
- [STAC Extensions](https://stac-extensions.github.io/)
- [STAC Browser](https://github.com/radiantearth/stac-browser)
- [STAC Index](https://stacindex.org/)

---

**Need help?** See [SETUP_GUIDE.md](SETUP_GUIDE.md) or [open an issue](https://github.com/walkthru-earth/stac-cms-template/issues).
