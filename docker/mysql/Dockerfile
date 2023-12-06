FROM mysql:latest

ENV MYSQL_DATABASE=iterator-dv
ENV MYSQL_USER=esgi
ENV MYSQL_PASSWORD=azerty
ENV MYSQL_ROOT_PASSWORD=azerty

EXPOSE 3306

# Lorsque le conteneur démarre, MySQL est exécuté automatiquement
CMD ["mysqld"]

COPY 1-SCHEMA.sql /docker-entrypoint-initdb.d/
COPY 2-PRIVILEGES.sql /docker-entrypoint-initdb.d/

