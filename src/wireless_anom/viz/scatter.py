"""Scatter plot visualizations."""
from __future__ import annotations
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def plot_scatter(df: pd.DataFrame, path: Path) -> None:
    fig, ax = plt.subplots()
    labels = df['label'].unique()
    for label in labels:
        subset = df[df['label'] == label]
        ax.scatter(subset['PC1'], subset['PC2'], label=label, s=10)
    if 'anomaly' in df.columns:
        anomalies = df[df['anomaly']]
        ax.scatter(anomalies['PC1'], anomalies['PC2'], edgecolor='r', facecolor='none', s=30, label='anomaly')
    ax.legend()
    fig.savefig(path, dpi=150)
    plt.close(fig)
