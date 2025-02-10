#!/usr/bin/bash

echo -e "\n[+] Creando contenedor para influxDB\n"

# Crear contenedor para influxDB 

docker run -dit \
  --name influxdb \
  -p 8086:8086 \
  influxdb:latest

echo -e "\n[+] Contenedor de influxDB configurado"
docker ps 

