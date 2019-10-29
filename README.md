# congento-server

[Congento](https://congento.org/)


## Development

Clone this repository and install all dependencies.

```bash
git clone git@github.com:fchampalimaud/congento-server.git
git pull --recurse-submodules
git submodule update --init --recursive

pipenv sync --dev
```

Configure the development environment from the example provided

```bash
cp .env.example .env
```

Setup MySQL database schema `congentodb` and apply the migrations.

```bash
python manage.py migrate
```

Use a local running instance of [MailHog](https://github.com/mailhog/MailHog)
to test e-mails.


## Development with Docker

```bash
docker-compose build
docker-compose up
docker-compose run django pipenv run python manage.py createsuperuser
```


## Deployment

...


## Notes

...
