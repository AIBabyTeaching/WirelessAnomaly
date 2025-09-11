"""Feature selection utilities."""
from __future__ import annotations
from pathlib import Path
import pandas as pd
from sklearn.linear_model import ElasticNet


def elastic_net_select(X: pd.DataFrame, y: pd.Series, out: Path | None = None) -> pd.DataFrame:
    """Run a simple Elastic Net and optionally export coefficients.

    Parameters
    ----------
    X, y: Input features and labels.
    out: Optional path to write coefficients for interpretability.
    """

    model = ElasticNet(alpha=0.001, l1_ratio=0.5, random_state=42)
    model.fit(X, y)
    if out:
        coeffs = pd.Series(model.coef_, index=X.columns)
        coeffs.to_csv(out)
    return X
