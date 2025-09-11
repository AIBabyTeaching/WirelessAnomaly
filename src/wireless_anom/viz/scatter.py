"""Scatter plot visualizations.

This plot shows the relationship between the first two KPCA components. Normal
scenarios are colored distinctly, while anomalies identified by the detection
algorithm are marked with red ``x`` markers. This helps researchers visually
inspect separability and detector behaviour.
"""
from __future__ import annotations
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def plot_scatter(df: pd.DataFrame, path: Path) -> None:
    """Plot PC1/PC2 scatter with anomaly overlays.

    Parameters
    ----------
    df:
        Data containing ``PC1``, ``PC2`` and ``label`` columns and optionally
        an ``anomaly`` boolean column.
    path:
        Output path without extension; both PNG and PDF are written.
    """

    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    labels = df["label"].unique()
    for idx, label in enumerate(labels):
        subset = df[df["label"] == label]
        ax.scatter(
            subset["PC1"],
            subset["PC2"],
            s=20,
            alpha=0.7,
            label=label,
        )
    if "anomaly" in df.columns:
        anomalies = df[df["anomaly"]]
        ax.scatter(
            anomalies["PC1"],
            anomalies["PC2"],
            marker="x",
            c="red",
            label="anomaly",
        )
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    fig.tight_layout()
    fig.savefig(path.with_suffix(".png"), dpi=150)
    fig.savefig(path.with_suffix(".pdf"))
    plt.close(fig)
