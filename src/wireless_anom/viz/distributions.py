"""Distribution plots."""
from __future__ import annotations
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def plot_distributions(df: pd.DataFrame, path: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(6, 3))
    df['PC1'].hist(ax=axes[0])
    axes[0].set_title('PC1')
    df['PC2'].hist(ax=axes[1])
    axes[1].set_title('PC2')
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
