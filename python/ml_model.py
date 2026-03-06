"""
Greater Manchester Brownfield Restoration Suitability Model
Predicts which sites are most suitable for ecological restoration interventions
"""

import pandas as pd
import geopandas as gpd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the brownfield data with risk scores
brownfield = gpd.read_file("../outputs/maps/gm_brownfield_clipped.gpkg")

print(f"Loaded {len(brownfield)} brownfield sites")
print(f"Columns: {list(brownfield.columns)}\n")

# Feature engineering - create additional predictive features
brownfield['site_size_category'] = pd.cut(
    brownfield['hectares.y'], 
    bins=[0, 0.5, 2, 10, 200], 
    labels=['Small', 'Medium', 'Large', 'Very Large']
)

# Check the data
print("Feature engineering preview:")
print(brownfield[['hectares.y', 'site_size_category', 'total_risk', 'risk_category']].head(10))

# Create a synthetic "restoration suitability" target variable
# In reality, this would come from historical restoration outcome data
# For this model, we define suitability based on:
# 1. Medium or High risk (worth remediating)
# 2. Site size between 0.1 and 10 hectares (manageable scale)
# 3. Relatively flat terrain (slope_risk > 0.8)

brownfield['suitable_for_restoration'] = (
    (brownfield['risk_category'].isin(['Medium', 'High'])) &
    (brownfield['hectares.y'] >= 0.1) &
    (brownfield['hectares.y'] <= 10) &
    (brownfield['slope_risk'] > 0.8)
).astype(int)

# Check the distribution
print("\nRestoration Suitability Distribution:")
print(brownfield['suitable_for_restoration'].value_counts())
print(f"\nPercentage suitable: {brownfield['suitable_for_restoration'].mean()*100:.1f}%")

# Preview some suitable vs unsuitable sites
print("\nSuitable sites (sample):")
print(brownfield[brownfield['suitable_for_restoration'] == 1][
    ['site.addre.y', 'hectares.y', 'total_risk', 'slope_risk']
].head(3))

print("\nUnsuitable sites (sample):")
print(brownfield[brownfield['suitable_for_restoration'] == 0][
    ['site.addre.y', 'hectares.y', 'total_risk', 'slope_risk']
].head(3))

# ===== PREPARE FEATURES FOR MACHINE LEARNING =====

# Select relevant features
feature_columns = ['water_risk', 'soil_risk', 'slope_risk', 'hectares.y', 'total_risk']
X = brownfield[feature_columns].copy()
y = brownfield['suitable_for_restoration']

# Check for missing values
print(f"\nMissing values in features:\n{X.isnull().sum()}")

# Drop rows with missing values (if any)
mask = X.notnull().all(axis=1) & y.notnull()
X = X[mask]
y = y[mask]

print(f"\nFinal dataset size: {len(X)} sites")
print(f"Features: {feature_columns}")

# Split into training and testing sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTraining set: {len(X_train)} sites")
print(f"Testing set: {len(X_test)} sites")
print(f"Class distribution in training: {y_train.value_counts().to_dict()}")

# Train Random Forest classifier
print("\n===== TRAINING RANDOM FOREST MODEL =====")
rf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train, y_train)
print("Model training complete!")

# Make predictions on test set
y_pred = rf_model.predict(X_test)
y_pred_proba = rf_model.predict_proba(X_test)[:, 1]

# Evaluate model performance
print("\n===== MODEL PERFORMANCE =====")
print(f"Accuracy: {rf_model.score(X_test, y_test):.3f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Unsuitable', 'Suitable']))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Feature importance
print("\n===== FEATURE IMPORTANCE =====")
feature_importance = pd.DataFrame({
    'feature': feature_columns,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

print(feature_importance)