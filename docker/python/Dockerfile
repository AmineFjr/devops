FROM python:3.9

WORKDIR /usr/src/app

# Installez le module mysql-connector
RUN pip install mysql-connector

# Copiez le code source dans le conteneur
COPY . .


CMD ["python", "./backend/main.py"]
