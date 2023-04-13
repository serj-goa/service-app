build:
		docker-compose build

run-rm:
		docker-compose run --rm web-app sh -c "django-admin startproject config ."

up-d:
		docker-compose up -d