cd docker/mysql && docker build -t mon_image_mysql .
cd ../python && docker build -t mon_image_python .
cd ../nginx && docker build -t mon_image_nginx .
cd ../newman && docker build -t mon_image_newman .
cd ../../