"""Isolation Forest detector."""
from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest


def run_isoforest(X: pd.DataFrame, cfg: dict):
    clf = IsolationForest(
        contamination=cfg.get("contamination", 0.05),
        n_estimators=cfg.get("n_estimators", 100),
        random_state=42,
    )
    scores = clf.fit_predict(X)
    anomalies = scores == -1
    return clf.decision_function(X), anomalies
