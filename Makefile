.RECIPEPREFIX := >
.PHONY: setup test reproduce docs format docker-build docker-run

setup:
>python -m pip install -e .[dev]
>pre-commit install

test:
>pre-commit run --files $(shell git ls-files '*.py') || true
>pytest -q

reproduce:
>./scripts/reproduce_figures.sh
>./scripts/reproduce_tables.sh

docs:
>mkdocs build -f docs/mkdocs.yml

format:
>pre-commit run --files $(shell git ls-files '*.py')

docker-build:
>docker build -t wireless-anom ./docker

docker-run:
>docker run --rm wireless-anom
