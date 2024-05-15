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

# ctrol + c 
function ctrl_c(){
  echo -e "\n\n${redColour}[!] Saliendo...${endColour}"
  exit 1
}

trap ctrl_c INT


ip=$(hostname -I  | tr '.' '\n' | head -n 3 | tr '\n' '.' | xargs)


echo -e "${greenColour}[+] ${endColour} Iniciando escaneo en red ${greenColour}$ip${endColour}0/24"

# Ocultar el cursor
tput civis

for i in $(seq 1 256); do 
  (ping -c 1 $ip$i &>/dev/null) && echo "[+] host $ip$i - Active" & 
done; wait

#Recupera el cursor
tput cnorm

