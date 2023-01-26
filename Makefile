SHELL=bash

export COMPOSE_FILE=docker-compose.yaml

build:
	@docker-compose build

up:
	@docker-compose up -d

down:
	@docker-compose down

test: up
	@docker-compose run --no-deps --rm app sh -c "python -m pytest -x /code/app/tests/"