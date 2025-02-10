#!/usr/bin/bash

echo -e "[+] Creando contenedor con Ubuntu Server (ubuntu-server)"
# Crear contenedor de Ubuntu Server
docker run -dit \
  --name ubuntu_server \
  --hostname ubuntu-server \
  -p 8080:80 -p 2222:22 \
  ubuntu:latest

echo -e "\n[+] Instalando paquetes básicos (SSH y Apache)"
# Actualizar repositorios, instalar SSH y Apache
docker exec ubuntu_server bash -c "
  apt update &&
  apt install -y openssh-server apache2 &&
  echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config &&
  echo 'Bienvenido!' > /var/www/html/index.html &&
  service ssh restart &&
  service apache2 start
"

# Configurar contraseña para root de forma automatizada
echo -e "\n[+] Configurando contraseña para usuario root"
docker exec -it ubuntu_server bash -c "
  echo 'root:admin' | chpasswd
"

echo -e "\n[+] Mostrando información del contenedor..."
docker ps

echo -e "\n[+] Configuración completada."
echo "[*] Accede a la web en: http://localhost:8080"
echo "[*] Acceso SSH disponible en: ssh -p 2222 root@localhost (Contraseña: admin)"
