"""Kernel PCA with gamma sampling."""
from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.decomposition import KernelPCA


def sample_gammas(cfg: dict) -> np.ndarray:
    gs = cfg["gamma_sampling"]
    if gs["strategy"] == "logspace":
        return np.logspace(gs["start_exp"], gs["end_exp"], gs["num_samples"])
    else:
        start = 10 ** gs["start_exp"]
        end = 10 ** gs["end_exp"]
        return np.linspace(start, end, gs["num_samples"])


class KernelPCAReducer:
    def __init__(self, cfg: dict):
        self.cfg = cfg
        self.gamma = None

    def _select_gamma(self, X: pd.DataFrame) -> float:
        gammas = sample_gammas(self.cfg)
        best_gamma = gammas[0]
        best_score = -np.inf
        for g in gammas:
            kpca = KernelPCA(
                n_components=self.cfg["n_components"],
                kernel=self.cfg.get("kernel", "rbf"),
                gamma=g,
                random_state=42,
            )
            kpca.fit(X)
            score = kpca.eigenvalues_.sum()
            if score > best_score:
                best_score = score
                best_gamma = g
        return float(best_gamma)

    def fit_transform(self, X: pd.DataFrame) -> pd.DataFrame:
        self.gamma = self._select_gamma(X)
        kpca = KernelPCA(n_components=self.cfg["n_components"], kernel=self.cfg.get("kernel", "rbf"), gamma=self.gamma, random_state=42)
        comps = kpca.fit_transform(X)
        cols = [f"PC{i+1}" for i in range(comps.shape[1])]
        return pd.DataFrame(comps, columns=cols, index=X.index)
