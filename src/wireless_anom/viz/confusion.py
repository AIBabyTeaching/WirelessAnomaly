"""Confusion matrix heatmap plots."""
from __future__ import annotations
from pathlib import Path
from typing import Sequence

import matplotlib.pyplot as plt
import numpy as np


def plot_confusion_matrix(cm: np.ndarray, labels: Sequence[str], path: Path) -> None:
    """Plot a confusion matrix heatmap.

    Parameters
    ----------
    cm: Confusion matrix as returned by ``sklearn.metrics.confusion_matrix``.
    labels: Class label names in the order used by ``cm``.
    path: Output path without extension; PNG and PDF are written.
    """

    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    im = ax.imshow(cm, cmap="Blues")
    ax.set_xticks(range(len(labels)), labels)
    ax.set_yticks(range(len(labels)), labels)
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, cm[i, j], ha="center", va="center")
    fig.colorbar(im, ax=ax)
    fig.tight_layout()
    fig.savefig(path.with_suffix(".png"), dpi=150)
    fig.savefig(path.with_suffix(".pdf"))
    plt.close(fig)
