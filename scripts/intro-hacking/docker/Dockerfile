# Sistema operativo a instalar 
FROM ubuntu:latest

# Creador 
MAINTAINER Cristhian Miranda aka krzkraken "kraken@gmail.com"

# Variable de entorno para no entrar en modo interactivo
ENV DEBIAN_FORNTEND noninteractive

# Comando que se ejecuta en la instalacion
RUN apt update && apt install -y net-tools \
  iputils-ping \
  curl \
  git \
  nano \
  wget \
  apache2 \
  php

# Puertos expuestos
EXPOSE 80

# Copiar archivos al contenedor
COPY test.txt /var/www/html/

# Comando que se ejecuta al arrancar el contenedor
ENTRYPOINT service apache2 start && /bin/bash 


