"""Evaluation and interpretability metrics."""
from __future__ import annotations
from typing import Dict
import numpy as np
import pandas as pd
from sklearn.metrics import silhouette_score, davies_bouldin_score


def compute_tev(X: pd.DataFrame) -> Dict[str, float]:
    """Compute total explained variance ratios for components."""
    var = X.var(axis=0, ddof=0)
    total = var.sum()
    return {col: (v / total) for col, v in var.items()}



def clustering_indices(X: pd.DataFrame, labels: pd.Series) -> Dict[str, float]:
    """Return basic clustering validation metrics."""
    return {
        "silhouette": float(silhouette_score(X, labels)),
        "davies_bouldin": float(davies_bouldin_score(X, labels)),
    }


def top_anomalies(df: pd.DataFrame, scores: np.ndarray, n: int = 5) -> pd.DataFrame:
    """List the top ``n`` most anomalous samples based on scores."""
    df = df.copy()
    df["score"] = scores
    return df.sort_values("score", ascending=False).head(n)