"""
Greater Manchester Brownfield Interactive Map
Creates an interactive web map with clickable brownfield sites
Enhanced with layer groups, marker clustering, and recentre button
"""

import geopandas as gpd
import folium
from folium import plugins

# Load the GeoPackage with risk scores
brownfield = gpd.read_file("../outputs/maps/gm_brownfield_clipped.gpkg")

print(f"Loaded {len(brownfield)} brownfield sites")

# Calculate map center
center_lat = brownfield.geometry.centroid.y.mean()
center_lon = brownfield.geometry.centroid.x.mean()

# Create base map
m = folium.Map(
    location=[center_lat, center_lon],
    zoom_start=11,
    tiles='CartoDB positron'
    # control_scale=True  # Adds a scale bar (commented out - see custom scale below)
)

# Add custom scale bar with better positioning and size
scale = folium.plugins.MeasureControl(
    position='bottomleft',
    primary_length_unit='kilometers',
    secondary_length_unit='miles',
    primary_area_unit='sqkilometers',
    secondary_area_unit='sqmiles'
)
scale.add_to(m)

# Define colors for risk categories
color_map = {
    'Low': '#27AE60',
    'Medium': '#F39C12',
    'High': '#E74C3C'
}

# Create separate feature groups for each risk category
feature_groups = {}
for category in ['High', 'Medium', 'Low']:
    fg = plugins.MarkerCluster(name=f'{category} Risk Sites')
    feature_groups[category] = fg

# Add each brownfield site to its appropriate feature group
for idx, row in brownfield.iterrows():
    lat = row.geometry.y
    lon = row.geometry.x
    
    # Create popup content
    popup_html = f"""
    <div style="font-family: Arial; width: 250px;">
        <h4 style="margin-bottom: 10px;">{row['site.addre.y']}</h4>
        <table style="width: 100%;">
            <tr><td><b>Reference:</b></td><td>{row['reference']}</td></tr>
            <tr><td><b>Size:</b></td><td>{row['hectares.y']:.2f} hectares</td></tr>
            <tr><td><b>Risk Category:</b></td><td><span style="color: {color_map[row['risk_category']]}; font-weight: bold;">{row['risk_category']}</span></td></tr>
            <tr><td><b>Total Risk Score:</b></td><td>{row['total_risk']:.3f}</td></tr>
            <tr><td><b>Water Risk:</b></td><td>{row['water_risk']:.3f}</td></tr>
            <tr><td><b>Soil Risk:</b></td><td>{row['soil_risk']:.3f}</td></tr>
            <tr><td><b>Slope Risk:</b></td><td>{row['slope_risk']:.3f}</td></tr>
        </table>
    </div>
    """
    
    # Create marker and add to appropriate feature group
    folium.CircleMarker(
        location=[lat, lon],
        radius=6,
        popup=folium.Popup(popup_html, max_width=300),
        color=color_map[row['risk_category']],
        fillColor=color_map[row['risk_category']],
        fillOpacity=0.7,
        weight=2
    ).add_to(feature_groups[row['risk_category']])

# Add all feature groups to the map
for fg in feature_groups.values():
    fg.add_to(m)

# Add layer control
folium.LayerControl(collapsed=False).add_to(m)

# Add a recentre button using custom JavaScript
# Store the initial center and zoom in the map's HTML
recentre_script = f"""
<div id="recentre-btn" style="
    position: fixed;
    top: 80px;
    left: 10px;
    z-index: 1000;
    background-color: white;
    border: 2px solid rgba(0,0,0,0.2);
    border-radius: 4px;
    padding: 8px 12px;
    cursor: pointer;
    font-family: Arial, sans-serif;
    font-size: 14px;
    box-shadow: 0 1px 5px rgba(0,0,0,0.2);
">
    Recentre Map
</div>

<script>
// Wait for the map to be fully loaded
setTimeout(function() {{
    var recentreBtn = document.getElementById('recentre-btn');
    if (recentreBtn) {{
        recentreBtn.onclick = function() {{
            // Get reference to the Leaflet map (Folium creates a global variable)
            var mapObj = window[Object.keys(window).filter(key => key.startsWith('map_'))[0]];
            if (mapObj) {{
                mapObj.setView([{center_lat}, {center_lon}], 11);
            }}
        }};
    }}
}}, 1000);
</script>
"""

m.get_root().html.add_child(folium.Element(recentre_script))

# Save the map
output_path = "../outputs/maps/gm_brownfield_interactive.html"
m.save(output_path)

print(f"\nInteractive map saved to: {output_path}")
print(f"Features added:")
print(f"  - Layer groups for High/Medium/Low risk sites")
print(f"  - Marker clustering for cleaner view at zoomed-out levels")
print(f"  - Layer control to toggle categories on/off")
print(f"  - Recentre button to reset map view")
print(f"  - Scale bar")