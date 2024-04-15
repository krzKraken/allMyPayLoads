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


# ctrl_c handler  
function ctrl_c(){
  tput cnorm
  echo -e " ${redColour}\n\n Exiting... ${endColour}" 
  exit 1
}

trap ctrl_c INT

# Variables globales
main_url="https://htbmachines.github.io/bundle.js"


# Function Help Panel
function helpPanel (){
  echo -e "\n${yellowColour}[+]${endColour} ${grayColour} Uso: ${endColour}"
  echo -e "\t${purpleColour}-m)${endColour}${grayColour} Buscar por nombre de maquina${endColour}"
  echo -e "\t${purpleColour}-u)${endColour}${grayColour} Actualizar base de datos${endColour}"
  echo -e "\t${purpleColour}-h)${endColour}${grayColour} Mostrar este panel de ayuda${endColour}"
}

# Function search Machine
function searchMachine(){
  machineName="$1"
  echo "$machineName"
}
# Update bundle.js 
function updateFiles(){
  if [ ! -f bundle.js ]; then
    echo -e "${greenColour}[+]${endColour} El archivo no existe...\nEmpezando las actualizaciones...\n"
    tput civis 
    curl -s -X GET $main_url | js-beautify > bundle.js 
    echo -e "Todos los archivos fueron descargados..."
    tput cnorm
  else
    echo -e "El archivo existe..."
  fi
}

# Indivators declaration for integer variable
declare -i parameter_counter=0 

while getopts "m:uh" arg; do 
  case $arg in 
    m) machineName=$OPTARG; let parameter_counter+=1;;
    u) let parameter_counter=2;;
    h) ;;
    
  esac 
done   

if [ $parameter_counter -eq 1 ]; then 
  searchMachine $machineName 
elif [ $parameter_counter -eq 2 ]; then
  updateFiles
else 
  helpPanel 
fi 
