# STAC CMS Template 🗺️

**A Git-based CMS for authoring STAC (SpatioTemporal Asset Catalog) metadata with a beautiful, user-friendly interface.**

[![STAC Validation](https://github.com/walkthru-earth/stac-cms-template/actions/workflows/validate-stac.yml/badge.svg)](https://github.com/walkthru-earth/stac-cms-template/actions/workflows/validate-stac.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## ✨ Features

- 🗺️ **Visual Map Editor** - Draw geometries with Leaflet + Terra Draw
- 📦 **Auto-Calculate Bbox** - Automatically calculated from geometry
- 📝 **STAC v1.1.0 Compliant** - Items, Collections, and Catalogs
- 🚀 **No Server Required** - Fully static, git-based workflow
- 🎨 **Modern UI** - Built with Sveltia CMS (Decap CMS successor)
- ✅ **Auto-Validation** - GitHub Actions with uv (10-100x faster than pip)
- 🔒 **Version Control** - Full Git history for all metadata changes
- 🌐 **Deploy Anywhere** - GitHub Pages, Netlify, Vercel, Cloudflare Pages

---

## 🚀 Quick Start

**New here?** See [**5-Minute Quick Start Guide**](docs/QUICK_START.md) 📊

### 1. Create Repository

```bash
gh repo create my-stac-catalog --template walkthru-earth/stac-cms-template --public
cd my-stac-catalog
```

Or click **"Use this template"** button above.

### 2. Configure

Edit `admin/config.yml`:

```yaml
backend:
  repo: YOUR-ORG/YOUR-REPO

site_url: https://YOUR-ORG.github.io/YOUR-REPO
```

### 3. Enable GitHub Pages

**Settings** → **Pages** → Source: `main` branch → Directory: `/` → **Save**

### 4. Access CMS

Navigate to: `https://YOUR-ORG.github.io/YOUR-REPO/admin/`

Login with GitHub and start authoring! 🎉

---

## 📖 What is STAC?

[STAC (SpatioTemporal Asset Catalog)](https://stacspec.org/) is a specification for describing geospatial information, making it easier to index, discover, and work with spatiotemporal data.

**Three components:**
- **Item** - A GeoJSON feature representing a single spatiotemporal asset
- **Collection** - A group of Items with shared properties
- **Catalog** - A structure for organizing Collections and Items

---

## 📚 Documentation

### Guides
- [**Quick Start**](docs/QUICK_START.md) - Get started in 5 minutes with visual diagrams
- [**Setup Guide**](docs/SETUP_GUIDE.md) - Detailed setup, OAuth, and advanced customization
- [**Features**](docs/FEATURES.md) - Complete feature list and technical details
- [**STAC Relationships**](docs/STAC-RELATIONSHIPS.md) - Managing catalog/collection/item relationships
- [**Local Testing**](docs/TEST_LOCALLY.md) - Test the CMS locally before deploying

### External Resources
- [STAC Specification](https://stacspec.org/) - Official STAC documentation
- [Sveltia CMS](https://github.com/sveltia/sveltia-cms) - CMS documentation
- [STAC Extensions](https://stac-extensions.github.io/) - Available extensions
- [uv Documentation](https://github.com/astral-sh/uv) - Fast Python package manager

---

## 🛠️ Local Development

**Quick test** (no authentication):

1. Start local server: `python3 -m http.server 8000`
2. Open: `http://localhost:8000/admin/index-local.html`
3. Edit and test without Git commits

**With Git** (recommended):

1. Start server: `python3 -m http.server 8000`
2. Open: `http://localhost:8000/admin/`
3. Click **"Work with Local Repository"**
4. Select folder and edit directly!

No proxy needed! See [TEST_LOCALLY.md](docs/TEST_LOCALLY.md) for details.

---

## 🧪 Validation

**Automatic** - Every commit and PR:
- GitHub Actions validates all STAC files
- Uses `uv` for 10-100x faster validation
- Blocks merge if validation fails

**Manual** - Local testing:
```bash
# Install uv (one-time)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Validate files
uvx stac-validator items/my-item.json
```

See [FEATURES.md](docs/FEATURES.md#-automatic-validation) for details.

---

## 📁 Repository Structure

```
stac-cms-template/
├── admin/              # CMS interface and configuration
├── catalog/            # Editable STAC catalogs (CMS managed)
├── collections/        # STAC Collections
├── items/              # STAC Items
├── assets/             # Media uploads
├── docs/               # Documentation
├── .github/workflows/  # CI/CD validation
└── catalog.json        # Published root (auto-copied)
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| CMS won't load | Check `admin/config.yml` repo name and YAML syntax |
| Map not showing | Check internet connection (Leaflet loads from CDN) |
| Validation fails | Run `uvx stac-validator your-file.json` for details |
| Can't save | Check GitHub write permissions |
| Authentication issues | Use `backend: {name: test-repo}` for testing |

See [SETUP_GUIDE.md](docs/SETUP_GUIDE.md#troubleshooting) for more help.

---

## 🤝 Contributing

Contributions welcome! Please:
- ⭐ Star this repository
- 🐛 [Report issues](https://github.com/walkthru-earth/stac-cms-template/issues)
- 💡 [Suggest improvements](https://github.com/walkthru-earth/stac-cms-template/discussions)
- 🔀 Submit pull requests
- 📢 Share with the STAC community!

### Ideas for Improvement
- [ ] Additional STAC Extensions (eo, view, projection, etc.)
- [ ] Bulk import from existing STAC catalogs
- [ ] STAC API integration
- [ ] Custom preview templates

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

**Uses:**
- [Sveltia CMS](https://github.com/sveltia/sveltia-cms) - MIT License
- [STAC Specification](https://github.com/radiantearth/stac-spec) - Apache 2.0
- [Leaflet](https://leafletjs.com/) - BSD 2-Clause

---

## 🙏 Acknowledgements

- [Sveltia CMS](https://github.com/sveltia/sveltia-cms) - Modern CMS foundation
- [STAC Community](https://stacspec.org/) - Excellent specification and tools
- [Walkthru Earth](https://github.com/walkthru-earth) - Project maintainers

---

**Happy STAC authoring! 🗺️✨**
