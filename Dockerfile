FROM python:3.7

LABEL maintainer="Scientific Software Platform"

ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT 1

RUN apt-get update && \
    apt-get -y install --upgrade \
      # bash \
      # locales \
      # locales-all \
      # wget \
      apache2 \
      apache2-dev \
      default-mysql-client \
      default-libmysqlclient-dev \
      libcurl4-openssl-dev \
      libssl-dev \
      libffi-dev \
      libxml2-dev \
      libxslt1-dev \
      libapache2-mod-wsgi-py3
      # python3-opencv

# ENV LC_ALL en_US.UTF-8
# ENV LANG en_US.UTF-8
# ENV LANGUAGE en_US.UTF-8

# Requirements are installed here to ensure they will be cached.
RUN pip install pipenv
COPY ./Pipfile* /setup/
COPY ./libraries/pyforms-web /setup/libraries/pyforms-web
COPY ./plugins/confirm-users-app /setup/plugins/confirm-users-app
COPY ./plugins/notifications-central /setup/plugins/notifications-central
RUN cd /setup && \
    pipenv install --deploy --ignore-pipfile && \
    #pipenv install --deploy && \
    pipenv run pip list && \
    cd /

COPY ./entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

## Add the wait script to the image
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.6.0/wait /wait
RUN chmod +x /wait

WORKDIR /app

EXPOSE 80 443

ENTRYPOINT ["/entrypoint"]