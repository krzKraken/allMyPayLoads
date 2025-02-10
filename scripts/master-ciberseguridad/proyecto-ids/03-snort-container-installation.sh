#!/usr/bin/bash

echo -e "\n[+] Creando contenedor para Snort\n"

# Descargar la imagen base y configurar contenedor
docker run -dit \
  --name snort_container \
  --network=host \
  ubuntu:latest

echo -e "\n[+] Instalando dependencias y Snort en el contenedor"
docker exec snort_container bash -c "
  apt update &&
  apt install -y snort tcpdump iputils-ping python3 python3-pip python3-venv &&
  python3 -m venv venv 
  source venv/bin/activate
  pip3 install influxdb-client --prefix=/usr/local 
  mkdir -p /etc/snort/rules &&
  echo 'alert icmp any any -> any any (msg:\"ICMP Packet Detected\"; sid:1000001;)' > /etc/snort/rules/local.rules &&
  echo 'include \$RULE_PATH/local.rules' >> /etc/snort/snort.conf
"

# Mostrar detalles del contenedor
echo -e "\n[+] Contenedor Snort configurado:"
docker ps

echo -e "\n[+] Snort listo para monitoreo. Para ejecutar manualmente:"
echo "docker exec snort_container snort -A console -q -c /etc/snort/snort.conf -i eno1"
