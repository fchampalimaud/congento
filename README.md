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

Make sure you have SSH keys configured for the production machine.

Clone this repository into the production manchine and synchronize the submodules.

```bash
git clone git@github.com:fchampalimaud/congento-server.git
git pull --recurse-submodules
git submodule update --init --recursive
```

Configure environment variables in `.env`

```bash
cp .env.example .env
```

Launch the containers

```bash
docker-compose -f docker-compose.prod.yml up --build -d
```


### Creating database dumps

```bash
docker-compose exec mysql sh -c 'export MYSQL_PWD="$MYSQL_ROOT_PASSWORD"; exec mysqldump --all-databases -uroot' > /some/path/on/your/host/all-databases.sql
```

### Restoring data from dump files

```bash
docker-compose exec -T mysql sh -c 'export MYSQL_PWD="$MYSQL_ROOT_PASSWORD"; exec mysql -uroot' < /some/path/on/your/host/all-databases.sql
```


## Notes

...
