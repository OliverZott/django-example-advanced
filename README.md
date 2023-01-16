# Advanced Django-Docker Example

[course](https://www.udemy.com/course/django-python-advanced/learn/lecture/32238716#announcements)


# Run & Debug

- Build new image: `docker-compose build`  
- Run Docker Service: `docker-compose run --rm app sh -c "python manage.py collectstatic"`
- Linting: `docker-compose run --rm app sh -c "flake8"`
- Unit Tests: `docker-compose run --rm app sh -c "python manage.py test`

# Setup Project

- Add Dockerhub Token as Github Action Secret:
    - Generate Docker token
    - Add Github Action secrets: username and token
- Docker / Django Setup

# Development Steps

- Python Requirements
- Docker

## Docker

- Dockerfile
    - base image
    - install dependencies
    - setup users
- Docker Compose
  - app-name
  - port mapping
  - volume mapping

Docker:  
- `docker build -t django-example .`
- `docker run -it -d --name django-example-app django-example`
- `docker-compose build`  
- `docker-compose run --rm app sh -c "python manage.py collectstatic"`  ...overwrites docker-compose.yml command
- Linting: `docker-compose run --rm app sh -c "flake8"` (/venv/bin/flake8)
- Unit Tests: `docker-compose run --rm app sh -c "python manage.py test`
