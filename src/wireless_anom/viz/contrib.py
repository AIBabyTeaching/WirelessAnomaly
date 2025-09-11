"""Total explained variance contribution plots.

The function in this module visualises how much each component contributes to
explained variance. A bar plot shows individual contributions while a cumulative
line helps assess how many components are required to reach a desired level.
"""
from __future__ import annotations
from pathlib import Path
from typing import Dict

import matplotlib.pyplot as plt


def plot_tev(tev: Dict[str, float], path: Path) -> None:
    """Plot total explained variance contributions.

    Parameters
    ----------
    tev: Mapping of component name to explained variance ratio.
    path: Output path without extension; PNG and PDF are written.
    """

    plt.style.use("seaborn-v0_8")
    labels = list(tev.keys())
    values = [tev[k] for k in labels]
    cumulative = [sum(values[: i + 1]) for i in range(len(values))]

    fig, ax1 = plt.subplots()
    ax1.bar(labels, values, color="steelblue", alpha=0.7)
    ax1.set_ylabel("TEV")
    ax2 = ax1.twinx()
    ax2.plot(labels, cumulative, color="darkorange", marker="o")
    ax2.set_ylabel("Cumulative")
    ax1.set_xlabel("Component")
    fig.tight_layout()
    fig.savefig(path.with_suffix(".png"), dpi=150)
    fig.savefig(path.with_suffix(".pdf"))
    plt.close(fig)
