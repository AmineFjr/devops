cd docker/mysql && docker run -d -p 3306:3306 --name mon_conteneur_mysql mon_image_mysql
cd ../python && docker run -d -p 3000:5000 --name mon_conteneur_python my_python_app