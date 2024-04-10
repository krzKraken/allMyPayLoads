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


function ctrl_c(){
  echo -e "${redColour}\n\n[!] Saliendo..\n\n${endColour}"
  exit 1
}

# Ctrl + C 
trap ctrl_c INT

if [ ! $1]; then
  echo -e "${redColour} [!] USE: \n\n [!] $0 [HOST-IP] \n\n Example: $0 192.168.0.1 ${endColour}"
  exit 1 
fi

 
host=$1
echo -e "${greenColour} [+] Leyendo en host: $host"
for port in $(seq 1 65565); do 
  (echo '' > /dev/tcp/$host/$port) 2>/dev/null && echo -e "\t${greenColour}[+]${endColour} Puerto ${yellowColour}$port${endColour} - ${greenColour}OPEN${endColour}" &
done; wait


