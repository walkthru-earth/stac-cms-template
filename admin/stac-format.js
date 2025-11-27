/**
 * Custom STAC JSON Format for Sveltia CMS
 *
 * This format handles the round-trip conversion between:
 * - Git storage: geometry as JSON object (STAC spec compliant)
 * - CMS editor: geometry as stringified JSON (map widget requirement)
 *
 * The map widget in Sveltia CMS requires geometry to be a stringified GeoJSON,
 * but STAC spec requires it to be a proper JSON object. This format converter
 * transparently handles the transformation at the file boundary.
 */

/**
 * Parse STAC JSON file from Git storage format to CMS edit format
 * Converts: geometry object → geometry string (for map widget)
 *
 * @param {string} text - Raw JSON file content from Git
 * @returns {Object} - Parsed object with geometry as string
 */
const fromFile = (text) => {
  const data = JSON.parse(text);

  // Only process STAC Items (Features)
  if (data.type === 'Feature' && data.geometry) {
    // If geometry is already an object (from Git after CI processing),
    // stringify it for the map widget
    if (typeof data.geometry === 'object') {
      data.geometry = JSON.stringify(data.geometry);
      console.log('🔄 [STAC Format] Converted geometry object → string for map widget');
    }
  }

  return data;
};

/**
 * Format STAC JSON from CMS edit format to Git storage format
 * Converts: geometry string → geometry object (STAC compliant)
 *
 * @param {Object} data - Entry data from CMS with geometry as string
 * @returns {string} - JSON string ready for Git with geometry as object
 */
const toFile = (data) => {
  // Clone to avoid mutating original
  const output = JSON.parse(JSON.stringify(data));

  // Only process STAC Items (Features)
  if (output.type === 'Feature' && output.geometry) {
    // If geometry is a string (from map widget), parse it to object
    if (typeof output.geometry === 'string') {
      try {
        output.geometry = JSON.parse(output.geometry);
        console.log('✅ [STAC Format] Converted geometry string → object for STAC compliance');
      } catch (e) {
        console.error('❌ [STAC Format] Failed to parse geometry string:', e);
        // Keep as string if parsing fails
      }
    }
  }

  // Return formatted JSON with proper indentation
  return JSON.stringify(output, null, 2);
};

// Register the custom format with Sveltia CMS
CMS.registerCustomFormat('stac-json', 'json', {
  fromFile,
  toFile
});

console.log('✅ [STAC Format] Registered custom STAC JSON format handler');
