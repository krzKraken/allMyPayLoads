#!/bin/bash

# Para hosts que no se encuentra habilitado el ping puedes usar un
# echo '' /dev/tcp/<ip>/port y con el codigo de estado ver si esta
# Abierto y/o El host ACTIVO

function ctrl_c() {
  echo -e "\n\n[!] Saliendo...\n"
  tput cnorm
  exit 1
}

trap ctrl_c SIGINT

for host in $(seq 1 255); do
  tput civis
  for port in 21 22 23 25 53 80 110 139 143 161 389 443 445 465 514 587 631 873 902 993 995 1025 1352 1433 1521 2049 3306 3389 5432 5900 5985 5986 6379 8080 8443 9000; do
    (echo '' >/dev/tcp/192.168.1.$host/$port) 2>/dev/null && echo -e "[+] Host: 192.168.1.$host - Port: $port (OPEN)" &
  done

done

tput cnorm
