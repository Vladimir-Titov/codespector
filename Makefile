lint:
	@ruff check . --fix
	@ruff format --check .

format:
	@ruff format .

fix:
	@ruff check . --fix
	@ruff format .
