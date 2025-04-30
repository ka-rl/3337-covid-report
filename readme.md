# COVID-19 Income Group Visualization

This project provides an analysis of COVID-19 outcomes across different socioeconomic groups.

---

## Group Members

- **Karl Ly** (UH ID: 2019049)
- **Gabriel Mena** (UH ID: 2031820)
- **Anthony Casarta** (UH ID: 2041116)

---

## Prerequisites

Ensure you have the following Python packages installed:

```bash
numpy pandas matplotlib scikit-learn seaborn scipy
```

---

## Notebooks

1. **visualizations.ipynb**

   - Visualizes COVID-19 fatality and infection rates across income groups
   - Groups countries into income groups by gdp_per_capita
   - Barplot, scatterplot, boxplot, and PCA

2. **clustering.ipynb**

   - K-means clustering to characterize and group global countries by socioeconomic status
   - Dendrogram to reveal nested groupings and visualize splits

3. **task-3-classifications.ipynb**

   - Generates response variable `pandemic_response_score` based on derived feature `case_fatality_rate`
   - Decision Tree, KNN, and SVM models were run using relevant socioeconomic features to predict `pandemic_response_score` classification
   - Tuning for all models included

4. **datapreprocessing-eda.ipynb**

   - Removes columns with greater than 50% missing data
   - Histogram for `total_cases` vs `total_deaths` and `log_total_cases` vs `log_total_deaths`
   - Scatterplots for `gdp_per_capitia` vs `log_total_cases` and `human_development_index` and `case_fatality_rate`
   - Boxplot for `total_cases` by `continent`

---
