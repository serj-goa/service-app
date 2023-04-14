build:
		docker-compose build

up-d:
		docker-compose up -d

logs:
		docker-compose logs -f

run-rm-startproject:
		docker-compose run --rm web-app sh -c "django-admin startproject config ."

run-rm-makemigrations:
		docker-compose run --rm web-app sh -c "./manage.py makemigrations"

run-rm-migrate:
		docker-compose run --rm web-app sh -c "./manage.py migrate"

run-rm-createsuperuser:
		docker-compose run --rm web-app sh -c "./manage.py createsuperuser"

run-rm-startapp-clients:
		docker-compose run --rm web-app sh -c "./manage.py startapp clients"

run-rm-startapp-services:
		docker-compose run --rm web-app sh -c "./manage.py startapp services"
