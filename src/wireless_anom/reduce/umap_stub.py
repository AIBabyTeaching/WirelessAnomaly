"""UMAP reducer placeholder."""
from __future__ import annotations
import pandas as pd


class UMAPReducer:
    """Placeholder for UMAP; requires optional dependency."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("UMAP reducer not implemented. Install umap-learn and implement.")

    def fit_transform(self, X: pd.DataFrame) -> pd.DataFrame:  # pragma: no cover
        raise NotImplementedError
