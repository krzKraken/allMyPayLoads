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
  echo -e "\n${redColour}\n\n[!] Saliendo...\n "
  exit 1
}

# Ctrl_c 
trap ctrl_c INT

function helpPanel(){
  echo -e "\n${yellowColour}[+]${endColour}${grayColour} USO:${endColour}\n"
  echo -e "\t${yellowColour}m)${endColour} ${grayColour}Money to play${endColour}"
  echo -e "\t${yellowColour}t)${endColour} ${grayColour}Technical to use ${endColour}${yellowColour}(martingala/inverselabrouchere)${endColour}"
  echo -e "\t${yellowColour}h)${endColour} ${grayColour}help Panel${endColour}"

}



function martingala(){
  money="$money"
  echo -e "${yellowColour}\n[?] Currentq money:${endColour} ${greenColour}\$$money${endColour}"
  echo -ne "${yellowColour}[?] How many money would you like bet?${endColour} ${greenColour}" && read initial_bet
  echo -ne "${yellowColour}[?] What do you want to bet? (odd/even) ${endColour}${greenColour}" && read even_odd
  
  echo -e "\n${yellowColour}[+] you are gonna play \$${endColour}${blueColour}$initial_bet${endColour}${yellowColour} to${endcolour} ${blueColour}$even_odd${endColour}\n"
  
  backup_initial_bet=$initial_bet


  tput civis
  # If the bet is odd (impar)
  if [ "$even_odd" == "odd" ]; then 

    while [ true ]; do
      
      money=$(($money - $initial_bet))
      echo -e "${yellowColour}[+]${endColour}${grayColour} You are going to bet${endcolour}${purpleColour} $initial_bet${endcolour}${grayColour} and your current money are: ${endcolour}${yellowColour}$money${endColour}"
      
      random_number="$(($RANDOM % 37))"
     
      if [ "$random_number" -eq 0 ]; then
        echo -e "${yellowColour}[-]${endColour}${grayColour}The random number is:${endColour}${yellowColour} $random_number${endColour}${redColour}, We lost!${endColour}"
        echo -e "${yellowColour}[+]${endColour}${grayColour} Your current money is: ${endColour} ${yellowColour}$money${endColour}\n"
        initial_bet=$(($initial_bet*2))

        
      elif [ "$(($random_number % 2))" -eq 0 ] ; then
        echo -e "${yellowColour}[-]${endColour}${grayColour}The random number is even:${endColour}${yellowColour} $random_number${endColour}${redColour}, We lost!${endColour}"
        echo -e "${yellowColour}[+]${endColour}${grayColour} Your current money is: ${endColour} ${yellowColour}$money${endColour}\n"
        initial_bet=$(($initial_bet*2))

      else
        echo -e "${yellowColour}[+]${endColour}${grayColour}The random number is odd:${endColour}${yellowColour} $random_number${endColour}${greenColour}, We won!${endColour}"
        reward=$(($initial_bet*2))
        money=$(($money+$reward))
        echo -e "${yellowColour}[+]${endColour}${grayColour} Your current money is: ${endColour} ${yellowColour}$money${endColour}\n"
        initial_bet=$backup_initial_bet

      fi 
      sleep 1
    done

  elif [ "$even_odd" == "even" ]; then
  # if the bet id even (par)
    while [[ true ]]; do
      random_number="$(($RANDOM % 37))"
      echo -e "ha salido el numero $random_number"
      if [ "$random_number" -eq 0 ]; then
        echo "Ha salido 0, perdemos"
      elif [ "$(($random_number % 2))" -eq 0 ] ; then
        echo "El Numero que ha salido es $random_number es par"
      else
        echo "El Numero que ha salido es impar"
      fi 
      sleep 2
    done
  

  else 
    echo -e "\n${redColour}[!] Only even or odd for this bet\n ${endColour}"
  fi
}

# While GETOPTS
while getopts "m:t:h" arg; do 
  case $arg in 
    m) money=$OPTARG;;
    t) technique=$OPTARG;;
    h) helpPanel;;

  esac 

done 

if [ "$money" ] && [ "$technique" ]; then
  echo "We are gonna play with \$$money and the $technique technique"
  if [ "$technique" == "martingala" ]; then
    martingala 
  else
    echo -e "\n${redColour} You choose a unavailable technique${endColour}\n"
    helpPanel
  fi
else 
  helpPanel
fi 

