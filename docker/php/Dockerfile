FROM php:fpm

COPY ./docker/php/php-fpm.conf /usr/local/etc/php-fpm.d/www.conf

COPY . /app

VOLUME ["/app"]

RUN apt update \
    apt install -y python3 \
    apt install -y python3-pip \
    pip3 install \
        RPi.GPIO
