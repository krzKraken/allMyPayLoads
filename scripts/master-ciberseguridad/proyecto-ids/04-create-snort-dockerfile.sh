#!/bin/bash

# set -e 
# Crear carpeta snort si no existe
mkdir -p snort/
cd snort || exit

echo -ne "\n[+] Creando DockerFile\n"
cat <<EOF > Dockerfile
FROM archlinux:latest
# instalar paquetes necesarios
RUN pacman -Syu --noconfirm && pacman -S --noconfirm snort
# Copiar configuración personalizada 
COPY snort.conf /etc/snort/snort.conf
# Ejecutar Snort en modo IDS
CMD ["snort", "-A", "console", "-q", "-c", "/etc/snort/snort.conf", "-i", "wlan0"]
EOF

echo -ne "\n[+] Dockerfile creado...\n"

echo -ne "\n[+] Copiando snort.conf de snort-comunnity.rules"

