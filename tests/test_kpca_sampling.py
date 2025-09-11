import pandas as pd
import numpy as np
from wireless_anom.reduce.kpca import KernelPCAReducer


def test_kpca_sampling_changes_gamma():
    X = pd.DataFrame(np.random.rand(50, 3), columns=["a","b","c"])
    cfg = {
        "n_components": 2,
        "kernel": "rbf",
        "gamma_sampling": {
            "strategy": "logspace",
            "start_exp": -3,
            "end_exp": 1,
            "num_samples": 4,
        },
    }
    reducer = KernelPCAReducer(cfg)
    reducer.fit_transform(X)
    assert reducer.gamma is not None
    assert reducer.gamma != 10 ** (-3)
