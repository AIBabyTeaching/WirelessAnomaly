"""Simple classifier wrappers."""
from __future__ import annotations
from typing import Sequence, Dict
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def run_classifiers(X: pd.DataFrame, y: pd.Series, models: Sequence[str]) -> Dict[str, float]:
    results = {}
    for name in models:
        if name == "knn":
            clf = KNeighborsClassifier()
        elif name == "svm":
            clf = SVC()
        elif name == "rf":
            clf = RandomForestClassifier(random_state=42)
        else:
            continue
        clf.fit(X, y)
        preds = clf.predict(X)
        results[name] = float(accuracy_score(y, preds))
    return results
