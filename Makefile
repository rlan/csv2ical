# Makefile for easy development workflows.
# See development.md for docs.
# Note GitHub Actions call uv directly, not this Makefile.

.DEFAULT_GOAL := default

.PHONY: default install lint test upgrade build clean

default: install lint test

install:
	uv sync --all-extras --dev

lint:
	-uv run codespell ./src
	-uv run ruff check ./src
	-uv run ruff format ./src
	-uv run basedpyright ./src

test:
	-uv run csv2ical sample.csv test.ics
	-diff sample.ics test.ics

upgrade:
	uv sync --upgrade

build:
	uv build

clean:
	-rm -rf dist/
	-rm -rf *.egg-info/
	-rm -rf .pytest_cache/
	-rm -rf .mypy_cache/
	-rm -rf .venv/
	-find . -type d -name "__pycache__" -exec rm -rf {} +