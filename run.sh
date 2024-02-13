
docker network create --subnet=172.10.0.0/16 intNetwork
docker run -d --name mysql --ip 172.10.0.10 -p 3306:3306 --network=intNetwork mon_image_mysql
docker run -d --name python --ip 172.10.0.20  -p 8000:8080 --network=intNetwork mon_image_python
docker run -d --name nginx --ip 172.10.0.30 -p 80:80 --network=intNetwork mon_image_nginx
docker run --name newman --ip 172.10.0.40 -p 6000:6000 --network=intNetwork mon_image_newman