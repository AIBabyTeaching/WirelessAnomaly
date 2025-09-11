# Pipeline

1. **Load** reduced or raw features via flexible loaders.
2. **Feature selection** using Elastic Net when raw features are available.
3. **Reduce** dimensionality with pluggable reducers (PCA, KPCA, UMAP stub).
4. **Detect** anomalies globally with Isolation Forest and optionally validate
   locally with DBSCAN.
5. **Classify** scenarios with a suite of supervised models.
6. **Evaluate** using total explained variance and clustering indices.
7. **Visualise** distributions, anomaly scatter plots, TEV contributions and
   confusion matrices.
