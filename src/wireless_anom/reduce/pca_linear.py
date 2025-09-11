"""Linear PCA reducer."""
from __future__ import annotations
import pandas as pd
from sklearn.decomposition import PCA


class LinearPCA:
    """Wraps scikit-learn's PCA for consistency with other reducers."""

    def __init__(self, n_components: int = 2):
        self.model = PCA(n_components=n_components)

    def fit_transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """Return the first ``n_components`` principal components."""

        comps = self.model.fit_transform(X)
        cols = [f"PC{i+1}" for i in range(comps.shape[1])]
        return pd.DataFrame(comps, columns=cols, index=X.index)
