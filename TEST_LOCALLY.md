# Local Testing Guide 🧪

Test the STAC CMS locally before deploying to GitHub.

---

## Quick Start

### 1. Start Local Server

Choose one of these methods:

**Python (Recommended - Usually Pre-installed)**
```bash
cd stac-cms-template
python3 -m http.server 8000
```

**Node.js (If you have Node installed)**
```bash
cd stac-cms-template
npx serve -p 8000
```

**PHP (If you have PHP installed)**
```bash
cd stac-cms-template
php -S localhost:8000
```

### 2. Open CMS

Open your browser to:
```
http://localhost:8000/admin/index-local.html
```

**No login required!** The test-repo backend runs in-memory.

### 3. Create a Test STAC Item

1. Click **"STAC Items"** in the sidebar
2. Click **"New STAC Item"**
3. Fill in the fields:
   - **ID**: `test-001`
   - **Geometry**: Click on the map to draw a polygon
     - Click to add points
     - Double-click to finish
   - **Bounding Box**: Click "Add Bounding Box" 4 times:
     - `-122.5` (minLon)
     - `37.7` (minLat)
     - `-122.4` (maxLon)
     - `37.8` (maxLat)
   - **Properties → Date & Time**: Select today
   - **Properties → Title**: "My Test Item"
   - **Links**: Add one link:
     - Relation: `self`
     - URL: `./test-001.json`
     - Type: `application/json`
   - **Assets → Thumbnail**:
     - URL: `https://via.placeholder.com/300x200.jpg`
     - Title: "Thumbnail"
     - Roles: `thumbnail`
4. Click **"Publish"** (in test mode, this shows you the JSON)
5. Copy the JSON!

### 4. Verify STAC Validity

**Option A: Copy-Paste to Online Validator**

1. Copy the JSON from the CMS
2. Go to [STAC Validator](https://stac-utils.github.io/stac-validator/)
3. Paste your JSON
4. Click "Validate"
5. Should see: ✅ "Valid STAC!"

**Option B: Command Line (If you have Python)**

```bash
# Install validator
pip install stac-validator

# Save your JSON to a file
# items/test-001.json

# Validate
stac-validator items/test-001.json
```

---

## What to Test

### ✅ Map Widget

**Test:**
1. Click on map to add points
2. Draw a polygon (at least 3 points)
3. Double-click to finish
4. Verify geometry appears in preview

**Expected:**
- Map loads with world view
- Can pan and zoom
- Can draw shapes
- Geometry coordinates appear correct

**Troubleshooting:**
- If map doesn't load, check internet connection (Leaflet loads from CDN)
- Try refreshing the page
- Check browser console for errors

### ✅ Nested Objects (Properties, Assets)

**Test:**
1. Fill in Properties → datetime
2. Add multiple assets
3. Verify nested structure in JSON

**Expected:**
- Can add/edit nested fields
- JSON structure is correct
- Fields are organized clearly

### ✅ Lists (BBox, Links, Roles)

**Test:**
1. Add 4 numbers to bbox
2. Add multiple links
3. Add multiple roles to assets

**Expected:**
- Can add list items
- Can reorder items
- Can delete items
- Arrays appear correct in JSON

### ✅ Select Widgets (Relation Types)

**Test:**
1. Try different link relation types
2. Change license types (in Collections)

**Expected:**
- Dropdown works
- Valid STAC relation types available

### ✅ Hidden Fields (type, stac_version)

**Test:**
1. Create an item
2. Check JSON includes `"type": "Feature"` and `"stac_version": "1.1.0"`

**Expected:**
- Hidden fields auto-populated
- Values are correct

### ✅ Collections

**Test:**
1. Click "STAC Collections"
2. Create a new collection
3. Fill in required fields
4. Verify JSON structure

**Expected:**
- Can create collections
- Extent object structured correctly
- Links array works

---

## Common Issues & Solutions

### Map Not Loading

**Problem:** Grey box instead of map
**Solution:**
- Check internet connection (Leaflet CDN)
- Try different browser
- Disable ad blockers
- Check browser console for errors

### Can't Draw Geometry

**Problem:** Clicking map does nothing
**Solution:**
- Make sure you're in the geometry field
- Try clicking "Edit" button if present
- Refresh page and try again

### JSON Looks Wrong

**Problem:** Structure doesn't match STAC spec
**Solution:**
- Check config-local.yml syntax
- Verify all required fields filled
- Compare with examples in `/items`, `/collections`

### Server Won't Start

**Problem:** Port 8000 already in use
**Solution:**
```bash
# Try a different port
python3 -m http.server 8001
# Then open: http://localhost:8001/admin/index-local.html
```

### Can't Save/Publish

**Problem:** Nothing happens when clicking Publish
**Solution:**
- This is normal for test-repo backend!
- Copy the JSON manually
- Or switch to git backend for real saves

---

## Next Steps After Testing

Once you've verified everything works:

### 1. Configure for GitHub

Edit `admin/config.yml`:
```yaml
backend:
  name: github  # Change from test-repo
  repo: YOUR-ORG/YOUR-REPO
```

### 2. Commit and Push

```bash
cd stac-cms-template

# Initialize git (if not already done)
git add .
git commit -m "Initial commit: STAC CMS template"

# Create GitHub repo and push
gh repo create walkthru-earth/stac-cms-template --public --source=. --remote=origin --push
```

### 3. Enable GitHub Pages

```bash
gh api repos/walkthru-earth/stac-cms-template/pages \
  --method POST \
  -f source[branch]=main \
  -f source[path]=/
```

### 4. Access Production CMS

After GitHub Pages deploys (1-2 mins):
```
https://walkthru-earth.github.io/stac-cms-template/admin/
```

---

## Testing Checklist

Before deploying to GitHub, verify:

- [ ] Map widget loads and works
- [ ] Can draw geometries (Point, Polygon, etc.)
- [ ] Can add bbox coordinates
- [ ] Can fill in all properties
- [ ] Can add links
- [ ] Can add assets with roles
- [ ] Hidden fields auto-populate
- [ ] Can create collections
- [ ] JSON validates with stac-validator
- [ ] All required STAC fields present
- [ ] Config syntax is valid

---

## Helpful Commands

```bash
# Start server (Python)
python3 -m http.server 8000

# Validate STAC file
stac-validator items/test-001.json

# Check config syntax
python3 -c "import yaml; yaml.safe_load(open('admin/config-local.yml'))"

# List all JSON files
find . -name "*.json" -not -path "./node_modules/*"

# Pretty-print JSON
cat items/test-001.json | python3 -m json.tool
```

---

## Resources

- [STAC Validator Online](https://stac-utils.github.io/stac-validator/)
- [STAC Examples](https://github.com/radiantearth/stac-spec/tree/master/examples)
- [Sveltia CMS Docs](https://github.com/sveltia/sveltia-cms)
- [Leaflet Docs](https://leafletjs.com/)

---

**Ready to test? Start your server and let's go! 🚀**
