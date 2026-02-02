.PHONY: test lint format typecheck check

test:
	pytest -q

lint:
	ruff check .

format:
	ruff format .

typecheck:
	mypy src

check: format lint typecheck test
