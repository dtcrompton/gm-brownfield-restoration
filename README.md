# Greater Manchester Brownfield Restoration Potential

Geospatial analysis identifying former industrial sites with high ecological risk and suitability for nature-based remediation (mycoforestry/phytoremediation).

## Project Overview

This project uses satellite imagery and open environmental datasets to model contamination risk across Greater Manchester's industrial heritage sites. The analysis combines:
- Proximity to watercourses (contamination spread risk)
- Soil permeability (groundwater pollution potential)
- Terrain characteristics (slope, elevation)
- Current land cover (built-up and bare areas as brownfield indicators)

High-risk sites are prioritised for ecological assessment and nature-based restoration interventions.

## Tools & Data Sources

**Analysis:**
- Google Earth Engine (satellite data processing, spatial analysis)
- R (statistical analysis, visualisation)
- QGIS (cartographic output)
- Python (planned: interactive mapping, ML extension)

**Datasets:**
- ESA WorldCover (land cover, 10m resolution)
- WWF HydroSHEDS (river networks)
- OpenLandMap (soil texture/permeability)
- SRTM (elevation, terrain)

## Project Status

**Phase 1: GEE Foundation (Complete)**
- ✅ Study area definition (Greater Manchester)
- ✅ Environmental data layers integrated
- ✅ Composite contamination risk score generated

**Phase 2: Export & Analysis (In Progress)**
- Export risk raster and statistics
- R-based visualisation and site ranking
- Summary statistics by district

**Phase 3: Cartography (Planned)**
- QGIS final map production
- Site-specific case studies

**Phase 4: ML Extension (Planned)**
- Predictive model for restoration success
- Interactive Folium web map for stakeholders

## Repository Structure
```
gm-brownfield-restoration/
├── README.md
├── gee/
│   └── analysis.js          # GEE risk scoring model
├── data/
│   ├── raw/                 # GEE exports
│   └── processed/           # Cleaned datasets
├── r/
│   └── visualisation.R      # Statistical analysis (pending)
├── python/                  # ML extension (pending)
├── qgis/
│   └── final_map.qgz       # Cartographic output (pending)
└── outputs/
    ├── figures/
    └── maps/
```

## Next Steps

1. Export risk score raster and zonal statistics from GEE
2. Analyse results in R (district-level summaries, site rankings)
3. Create polished map outputs in QGIS
4. Build interactive web map (Python + Folium)
5. Develop ML model for restoration suitability prediction
