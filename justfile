default:
    uv run manage.py runserver_plus

test:
    uv run manage.py test

run:
    uv run manage.py runserver_plus 0.0.0.0:8000

format:
    ruff format

migrate:
    uv run manage.py makemigrations
    uv run manage.py migrate

css:
    npm run watch
