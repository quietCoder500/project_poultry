default:
    uv run manage.py runserver_plus

test:
    uv run manage.py test

run:
    uv run manage.py runserver_plus

format:
    ruff format

migrate:
    uv run manage.py makemigrations
    uv run manage.py migrate

css:
    npm run watch
