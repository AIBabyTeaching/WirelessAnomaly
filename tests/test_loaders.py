from wireless_anom.io.loaders import load_reduced_csvs


def test_load_reduced_csv():
    df = load_reduced_csvs("v4_data/25_results/*.csv", ["PC1","PC2"], "label")
    assert not df.empty
    assert set(df.columns) == {"PC1","PC2","label"}
