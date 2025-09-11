"""Distribution plots for principal components.

Each subplot shows a histogram and kernel density estimate (KDE) for a principal
component, allowing quick comparison of how scenarios distribute along each
axis. Shared scales make the plots comparable across components.
"""
from __future__ import annotations
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_distributions(df: pd.DataFrame, path: Path) -> None:
    """Plot histograms with KDE overlays for PC1 and PC2.

    Parameters
    ----------
    df: DataFrame with ``PC1`` and ``PC2`` columns.
    path: Output path without extension; PNG and PDF are written.
    """

    plt.style.use("seaborn-v0_8")
    fig, axes = plt.subplots(1, 2, figsize=(8, 4), sharey=True)
    for ax, col in zip(axes, ["PC1", "PC2"]):
        sns.histplot(df[col], ax=ax, kde=True, color="steelblue")
        ax.set_title(col)
    fig.tight_layout()
    fig.savefig(path.with_suffix(".png"), dpi=150)
    fig.savefig(path.with_suffix(".pdf"))
    plt.close(fig)
