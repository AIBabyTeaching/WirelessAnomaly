"""Simple classifier wrappers used for scenario classification.

Each classifier is trained on the reduced 2-D feature space. Accuracy and
confusion matrices are returned to aid interpretation of classifier behaviour.
"""
from __future__ import annotations
from typing import Sequence, Dict, Any
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix


def run_classifiers(X: pd.DataFrame, y: pd.Series, models: Sequence[str]) -> Dict[str, Any]:
    """Fit classifiers and return accuracy and confusion matrices."""

    results: Dict[str, Any] = {}
    for name in models:
        if name == "knn":
            clf = KNeighborsClassifier()
        elif name == "svm":
            clf = SVC()
        elif name == "rf":
            clf = RandomForestClassifier(random_state=42)
        elif name == "lr":
            clf = LogisticRegression(max_iter=1000)
        elif name == "dt":
            clf = DecisionTreeClassifier(random_state=42)
        elif name == "nb":
            clf = GaussianNB()
        else:
            continue
        clf.fit(X, y)
        preds = clf.predict(X)
        acc = float(accuracy_score(y, preds))
        cm = confusion_matrix(y, preds)
        results[name] = {"accuracy": acc, "confusion": cm, "model": clf}
    return results
