"""Decision boundary visualisation for 2D data."""
from __future__ import annotations
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_decision_boundary(model, X: pd.DataFrame, y: pd.Series, path: Path) -> None:
    """Plot decision boundary for a fitted classifier on 2-D data.

    Parameters
    ----------
    model: Fitted scikit-learn classifier supporting ``predict``.
    X: DataFrame with ``PC1`` and ``PC2`` columns.
    y: Scenario labels.
    path: Output path without extension; PNG and PDF are written.
    """

    plt.style.use("seaborn-v0_8")
    x_min, x_max = X["PC1"].min() - 0.5, X["PC1"].max() + 0.5
    y_min, y_max = X["PC2"].min() - 0.5, X["PC2"].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))
    grid = np.c_[xx.ravel(), yy.ravel()]
    preds = model.predict(grid)
    preds_idx, _ = pd.factorize(preds)
    preds_idx = preds_idx.reshape(xx.shape)

    fig, ax = plt.subplots()
    ax.contourf(xx, yy, preds_idx, alpha=0.2, levels=len(np.unique(preds_idx)))
    ax.scatter(X["PC1"], X["PC2"], c=pd.factorize(y)[0], edgecolor="k")
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    fig.tight_layout()
    fig.savefig(path.with_suffix(".png"), dpi=150)
    fig.savefig(path.with_suffix(".pdf"))
    plt.close(fig)
