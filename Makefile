dev:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

lint:
	poetry run flake8 task_manager

test:
	poetry run python manage.py test

makemessages:
	 django-admin makemessages --ignore="static" --ignore=".env" -l ru

compilemessages:
	django-admin compilemessages
	
test-coverage:
	poetry run coverage run --source='task_manager' manage.py test task_manager
	poetry run coverage xml
