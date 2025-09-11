"""Evaluation metrics."""
from __future__ import annotations
import pandas as pd


def compute_tev(X: pd.DataFrame) -> dict:
    """Compute total explained variance ratios for components."""
    var = X.var(axis=0, ddof=0)
    total = var.sum()
    return {col: (v / total) for col, v in var.items()}
