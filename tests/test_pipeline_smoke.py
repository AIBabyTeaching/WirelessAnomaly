from wireless_anom.pipeline import load_config, run_pipeline


def test_pipeline_smoke(config_path):
    cfg = load_config(config_path)
    res = run_pipeline(cfg)
    assert "iso_scores" in res
    assert "classifiers" in res
