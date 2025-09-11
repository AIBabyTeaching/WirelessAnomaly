"""Isolation Forest detector.

Isolation Forest isolates anomalies by randomly partitioning the feature space
and measuring how quickly points become isolated. Shorter average path lengths
indicate anomalies. This wrapper returns the anomaly scores and flags.
"""
from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest


def run_isoforest(X: pd.DataFrame, cfg: dict):
    """Run Isolation Forest and return scores and anomaly flags."""
    clf = IsolationForest(
        contamination=cfg.get("contamination", 0.05),
        n_estimators=cfg.get("n_estimators", 100),
        random_state=42,
    )
    scores = clf.fit_predict(X)
    anomalies = scores == -1
    return clf.decision_function(X), anomalies
