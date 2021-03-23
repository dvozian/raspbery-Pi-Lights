FROM php:fpm

# Copy the php config file
COPY ./docker/php/php-fpm.conf /usr/local/etc/php-fpm.d/www.conf

# Copy the application code
COPY . /app

VOLUME ["/app"]

#RUN apt update \
#    apt install -y python3 \
#    apt install -y python3-pip \
#    pip3 install \
#        RPi.GPIO

