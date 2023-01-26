SHELL=bash

export COMPOSE_FILE=docker-compose.yaml

build:
	@docker-compose build

up:
	@docker-compose up -d