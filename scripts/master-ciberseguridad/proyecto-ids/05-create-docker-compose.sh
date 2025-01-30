#!/bin/bash

echo -ne "\n[+] Copiando snort.conf de snort-community.rules\n"
cp ./snort3-community-rules/snort3-community.rules ./snort/snort.conf

echo -ne "\n[+]Crea docker-compose.yml\n"

cat <<EOF > docker-compose.yml
version: '3'
services:
  snort:
    build: ./snort 
    container_name: snort
    networks:
      - ids_network
    cap_add:
      - NET_ADMIN # permite capturar trafico enla interfaz
    restart: unless-stopped

networks:
  ids_network:
    driver: bridge
EOF

echo -ne "\n[+] docker-compose creado\n"

echo -ne "\n[+] Construyendo contenedor snort\n"
docker-compose up -d --build 
