"""Data loading utilities."""
from __future__ import annotations
from pathlib import Path
from typing import Sequence
import glob
import pandas as pd


def load_reduced_csvs(pattern: str, columns: Sequence[str], label_col: str) -> pd.DataFrame:
    """Load reduced CSV files with columns and label."""
    files = glob.glob(pattern)
    if not files:
        raise FileNotFoundError(f"No files matched pattern {pattern}")
    dfs = [pd.read_csv(f, names=columns + [label_col], header=0) for f in files]
    return pd.concat(dfs, ignore_index=True)
