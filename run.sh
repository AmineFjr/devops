docker network rm intNetwork || true
docker network create --subnet=172.10.0.0/16 intNetwork
cd docker/mysql && docker run -d --name wildfly1 --ip 172.10.0.10 -h wildfly1 -p 3306:3306 --network=intNetwork mon_image_mysql
cd ../python && docker run -d --name wildfly2 --ip 172.10.0.20 -h wildfly2 -p 8080:8080 --network=intNetwork my_python_app