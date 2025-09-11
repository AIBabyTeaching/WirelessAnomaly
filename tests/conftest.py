from pathlib import Path
import pytest


@pytest.fixture
def config_path() -> str:
    return "src/wireless_anom/config/defaults.yaml"
