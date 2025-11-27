# STAC CMS Setup Guide 🚀

Complete step-by-step guide for setting up your STAC CMS.

---

## Prerequisites

- GitHub account
- Git installed locally
- Text editor (VS Code recommended)
- Basic understanding of Git workflows

---

## Step 1: Create Repository from Template

### Option A: GitHub Web Interface

1. Go to https://github.com/walkthru-earth/stac-cms-template
2. Click **"Use this template"** button (top right)
3. Select **"Create a new repository"**
4. Fill in:
   - **Owner**: Your organization or username
   - **Repository name**: e.g., `my-stac-catalog`
   - **Description**: "STAC metadata for [your project]"
   - **Public** or **Private** (recommend Public for STAC catalogs)
5. Click **"Create repository"**

### Option B: GitHub CLI

```bash
# Create from template
gh repo create my-stac-catalog \
  --template walkthru-earth/stac-cms-template \
  --public \
  --clone

cd my-stac-catalog
```

---

## Step 2: Configure the CMS

### Edit `admin/config.yml`

```yaml
backend:
  name: github
  repo: YOUR-ORG/YOUR-REPO  # ← Change this!
  branch: main

site_url: https://YOUR-ORG.github.io/YOUR-REPO  # ← Change this!
```

**Example:**
```yaml
backend:
  name: github
  repo: walkthru-earth/earth-observations
  branch: main

site_url: https://walkthru-earth.github.io/earth-observations
```

### Update Example Files

Replace placeholder URLs in these files:

**`catalog/root.json`:**
```json
{
  "links": [
    {
      "rel": "self",
      "href": "https://YOUR-ORG.github.io/YOUR-REPO/catalog/root.json"
      // ↑ Update this
    }
  ]
}
```

Do the same for:
- `collections/example-collection.json`
- `items/example-item.json`

Or just delete these files and create new ones via the CMS!

---

## Step 3: Enable GitHub Pages

### Via GitHub Web Interface

1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. Scroll to **Pages** (left sidebar)
4. Under **Source**:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**
6. Wait 1-2 minutes for deployment

### Via GitHub CLI

```bash
# Enable GitHub Pages
gh api repos/YOUR-ORG/YOUR-REPO/pages \
  --method POST \
  -f source[branch]=main \
  -f source[path]=/
```

### Verify Deployment

After 1-2 minutes, visit:
```
https://YOUR-ORG.github.io/YOUR-REPO/admin/
```

You should see the Sveltia CMS login screen! 🎉

---

## Step 4: Set Up GitHub OAuth (For Authentication)

### Option A: GitHub OAuth App (Recommended for Organizations)

1. Go to GitHub Settings → Developer settings → OAuth Apps
2. Click **"New OAuth App"**
3. Fill in:
   - **Application name**: `STAC CMS - [Your Repo]`
   - **Homepage URL**: `https://YOUR-ORG.github.io/YOUR-REPO`
   - **Authorization callback URL**: `https://api.netlify.com/auth/done`
4. Click **"Register application"**
5. Copy **Client ID**
6. Generate and copy **Client Secret**

### Configure OAuth

**Option 1: Netlify Identity (Easiest)**

1. Deploy to Netlify (or use GitHub Pages with Netlify for OAuth only)
2. Enable Netlify Identity
3. Configure GitHub as external provider with your OAuth credentials

**Option 2: Self-hosted OAuth Gateway**

