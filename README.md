<p align="center">
 <p align="center">
   <a href="https://congento.org" target="_blank">
     <img src="congento.png" alt="CONGENTO" height="300">
   </a>
 </p>
</p>


## Docker: configurations available

| Compose file | Usage |
| --- | --- |
| `docker-compose.yml` | Launch a development server |
| `docker-compose.staging.yml` | Launch a staging server |
| `docker-compose.production.yml` | Launch a production server |


## Development

Clone this repository and install all dependencies.

```bash
git clone git@github.com:fchampalimaud/congento.git
cd congento
git pull --recurse-submodules
git submodule update --init --recursive
```

Configure the development environment from the example provided

```bash
cp .env.example .env
```

Build the image and launch it. To create an admin user or run any command inside the container, see the examples below.

```bash
docker-compose build
docker-compose up
docker-compose exec django pipenv run python manage.py createsuperuser
```


## Deployment

Clone this repository into the production machine and synchronize the submodules.

```bash
git clone --branch master --single-branch https://github.com/fchampalimaud/congento.git
cd congento
perl -i -p -e 's|git@(.*?):|https://\1/|g' .gitmodules
```

> **Note:** the `perl` script is required to change submodules URLs to `https://` schema.

Pull the latest modifications and update the submodules.

```bash
git pull --recurse-submodules
git submodule update --init --recursive
```

Configure environment variables in `.env`

```bash
cp .env.example .env
```

Launch the containers

```bash
docker-compose -f docker-compose.production.yml up --build -d
```


### Creating database dumps

```bash
docker-compose exec mysql sh -c 'export MYSQL_PWD="$MYSQL_ROOT_PASSWORD"; exec mysqldump --all-databases -uroot' > /some/path/on/your/host/all-databases.sql
```

### Restoring data from dump files

```bash
docker-compose exec -T mysql sh -c 'export MYSQL_PWD="$MYSQL_ROOT_PASSWORD"; exec mysql -uroot' < /some/path/on/your/host/all-databases.sql
```
