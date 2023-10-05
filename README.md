## govelo

### Run using docker

- **Docker** Command For `build`

      $ docker-compose -f local.yml build

- Makemigrations and migrate

      $ docker-compose -f local.yml run --rm django python manage.py makemigrations
      $ docker-compose -f local.yml run --rm django python manage.py migrate

- or Create 4 Superusers in one command:

      $ docker-compose -f local.yml run --rm django python manage.py sample

- generate metadata:

      $ docker-compose -f local.yml run --rm django python manage.py loaddata shop.json
      $ docker-compose -f local.yml run --rm django python manage.py loaddata static.json

- To create a **superuser**, use this command:

      $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

- **Docker** Command For `up` or run

      $ docker-compose -f local.yml up
