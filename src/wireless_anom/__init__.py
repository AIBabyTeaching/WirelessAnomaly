"""Wireless anomaly detection package."""
__all__ = ["run_pipeline", "load_config"]
from .cli.main import app as cli_app  # CLI entry
from .pipeline import run_pipeline, load_config
