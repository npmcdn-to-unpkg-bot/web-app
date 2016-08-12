MANAGE = python3 ./manage.py
COFFEE = ./node_modules/coffee-script/bin/coffee
STYLUS = ./node_modules/stylus/bin/stylus
UGLIFY = ./node_modules/uglify-js/bin/uglifyjs
NOW = $(shell date +"%Y%m%d-%H%M%S")

usage:
	@echo ''
	@echo 'Core tasks                       : Description'
	@echo '--------------------             : -----------'
	@echo 'make setup                       : Install all necessary dependencies'
	@echo 'make dev                         : Start the local development server'
	@echo 'make celery                      : Start the local celery process'
	@echo 'make migrate                     : Run the South migrations'
	@echo 'make assets                      : Recompile JS, CSS & image assets'
	@echo 'make css                         : Watch stylus assets'
	@echo 'make js                          : Watch coffee assets'
	@echo 'make clean                       : Clean up all compiled styles and javascript'
	@echo 'make test                        : Run tests'
	@echo ''

echo:
	echo $$USER

dbshell:
	$(MANAGE) dbshell
shell:
	$(MANAGE) shell

dev:
	$(MANAGE) runserver

runserver:
	$(MANAGE) runserver

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate shoutweb

css:
	stylus -w -o public/css shoutweb/frontend/stylus

js:
	$(COFFEE) -w -o public/js shoutweb/frontend/coffee



