build:
		docker-compose build

run-rm-createsuperuser:
		docker-compose run --rm web-app sh -c "python manage.py createsuperuser"

run-rm-migrate:
		docker-compose run --rm web-app sh -c "python manage.py migrate"

run-rm-startproject:
		docker-compose run --rm web-app sh -c "django-admin startproject config ."

up-d:
		docker-compose up -d