"""CLI entrypoints using Typer."""
from __future__ import annotations
import typer
from ..pipeline import run_pipeline, load_config

app = typer.Typer(help="Wireless anomaly detection")
run_app = typer.Typer(help="Run pipelines")
app.add_typer(run_app, name="run")

ev_app = typer.Typer(help="Evaluation")
app.add_typer(ev_app, name="eval")

viz_app = typer.Typer(help="Visualization")
app.add_typer(viz_app, name="viz")


@run_app.command("reduced")
def run_reduced(config: str = typer.Option(..., "--config", "-c")):
    cfg = load_config(config)
    cfg['data']['mode'] = 'reduced'
    run_pipeline(cfg)


@ev_app.command("metrics")
def eval_metrics(config: str = typer.Option(..., "--config", "-c")):
    cfg = load_config(config)
    cfg['eval']['compute_tev'] = True
    run_pipeline(cfg)


@viz_app.command("figures")
def viz_figures(config: str = typer.Option(..., "--config", "-c")):
    cfg = load_config(config)
    cfg['viz']['enabled'] = True
    run_pipeline(cfg)


if __name__ == "__main__":
    app()
