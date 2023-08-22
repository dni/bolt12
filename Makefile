all: black ruff mypy pyright test

format: black ruff

black:
	poetry run black --preview .

ruff:
	poetry run ruff check . --fix

mypy:
	poetry run mypy .

pyright:
	poetry run pyright

test:
	poetry run pytest tests
