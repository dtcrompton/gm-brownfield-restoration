// Define Greater Manchester boundary manually using approximate coordinates
var greaterManchester = ee.Geometry.Rectangle([-2.7, 53.35, -1.95, 53.65]);

Map.centerObject(greaterManchester, 10);
Map.addLayer(greaterManchester, {color: 'blue'}, 'Greater Manchester bbox', false);
print('Study area:', greaterManchester);

// Load land cover data (ESA WorldCover 10m resolution)
var landcover = ee.ImageCollection('ESA/WorldCover/v200')
  .filterBounds(greaterManchester)
  .first()
  .clip(greaterManchester);

// Print land cover info
print('Land cover:', landcover);

// Display land cover with standard visualization
Map.addLayer(landcover, {}, 'Land Cover', false);

// Define classification values we care about:
// 50 = Built-up (urban/industrial)
// 60 = Bare/sparse vegetation (potential brownfield)
// 40 = Cropland
// 10 = Trees

// Create a mask for built-up areas
var builtUp = landcover.eq(50);
Map.addLayer(builtUp.selfMask(), {palette: ['red']}, 'Built-up areas', false);

// Create a mask for bare/sparse areas (potential brownfield indicators)
var bareSparse = landcover.eq(60);
Map.addLayer(bareSparse.selfMask(), {palette: ['brown']}, 'Bare/sparse vegetation', false);