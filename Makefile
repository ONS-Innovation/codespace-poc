.DEFAULT_GOAL := all

.PHONY: all
all: ## Show the available make targets.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep

.PHONY: lint
lint: ## Run linters.
	@echo "Running black..."
	black .
	@echo "Running flake8..."
	flake8 .
	@echo "Running isort..."
	poetry run isort .
	@echo "Running mypy..."
	poetry run mypy .
