# STAC CMS Template 🗺️

**A Git-based CMS for authoring STAC (SpatioTemporal Asset Catalog) metadata with a beautiful, user-friendly interface.**

[![STAC Validation](https://github.com/walkthru-earth/stac-cms-template/actions/workflows/validate-stac.yml/badge.svg)](https://github.com/walkthru-earth/stac-cms-template/actions/workflows/validate-stac.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## ✨ Features

- 🗺️ **Visual Map Editor** - Draw geometries with Leaflet + Terra Draw
- 📝 **STAC-Compliant** - Full support for Items, Collections, and Catalogs (STAC v1.1.0)
- 🚀 **No Server Required** - Fully static, git-based workflow
- 🎨 **Modern UI** - Built with Sveltia CMS (Decap CMS successor)
- ✅ **Automatic Validation** - GitHub Actions validate STAC on every commit
- 🌍 **Geospatial Native** - Designed specifically for geospatial metadata
- 📱 **Mobile Friendly** - Edit metadata from any device
- 🔒 **Version Control** - Full Git history for all metadata changes
- 🌙 **Dark Mode** - Easy on the eyes
- 🌐 **i18n Ready** - Multi-language support built-in

---

## 🚀 Quick Start

### 1. Use This Template

Click the **"Use this template"** button above to create your own repository, or:

```bash
gh repo create my-stac-catalog --template walkthru-earth/stac-cms-template --public
cd my-stac-catalog
```

### 2. Configure Your Repository

Edit `admin/config.yml` and update:

```yaml
backend:
  repo: YOUR-ORG/YOUR-REPO  # Your GitHub repository

site_url: https://YOUR-ORG.github.io/YOUR-REPO  # Your site URL
```

Also update the example JSON files in `catalog/`, `collections/`, and `items/` with your URLs.

### 3. Enable GitHub Pages

1. Go to **Settings** → **Pages**
2. Set **Source** to `main` branch
3. Set **Directory** to `/` (root)
4. Save

### 4. Access the CMS

Navigate to: `https://YOUR-ORG.github.io/YOUR-REPO/admin/`

Authenticate with GitHub and start editing!

---

## 📖 What is STAC?

[STAC (SpatioTemporal Asset Catalog)](https://stacspec.org/) is a specification for describing geospatial information, making it easier to index, discover, and work with spatiotemporal data.

**STAC Components:**

- **Item** - A GeoJSON feature representing a single spatiotemporal asset
- **Collection** - A group of Items with shared properties
- **Catalog** - A structure for organizing Collections and Items

---

## 📁 Repository Structure

```
stac-cms-template/
├── admin/
│   ├── index.html          # CMS entry point
│   └── config.yml          # CMS configuration
├── catalog/
│   └── root.json           # Root STAC Catalog
├── collections/
│   └── example-collection.json
├── items/
│   └── example-item.json
├── assets/                 # Media uploads
├── .github/
│   └── workflows/
│       └── validate-stac.yml  # Auto-validation
└── README.md
```

---

## 🎨 CMS Features

### Map Widget

Draw geometries directly on an interactive map:
- **Point** - Single coordinates
- **LineString** - Linear features
- **Polygon** - Areas (default for STAC Items)
- **Multi-types** - Complex geometries

### STAC Fields

All STAC-required fields are pre-configured:
- ✅ Geometry editor with visual map
- ✅ Bounding box (manual or auto-calculated)
- ✅ Properties (datetime, title, description)
- ✅ Assets (downloadable files)
- ✅ Links (relationships between STAC objects)
- ✅ Collection references
- ✅ Extensions support

### Validation

GitHub Actions automatically validate all STAC JSON files on commit:
```bash
# Validates against STAC v1.1.0 specification
stac-validator items/*.json
stac-validator collections/*.json
stac-validator catalog/*.json
```

---

## 🛠️ Local Development

### Option 1: Test Backend (No Git, In-Memory)

Edit `admin/config.yml`:

```yaml
backend:
  name: test-repo
```

Refresh the CMS - no authentication needed!

### Option 2: Local Git Repository (Recommended)

Sveltia CMS supports editing local files:

1. Open `https://localhost:8000/admin/` (use any local server)
2. Click **"Work with Local Repository"**
3. Select your repository folder
4. Edit files directly!

No proxy server needed! 🎉

### Option 3: GitHub Proxy

For Decap CMS compatibility:

```bash
npx decap-server
```

Edit `admin/config.yml`:

```yaml
backend:
  name: github
local_backend: true
```

---

## 📝 Creating Content

### Creating a STAC Item

1. Go to **STAC Items** → **New STAC Item**
2. Fill in required fields:
   - **ID**: Unique identifier
   - **Geometry**: Draw on the map
   - **Bounding Box**: [minLon, minLat, maxLon, maxLat]
   - **Properties → Date/Time**: Acquisition datetime
   - **Links**: At least one link (usually to collection)
   - **Assets**: At least one asset (e.g., thumbnail)
3. **Save** → Creates `items/{id}.json`

### Creating a STAC Collection

1. Go to **STAC Collections** → **New STAC Collection**
2. Fill in required fields:
   - **ID**: Unique identifier
   - **Title**: Human-readable name
   - **Description**: Detailed description
   - **License**: Data license
   - **Extent**: Spatial and temporal bounds
   - **Links**: At least one link
3. **Save** → Creates `collections/{id}.json`

### Creating a STAC Catalog

1. Go to **STAC Catalogs** → **New STAC Catalog**
2. Fill in:
   - **ID**: Unique identifier
   - **Title**: Catalog name
   - **Description**: Purpose
   - **Links**: Links to children
3. **Save** → Creates `catalog/{id}.json`

---

## 🔗 Linking STAC Objects

### Item → Collection

In a STAC Item:

```yaml
Collection: example-collection  # Use the relation widget
```

In the JSON:

```json
{
  "collection": "example-collection",
  "links": [
    {
      "rel": "collection",
      "href": "../collections/example-collection.json"
    }
  ]
}
```

### Catalog → Collection

In a STAC Catalog:

```yaml
Links:
  - Relation Type: child
    URL: ../collections/example-collection.json
    Title: Example Collection
```

---

## 🧪 Validation

### Automatic (GitHub Actions)

Validation runs automatically on:
- Every commit to `main`
- Every pull request

### Manual (Local)

```bash
# Install validator
pip install stac-validator

# Validate files
stac-validator items/my-item.json
stac-validator collections/my-collection.json
stac-validator catalog/root.json

# Validate entire catalog
find . -name "*.json" -not -path "./node_modules/*" -exec stac-validator {} \;
```

---

## 🌐 Deployment

### GitHub Pages (Recommended)

Already configured! Your STAC catalog is automatically available at:

```
https://YOUR-ORG.github.io/YOUR-REPO/
```

Access the CMS at:

```
https://YOUR-ORG.github.io/YOUR-REPO/admin/
```

### Netlify

1. Connect your GitHub repository
2. Build settings: **None** (static site)
3. Publish directory: `/`
4. Deploy!

### Vercel, Cloudflare Pages, etc.

All work out of the box - just connect and deploy! ✨

---

## 📚 Documentation

- [STAC Specification](https://stacspec.org/en/about/stac-spec/)
- [Sveltia CMS Documentation](https://github.com/sveltia/sveltia-cms)
- [STAC Best Practices](https://github.com/radiantearth/stac-spec/blob/master/best-practices.md)
- [STAC Extensions](https://stac-extensions.github.io/)

---

## 🤝 Contributing

Contributions welcome! This template is designed to be:

- ✅ Easy to use for non-technical users
- ✅ Flexible for advanced users
- ✅ STAC specification compliant
- ✅ Well-documented

### Ideas for Improvement

- [ ] Additional STAC Extensions support
- [ ] Auto-calculate bbox from geometry
- [ ] Asset preview/upload
- [ ] Bulk import from existing STAC catalogs
- [ ] Custom preview templates
- [ ] STAC API integration

---

## 🐛 Troubleshooting

### "Failed to load config" error

Check that `admin/config.yml` has:
- Correct repository name
- Valid YAML syntax
- Proper indentation (2 spaces)

### Authentication issues

- Make sure you're accessing via HTTPS (or localhost)
- GitHub backend requires proper OAuth setup
- For testing, use `backend: { name: test-repo }`

### Validation failures

- Use [STAC Validator online](https://stac-utils.github.io/stac-validator/) to check files
- Ensure all required fields are present
- Check that URLs/hrefs are valid
- Verify geometry coordinates are valid GeoJSON

### Map not loading

- Check browser console for errors
- Ensure you have internet connection (Leaflet loads from CDN)
- Try clearing browser cache

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

This template uses:
- [Sveltia CMS](https://github.com/sveltia/sveltia-cms) - MIT License
- [STAC Specification](https://github.com/radiantearth/stac-spec) - Apache 2.0 License
- [Leaflet](https://leafletjs.com/) - BSD 2-Clause License

---

## 🙏 Acknowledgements

- [Sveltia CMS](https://github.com/sveltia/sveltia-cms) - Incredible CMS foundation
- [STAC Community](https://stacspec.org/) - Excellent specification and tools
- [Walkthru Earth](https://github.com/walkthru-earth) - Project maintainers

---

## 🌟 Show Your Support

If this template helped you, please:
- ⭐ Star this repository
- 🐛 Report issues
- 💡 Suggest improvements
- 🔀 Submit pull requests
- 📢 Share with others!

---

**Happy STAC authoring! 🗺️✨**
