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
  echo -e "\t${purpleColour}m)${endColour}${grayColour} Buscar por nombre de maquina${endColour}"
  echo -e "\t${purpleColour}i)${endColour}${grayColour} Buscar por direccion ip${endColour}"
  echo -e "\t${purpleColour}o)${endColour}${grayColour} Buscar por sistema operativo${endColour}"
  echo -e "\t${purpleColour}s)${endColour}${grayColour} Buscar por skills Ej: (\"Active Directory\")${endColour}"
  echo -e "\t${purpleColour}y)${endColour}${grayColour} Obtener enlace de resolucion de la maquina${endColour}"
  echo -e "\t${purpleColour}u)${endColour}${grayColour} Actualizar base de datos${endColour}"
  echo -e "\t${purpleColour}h)${endColour}${grayColour} Mostrar este panel de ayuda${endColour}"
}
# Update bundle.js 
function updateFiles(){
  tput civis
  echo -e "${yellowColour}[+]${endColour} ${grayColour}Verificando todos los archivos necesarios...${endColour}\n"
  sleep 2
  if [ ! -f bundle.js ]; then
    echo -e "${greenColour}[+]${endColour} El archivo no existe... Descargando.....\n"
    sleep 2

    tput civis 
    curl -s -X GET $main_url | js-beautify > bundle.js 
    echo -e "Todos los archivos fueron descargados..."
    tput cnorm

  else
    echo -e "${yellowColour}[!] ${endColour}${grayColour}El archivo existe, verificando se encuentre actualizado...\n${endColour}"
    curl -s -X GET $main_url | js-beautify > bundle_temp.js 
    md5sum_temp_value=$(md5sum bundle_temp.js | awk '{print $1}')
    md5sum_original_value=$(md5sum bundle.js | awk '{print $1}')
    if [ "$md5sum_original_value" == "$md5sum_temp_value" ]; then
      echo -e "\n${yellowColour}[-]${endColour}${grayColour} No existen actualizaciones pendientes...\n${endColour}"
      rm bundle_temp.js
    else 
      echo -e "\n${yellowColour}[+]${endColour}${grayColour} Existen Actualizaciones disponibles...!\n${endColour}"
      rm bundle.js && mv bundle_temp.js bundle.js
    fi 
  fi
  tput cnorm 
}

# Function search Machine
function searchMachine(){
  machineName="$1"
  machineName_cheker="$(cat bundle.js | awk "/name: \"$machineName\"/,/resuelta:/" | grep -vE "id|sku|resuelta" | tr -d '"' | tr -d ',' | sed 's/^ *//')"
  if [ "$machineName_cheker" ]; then  
    echo -e "${greenColour}[+]${endColour} ${grayColour}Listando las propiedades de la maquina:${endColour} ${blueColour}$machineName${endColour}\n"
    cat bundle.js | awk "/name: \"$machineName\"/,/resuelta:/" | grep -vE "id|sku|resuelta" | tr -d '"' | tr -d ',' | sed 's/^ *//'
  else 
    echo -e "${redColour}[!]${endColour} La maquina solicitada no existe...\n"
  fi
} 

function searchIP(){
  ipAddress="$1"
  machineName=$(cat bundle.js | grep "$ipAddress" -B 5 | grep "name: " | awk 'NF{print $NF}' | tr -d '",')
  if [ "$machineName" ]; then
    echo -e "\n${greenColour}[+]${endColour} La máquina que corresponde a la IP ${purpleColour}$ipAddress${endColour} es: ${blueColour}$machineName${endColour}\n"
  searchMachine $machineName
  else 
    echo -e "${redColour}[!]${endColour} La ip proporcionada no existe...\n"
  fi
}

