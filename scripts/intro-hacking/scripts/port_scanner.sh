#!/bin/bash 

# Descubrimient de puertos usando descriptores de estados. 

function ctrl_c() {
  echo -e '\n\n[!] Saliendo...\n\n '
  tput cnorm; exit 1
}

#Ctrl + C 
trap ctrl_c SIGINT

# Array de ports [1 2 3 4 5...65535]
declare -a ports=( $(seq 1 65535) )
# Iteramos por cada valor del array

function checkPort(){
  host=$1
  port=$2
  
  # Creando descriptor de archivo 
  (exec 3<> /dev/tcp/$host/$port) 2>/dev/null

  if [ $? -eq 0 ]; then
    echo -e "[+] Host $host - Port $port (OPEN)"
  fi 
  
  # Cerrando descriptor de archivo 
  exec 3>&-
  exec 3<&-

}
tput civis # ocultar el cursor 
if [ $1 ]; then
  for port in ${ports[@]}; do 
    checkPort $1 $port
  done
else
  echo -e "\n[!] Uso: $0 <ip-address>"
fi 

wait 
tput cnorm # Mostrar el cursor 
