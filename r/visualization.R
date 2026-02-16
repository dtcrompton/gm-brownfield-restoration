# Greater Manchester Brownfield Risk Analysis
# Visualization and statistical summary of GEE risk scores

# Load libraries ----
library(ggplot2)
library(dplyr)
library(tidyr)

# Set theme for plots
theme_set(theme_minimal(base_size = 14))

# Read in the data ----
brownfield <- read.csv("../data/raw/GM_brownfield_risk_scores.csv")

# Initial data exploration ----
str(brownfield)
summary(brownfield)
head(brownfield)

# Check for missing values in risk scores
sum(is.na(brownfield$total_risk))

# Clean data ----
# Remove the one site with missing hectares (can't analyze size properly)
brownfield_clean <- brownfield %>% 
  filter(!is.na(hectares))

# Create risk categories for easier interpretation
brownfield_clean <- brownfield_clean %>%
  mutate(
    risk_category = case_when(
      total_risk >= 0.8 ~ "High",
      total_risk >= 0.7 ~ "Medium",
      TRUE ~ "Low"
    ),
    risk_category = factor(risk_category, levels = c("Low", "Medium", "High"))
  )

# Summary statistics by risk category
risk_summary <- brownfield_clean %>%
  group_by(risk_category) %>%
  summarise(
    n_sites = n(),
    mean_hectares = mean(hectares),
    total_hectares = sum(hectares)
  )

print(risk_summary)