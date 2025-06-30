#!/bin/bash

function ctrl_c() {
  echo -e "\n\n[!] Saliendo...\n"
  tput cnorm
  exit 1
}

trap ctrl_c SIGINT

# Ping a host

for host in $(seq 1 255); do
  tput civis
  # echo -e "[+] 192.168.1.$host"
  (timeout 1 bash -c "ping -c 1 192.168.1.$host &>/dev/null") && echo -e "[+] Host: 192.168.1.$host - ACTIVE" &
done

tput cnorm
wait
