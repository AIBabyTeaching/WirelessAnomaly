"""Core pipeline orchestrating loading, reduction, detection, classification."""
from __future__ import annotations
import glob
from pathlib import Path
from typing import Dict, Any

import yaml
import pandas as pd
from rich.console import Console

from .io.loaders import load_reduced_csvs
from .detect.isolation_forest import run_isoforest
from .classify.models import run_classifiers
from .viz.scatter import plot_scatter
from .viz.distributions import plot_distributions
from .detect.metrics import compute_tev
from .utils.seeds import set_seeds
from .utils.paths import ensure_dir

console = Console()


def load_config(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def run_pipeline(config: Dict[str, Any]) -> Dict[str, Any]:
    """Run reduced pipeline and return results."""
    set_seeds(config.get("seed", 42))
    data_mode = config["data"]["mode"]
    input_path = config["paths"]["input"]
    if data_mode == "reduced":
        df = load_reduced_csvs(input_path, config["data"]["reduced_columns"], config["data"]["label_column"])
    else:
        raise NotImplementedError("end2end mode not yet implemented")

    results: Dict[str, Any] = {}
    if config["eval"].get("compute_tev", False):
        results["tev"] = compute_tev(df[config["data"]["reduced_columns"]])
        console.print(f"TEV: {results['tev']}")

    iso_cfg = config["detect"]["isoforest"]
    iso_scores, iso_flags = run_isoforest(df[config["data"]["reduced_columns"]], iso_cfg)
    results["iso_scores"] = iso_scores
    df["anomaly"] = iso_flags
    console.print(f"Anomaly rate: {iso_flags.mean():.2%}")

    if config["classify"].get("enabled", False):
        clf_results = run_classifiers(df[config["data"]["reduced_columns"]], df[config["data"]["label_column"]], config["classify"]["models"])
        results["classifiers"] = clf_results
        console.print(f"Classifier accuracy: {clf_results}")

    if config["viz"].get("enabled", False):
        fig_dir = Path(config["paths"]["figures"])
        ensure_dir(fig_dir)
        if config["viz"].get("scatter", False):
            plot_scatter(df, fig_dir / "scatter.png")
        if config["viz"].get("distributions", False):
            plot_distributions(df, fig_dir / "dist.png")

    return results