Use [decap-server](https://github.com/decaporg/decap-cms/tree/master/packages/decap-server) or similar.

### Option B: GitHub App (Advanced)

More secure, fine-grained permissions. See [GitHub Apps documentation](https://docs.github.com/en/apps).

---

## Step 5: Test the CMS

### Access the CMS

1. Go to `https://YOUR-ORG.github.io/YOUR-REPO/admin/`
2. Click **"Login with GitHub"**
3. Authorize the application
4. You're in! 🎉

### Create Your First STAC Item

1. Click **"STAC Items"** in the sidebar
2. Click **"New STAC Item"**
3. Fill in the fields:
   - **ID**: `test-item-001`
   - **Geometry**: Click the map to draw a polygon
   - **Bounding Box**: `[-122.5, 37.7, -122.4, 37.8]`
   - **Properties → Date & Time**: Select today's date
   - **Links**: Add a link to your collection
   - **Assets → Thumbnail**: Add a thumbnail URL
4. Click **"Save"**
5. Click **"Publish"** (or create a pull request if using editorial workflow)

### Verify the File

Check your repository - you should see:
```
items/test-item-001.json
```

The GitHub Action will automatically validate it! ✅

---

## Step 6: Customize for Your Use Case

### Modify Collections Configuration

Edit `admin/config.yml` to add or remove fields:

```yaml
collections:
  - name: stac-items
    fields:
      # Add custom fields here
      - label: 'Custom Field'
        name: 'custom_field'
        widget: 'string'
```

### Add STAC Extensions

To support STAC extensions, add fields to the configuration:

```yaml
# Example: EO Extension
- label: 'Cloud Cover'
  name: 'properties.eo:cloud_cover'
  widget: 'number'
  value_type: 'float'
  min: 0
  max: 100
  hint: 'Percentage of cloud cover'
```

### Customize Geometry Types

Change the default geometry type:

```yaml
- label: 'Geometry'
  name: 'geometry'
  widget: 'map'
  type: 'Point'  # or LineString, Polygon, MultiPoint, etc.
```

---

## Step 7: Set Up Local Development (Optional)

### Option A: Local Git Repository (Recommended)

Sveltia CMS supports editing local files:

```bash
# Serve your repository locally
python -m http.server 8000
# or: npx serve

# Open in browser
open http://localhost:8000/admin/
```

Click **"Work with Local Repository"** and select your folder!

No proxy needed! 🚀

### Option B: GitHub Proxy (For Decap CMS Compatibility)

```bash
# Install proxy
npm install -g decap-server

# Run proxy
npx decap-server
```

Edit `admin/config.yml`:

```yaml
backend:
  name: github
local_backend: true  # Enable local proxy
```

---

## Step 8: Workflow Configuration

### Editorial Workflow (Recommended)

Use pull requests for reviewing changes:

```yaml
publish_mode: editorial_workflow
```

**Workflow:**
1. Create content → **Draft**
2. Click **"Set to Review"** → **In Review**
3. Click **"Publish"** → Creates PR
4. Merge PR → Content goes live

### Simple Workflow

Commit directly to main:

```yaml
publish_mode: simple
```

**Workflow:**
1. Create content
2. Click **"Publish"** → Commits directly

---

## Step 9: Validation Setup

The GitHub Action is already configured! It will:

1. Run on every commit to `main`
2. Run on every pull request
3. Validate all STAC JSON files
4. Report errors

### Test Validation Locally

**Recommended: Use uv (10-100x faster)**

```bash
# Install uv (one-time setup)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install validator
uv tool install stac-validator

# Validate a file
uvx stac-validator items/test-item-001.json

# Validate all files
find . -name "*.json" -not -path "./node_modules/*" -exec uvx stac-validator {} \;
```

**Alternative: Use pip (slower)**

```bash
pip install stac-validator
stac-validator items/test-item-001.json
```

---

## Step 10: Share Your Catalog

### STAC Browser

Deploy a [STAC Browser](https://github.com/radiantearth/stac-browser) to visualize your catalog:

```bash
# Clone STAC Browser
git clone https://github.com/radiantearth/stac-browser.git

# Configure for your catalog
# Edit config.js to point to your catalog root
```

### STAC Index

Add your catalog to [STAC Index](https://stacindex.org/) for discovery.

### Documentation

Add to your README:
- Catalog URL
- Browser URL (if deployed)
- Contact information
- Data license
- Usage examples

---

## Troubleshooting

### CMS Won't Load

1. Check browser console for errors
2. Verify `admin/config.yml` syntax (use YAML validator)
3. Ensure repository name is correct
4. Try clearing browser cache

### Authentication Fails

1. Verify OAuth app settings
2. Check callback URL matches exactly
3. Ensure repository access permissions
4. Try incognito/private browsing

### Validation Fails

1. Run `stac-validator` locally to see detailed errors
2. Check for missing required fields
3. Verify JSON syntax (use JSON validator)
4. Ensure geometry coordinates are valid

### Map Not Working

1. Check internet connection (Leaflet loads from CDN)
2. Verify browser supports modern JavaScript
3. Check browser console for errors
4. Try different browser

### Changes Not Saving

1. Check GitHub permissions (write access)
2. Verify branch name in config
3. Check for conflicts with editorial workflow
4. Look at browser network tab for errors

---

## Next Steps

Now that your STAC CMS is set up:

1. ✅ Delete example files
2. ✅ Create your first collection
3. ✅ Add real items
4. ✅ Customize field configurations
5. ✅ Set up STAC Browser
6. ✅ Add to STAC Index
7. ✅ Invite collaborators
8. ✅ Document your catalog

---

## Support

- 🐛 [Report issues](https://github.com/walkthru-earth/stac-cms-template/issues)
- 💬 [Discussions](https://github.com/walkthru-earth/stac-cms-template/discussions)
- 📖 [STAC Specification](https://stacspec.org/)
- 📘 [Sveltia CMS Docs](https://github.com/sveltia/sveltia-cms)

---

**Happy STAC authoring! 🗺️✨**
