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

function ctrl_c() {
  echo -e "${redColour}\n\n[!] Saliendo...${endColour}\n"
  # Código de estado de salida no exitoso 1
  tput cnorm
  exit 1
}

# Ctrl + c
trap ctrl_c SIGINT

# Array de puertos
declare -a ports=($(seq 1 65535))

# Funcion CheckPort
function checkPort() {

  #Abriendo Descriptor de archivo con capacidad de lectura y escritura
  (exec 3<>/dev/tcp/$1/$2) 2>/dev/null
  if [ $? -eq 0 ]; then
    echo -e "${blueColour}[+] Host $1 - Port $2 (Open)${endColour}"
  fi
  # Cerrando los descriptores de archivos
  exec 3>&-
  exec 3<&-
}

tput civis # Ocultar el cursor
# Validación de argumento
if [ $1 ]; then
  # Si tiene argumento
  for port in ${ports[@]}; do
    # Iteración con check port
    checkPort $1 $port &
  done
else
  # Si no tiene argumento
  echo -e "${blueColour}\n[!] Uso: $0 <ip-address>${endColour}"
  echo -e "${blueColour}\n[!] Ejemplo: $0 192.168.1.1${endColour}"
fi

wait
tput cnorm
