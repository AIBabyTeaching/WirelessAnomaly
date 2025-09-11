"""Seed utilities."""
from __future__ import annotations
import random
import numpy as np


def set_seeds(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
