# Greater Manchester Brownfield Restoration Potential

Geospatial analysis identifying brownfield sites with high environmental risk and restoration potential using satellite data, open datasets, and machine learning.

## Project Overview

This project combines remote sensing, GIS, and predictive modelling to assess contamination risk across Greater Manchester's brownfield sites and identify priority candidates for nature-based remediation interventions like mycoforestry and phytoremediation.

The risk assessment model integrates three satellite-derived environmental factors:

- **Proximity to watercourses** — contamination spread potential to rivers and streams
- **Soil permeability** — groundwater pollution risk based on soil texture
- **Terrain characteristics** — slope and elevation as proxies for historical industrial land use

High-risk sites are flagged for ecological assessment, with outputs designed for non-technical stakeholders including interactive maps and stakeholder reports.


## Repository Structure
```
gm-brownfield-restoration/
├── README.md
├── gee/
│   └── analysis.js          # GEE risk scoring model
├── data/
│   ├── raw/                 # GEE exports and source data
│   └── processed/           # Cleaned datasets
├── r/
│   └── visualisation.R      # Statistical analysis and visualisations
├── python/
│   └── interactive_map.py   # Folium web map
├── qgis/
│   └── gm_brownfield_map.qgz  # Cartographic project
└── outputs/
├── figures/             # Charts and plots
└── maps/                # Map exports (PNG, HTML)
```


## Tools & Data Sources

**Analysis Platform:**
- **Google Earth Engine** — satellite data processing, spatial analysis
- **R** — statistical analysis, data visualisation (ggplot2, dplyr, sf)
- **QGIS** — professional cartography and map layout
- **Python** — interactive mapping (Folium, GeoPandas), ML modelling (scikit-learn)

**Datasets:**
- **UK Brownfield Land Register** — 1,585 active sites in Greater Manchester
- **ESA WorldCover** — land cover classification (10m resolution)
- **WWF HydroSHEDS** — river networks and watercourse proximity
- **OpenLandMap** — soil texture and permeability (USDA classification)
- **SRTM DEM** — elevation and terrain analysis (30m resolution)


## Key Findings

### Site Distribution and Risk Assessment

- **1,585 active brownfield sites** analysed across Greater Manchester
- **746 sites (47%)** scored as **high environmental risk** (total risk ≥ 0.8)
- **764 sites (48%)** scored as **medium risk** (0.7–0.8)
- **75 sites (5%)** scored as **low risk** (< 0.7)

### Risk Factor Breakdown

| Risk Factor | Mean Score | Median Score | Range |
|-------------|-----------|--------------|-------|
| Water Proximity | 0.853 | 0.884 | 0.396–0.998 |
| Soil Permeability | 0.611 | 0.583 | 0.500–0.750 |
| Slope (flatness) | 0.908 | 0.924 | 0.534–0.999 |
| **Total Risk** | **0.791** | **0.797** | **0.615–0.899** |

**Interpretation:**
- **Water proximity** is the dominant risk driver (mean 0.85) — most sites are within 1–2km of watercourses
- **Terrain** is consistently flat (mean slope risk 0.91), reflecting urban/industrial land use patterns
- **Soil** shows moderate variation, with most sites on clay/loam soils (lower permeability)

### Geographic Concentration

- **Salford (M5 postcode area)** — highest concentration of top-risk sites
  - 3 of top 10 highest-risk sites located here
  - Proximity to River Irwell, flat terrain, historical industrial land use
- **772 hectares** of high-risk brownfield land identified across Greater Manchester
- Mean site size: 1.12 hectares (range: 0.01–109 hectares)

### Top 10 Highest Risk Sites

| Rank | Site Address | Total Risk | Hectares |
|------|-------------|-----------|----------|
| 1 | Land at Worrall Street, Salford M5 4TH | 0.898 | 0.32 |
| 2 | Former Hardy's Well pub, Wilmslow Road | 0.898 | 0.17 |
| 3 | 221-223 Ordsall Lane, Salford M5 4TD | 0.895 | 0.50 |
| 4 | Former Ambulance Station, Pottery Road | 0.894 | 0.38 |
| 5 | Site Between Trinity Way And Audacious Church... | 0.892 | 0.27 |

*Full table available in `outputs/figures/top10_highest_risk_sites.csv`*


## Project Status

**Phase 1: GEE Foundation COMPLETE**
- Study area definition (Greater Manchester bounding box: -2.7 to -1.95°E, 53.35 to 53.65°N)
- UK brownfield register imported and filtered (1,585 active sites)
- Environmental data layers integrated (land cover, watercourses, soil, terrain)
- Composite risk score calculated for all sites
- Data exported to CSV and GeoPackage formats

**Phase 2: R Analysis COMPLETE**
- Statistical summary and risk categorisation
- Distribution analysis and site rankings
- Four publication-quality visualisations:
  - Risk score histogram
  - Risk category bar chart
  - Site size vs. risk scatter plot
  - Top 10 highest-risk sites chart

**Phase 3: QGIS Cartography COMPLETE**
- Professional map layout with legend, scale bar, north arrow
- Risk-categorised sites (green/orange/red colour scheme)
- High-resolution export (300 DPI) for portfolio and presentations

**Phase 4: Python Extension COMPLETE**
- Web-based interactive map (Folium + GeoPandas)
- Clickable markers with detailed site information
- Layer control to toggle risk categories
- Marker clustering and distance measurement tool
- Standalone HTML file (no server required)

**Phase 5: ML Extension (Planned)**
- Predictive model for ecological restoration success
- Feature engineering from environmental and site characteristics
- Model validation and performance metrics
- 1-page stakeholder explainer document


## Outputs

**Interactive Map:** `outputs/maps/gm_brownfield_interactive.html` — open in any web browser

**Static Map:** `outputs/maps/GM Brownfield Risk Map.png` — 300 DPI print-quality export

**Visualisations:**
- `outputs/figures/risk_distribution.png`
- `outputs/figures/risk_category_chart.png`
- `outputs/figures/size_risk_scatter.png`
- `outputs/figures/top10_risk_sites.png`

**Data Exports:**
- `outputs/figures/top10_highest_risk_sites.csv`
- `outputs/maps/gm_brownfield_clipped.gpkg` — filtered sites with risk scores


## Future Work

This project demonstrates a reproducible geospatial workflow applicable to other regions and contamination assessment contexts. Potential extensions include:

- Additional UK metropolitan areas with industrial heritage
- Integration of historical contamination records where available
- Habitat suitability modelling for specific bioremediation implementations

The methodology and codebase are designed to be adaptable for similar brownfield restoration analyses.


## Author

**Daniel Crompton**  
MSc Computer Science & AI | MSc Quantity Surveying & Commercial Management  
[LinkedIn](https://www.linkedin.com/in/dtcrompton/) | [GitHub](https://github.com/dtcrompton)

---

## Licence

MIT Licence — see `LICENCE` file for details