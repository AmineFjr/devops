FROM mysql:8.1.0

ENV MYSQL_ROOT_PASSWORD=azerty

COPY 1-SCHEMA.sql /docker-entrypoint-initdb.d/
COPY 2-PRIVILEGES.sql /docker-entrypoint-initdb.d/

