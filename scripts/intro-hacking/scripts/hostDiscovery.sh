#!/bin/bash

#Colours
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

# Controlando Salida Ctrl_c
function ctrl_c() {
  echo -e "${redColour}\n\n[!] Saliendo... \n${endColour}"
  tput cnorm
  exit 1
}

function checkHost() {
  host=$1$2
  (timeout 1 bash -c "ping -c 1 $host") &>/dev/null && echo -e "${blueColour}Host: $host - (Activo)${endColour}" &
}

# ctrl + c
trap ctrl_c SIGINT

ip=$(hostname -I | cut -d ' ' -f 1 | grep -oP '\d{1,3}+.\d{1,3}+.\d{1,3}+.')

declare -a hosts=($(seq 1 255))

if [ $1 ]; then
  tput civis
  for host in ${hosts[@]}; do
    checkHost $ip $host &
  done
else
  echo -e "${blueColour}[!] Uso: $0 <interface> <mascara-de-red>${endColour}"
fi

tput cnorm
wait
