"""Reducer base interface."""
from __future__ import annotations
from typing import Protocol
import pandas as pd


class Reducer(Protocol):
    def fit_transform(self, X: pd.DataFrame) -> pd.DataFrame:
        ...