function getYouTubeLink(){
  machineName="$1" 

  youtubeLink="$(cat bundle.js | awk "/name: \"$machineName\"/,/resuelta:/" | grep -vE "id|sku|resuelta" | tr -d '"' | tr -d ',' | sed 's/^ *//' | grep "youtube: " | awk 'NF{print $NF}')"
  if [ "$youtubeLink" ]; then 
    echo -e "${greenColour}\n[+]${endColour}${grayColour} El link de la maquina${endColour} ${purpleColour} $machineName${endColour}${grayColour} es: ${endColour}${greenColour}$youtubeLink${endColour}"
  else
    echo -e "${redColour}\n[!]${endColour}${grayColour} No existe link para la maquina: ${endColour}${purpleColour}$machineName${endColour}"
  fi
}
function getMachinesDificulty(){
  dificultad="$1"

  machinesNames="$(cat bundle.js | js-beautify | grep -i "dificultad: \"$dificultad\"" -B 5  | grep "name: " | awk 'NF {print $NF}' | tr -d ',"' | column)"
  if [ "$machinesNames" ]; then
    echo -e "\n${greenColour}[+]${endColour} ${grayColour}Las maquinas de dificultad${endColour} ${purpleColour}$dificultad${endColour}${grayColour}:${endColour}"
    echo -e "${purpleColour}$machinesNames ${endColour}"
  else
    echo -e "${redColour}\n[!]${endColour}${grayColour} No se encontraron máquinas para la dificultad:${endColour} ${purpleColour}$dificultad${endColour}\n" 
  fi 
}
function getMachinesOS(){
  sistemaOperativo="$1"
  machinesNames="$(cat bundle.js | grep "so: " -B 5 | cat bundle.js | grep -i "so: \"$sistemaOperativo\"" -B 5 | grep "name: " | awk 'NF{print $NF}' | tr -d ',"' | column)"
  if [ "$machinesNames" ]; then
    echo -e "\n${greenColour}[+]${endColour}${grayColour}Las maquinas con sistema operativo ${endColour}${purpleColour}$sistemaOperativo${endColour} ${grayColour}son:${endColour}\n"
    echo -e "${purpleColour}$machinesNames${endColour}"
  else

    echo -e "${redColour}\n[!]${endColour}${grayColour} No se encontraron máquinas para el sistema operativo: ${endColour} ${purpleColour}$sistemaOperativo${endColour}\n" 
  fi 

}
 
function getOSDifficultyMachines(){

  dificultad="$1"
  sistemaOperativo="$2" 
  
  echo -e "\n${greenColour}[+]${endColour} ${grayColour}Buscando por dificultad: ${endColour} ${purpleColour}$dificultad${endColour}${grayColour} y sistema operativo: ${endColour}${purpleColour} $sistemaOperativo${endColour}\n"
  machinesNames="$(cat bundle.js | grep -i "dificultad: \"$dificultad\"" -B 6  | grep -i "so: \"$sistemaOperativo\"" -B 5 | grep "name: " | awk 'NF{print $NF}' | tr -d ',"' | column)"
  if [ ! "$machinesNames" ]; then
    echo -e "${redColour}\n[!]${endColour}${grayColour} No se encontraron máquinas de dificultad: ${endColour} ${purpleColour}$dificultad${endColour} ${grayColour}y sistema operativo:${endColour}${purpleColour}$sistemaOperativo${endColour}\n" 
  fi
    echo -e "${purpleColour}$machinesNames${endColour}"

}

function getSkillMachines(){
  skills="$1"
  echo -e "\n${greenColour}[+]${endColour}${grayColour}Buscando por la Skill:${endColour}${purpleColour} $skills${endColour}\n"
  machinesNames="$(cat bundle.js | grep -i "$skills" -B 7 | grep "name: " | awk 'NF{print $NF}' | tr -d ',"' | column)"
  
  if [ "$machinesNames" ]; then 
    echo -e "\n${greenColour}[+]${endColour}${grayColour}Las maquinas para la skill:${endColour} $skills${endColour} ${grayColour}son:${endColour}"
    echo -e "$machinesNames"
  else 
    
    echo -e "${redColour}\n[!]${endColour}${grayColour} No se encontraron máquinas para la skill: ${endColour}${purpleColour}$skills${endColour}\n" 
  fi 

}

# Indivators declaration for integer variable
declare -i parameter_counter=0

#Chivatos
declare -i chivato_dificultad=0 
declare -i chivato_sistemaOperativo=0 

while getopts "m:ui:y:d:o:s:h" arg; do 
  case $arg in 
    m) machineName=$OPTARG; let parameter_counter+=1;;
    u) let parameter_counter=2;;
    i) ipAddress=$OPTARG; let parameter_counter=3;;
    y) machineName=$OPTARG; let parameter_counter=4;;
    d) dificultad=$OPTARG; chivato_dificultad=1; let parameter_counter=5;;
    o) sistemaOperativo=$OPTARG; chivato_sistemaOperativo=1; let parameter_counter=6;;
    s) skills=$OPTARG; parameter_counter=7;; 
    h) ;;

  esac 
done   

if [ $parameter_counter -eq 1 ]; then 
  searchMachine $machineName 
elif [ $parameter_counter -eq 2 ]; then
  updateFiles
elif [ $parameter_counter -eq 3 ]; then
  searchIP $ipAddress
elif [ $parameter_counter -eq 4 ]; then
  getYouTubeLink $machineName
elif [ $chivato_dificultad -eq 1 ] && [ $chivato_sistemaOperativo -eq 1 ]; then
  getOSDifficultyMachines $dificultad $sistemaOperativo
elif [ $parameter_counter -eq 5 ]; then
  getMachinesDificulty $dificultad
elif [ $parameter_counter -eq 6 ]; then
  getMachinesOS $sistemaOperativo
elif [ $parameter_counter -eq 7 ]; then
  getSkillMachines "$skills"
else
  helpPanel 
fi 
