#!/bin/bash

# Recursive unziper 
# krzkraken 

# [+] Use:
#

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
  echo -e "\n\n ${redColour}[!] Saliendo... ${endColour}\n\n"
  exit 1
}

# Ctrl + c 
trap ctrl_c INT 

while [ $1 ]; do
  
  # Lectura de archivo
  first_file_name=$1
  decompresed_file=$(7z l data.gz | tail -n 3  | head -n 1 | awk 'NF{print $NF}')

  # Descomprimiendo archivo
  7z x $first_file_name &>/dev/null

  echo -e "\n\n ${greenColour}[+]${endColour} Descomprimiendo ${greenColour}$first_file_name${endColour} \n\n"

  while [ $decompresed_file ]; do
    echo -e "${greenColour}[+]${endColour} Nuevo archivo descomprimido: ${greenColour}$decompresed_file${endColour}"
    7z x $decompresed_file &>/dev/null
    decompresed_file=$(7z l $decompresed_file 2>/dev/null | tail -n 3  | head -n 1 | awk 'NF{print $NF}')
  done

done

echo -e "${redColour}\n\n[-] USE:${endColour}\n"
echo -e "${redColour}$0 [file_name]}"
exit 1




