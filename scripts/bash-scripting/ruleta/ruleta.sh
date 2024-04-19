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
  good_plays_counter=0
  bad_plays_counter=0

  tput civis
  while [ true ]; do 
    if [ $money -gt 0 ]; then # && [ $initial_bet -le $money ]; then
      # If the bet is odd (impar)
      if [ "$even_odd" == "odd" ]; then 
        money=$(($money - $initial_bet))
        echo -e "${yellowColour}[+]${endColour}${grayColour} You are going to bet${endcolour}${purpleColour} $initial_bet${endcolour}${grayColour} and your current money are: ${endcolour}${yellowColour}$money${endColour}"
        
        random_number="$(($RANDOM % 37))"
        if [ "$random_number" -eq 0 ]; then
          echo -e "${yellowColour}[-]${endColour}${grayColour}The random number is:${endColour}${yellowColour} $random_number${endColour}${redColour}, We lost!${endColour}"
          echo -e "${yellowColour}[+]${endColour}${grayColour} Your current money is: ${endColour} ${yellowColour}$money${endColour}\n"
          initial_bet=$(($initial_bet*2))
          let bad_plays_counter+=1
          echo -e "${yellowColour}[?]${endColour} ${grayColour}#goods:${endColour} ${greenColour}$good_plays_counter${endColour} ${grayColour}#bads:${endColour}${redColour}$bad_plays_counter${endColour}  "

          
        elif [ "$(($random_number % 2))" -eq 0 ] ; then
          echo -e "${yellowColour}[-]${endColour}${grayColour}The random number is even:${endColour}${yellowColour} $random_number${endColour}${redColour}, We lost!${endColour}"
          echo -e "${yellowColour}[+]${endColour}${grayColour} Your current money is: ${endColour} ${yellowColour}$money${endColour}\n"
          initial_bet=$(($initial_bet*2))
          let bad_plays_counter+=1
          echo -e "${yellowColour}[?]${endColour} ${grayColour}#goods:${endColour} ${greenColour}$good_plays_counter${endColour} ${grayColour}#bads:${endColour}${redColour}$bad_plays_counter${endColour}  "


        else
          echo -e "${yellowColour}[+]${endColour}${grayColour}The random number is odd:${endColour}${yellowColour} $random_number${endColour}${greenColour}, We won!${endColour}"
          reward=$(($initial_bet*2))
          money=$(($money+$reward))
          echo -e "${yellowColour}[+]${endColour}${grayColour} Your current money is: ${endColour} ${yellowColour}$money${endColour}\n"
          initial_bet=$backup_initial_bet
          good_plays_counter=$(($good_plays_counter+1))
          echo -e "${yellowColour}[?]${endColour} ${grayColour}#goods:${endColour} ${greenColour}$good_plays_counter${endColour} ${grayColour}#bads:${endColour}${redColour}$bad_plays_counter${endColour}  "


        fi 
      # if the bet id even (par)
      elif [ "$even_odd" == "even" ]; then
        money=$(($money - $initial_bet))
        echo -e "${yellowColour}[+]${endColour}${grayColour} You are going to bet${endcolour}${purpleColour} $initial_bet${endcolour}${grayColour} and your current money are: ${endcolour}${yellowColour}$money${endColour}"
        
        random_number="$(($RANDOM % 37))"
        if [ "$random_number" -eq 0 ]; then
          echo -e "${yellowColour}[-]${endColour}${grayColour}The random number is:${endColour}${yellowColour} $random_number${endColour}${redColour}, We lost!${endColour}"
          echo -e "${yellowColour}[+]${endColour}${grayColour} Your current money is: ${endColour} ${yellowColour}$money${endColour}\n"
          initial_bet=$(($initial_bet*2))
          bad_plays_counter=$(($bad_plays_counter+1))
          echo -e "${yellowColour}[?]${endColour} ${grayColour}#goods:${endColour} ${greenColour}$good_plays_counter${endColour} ${grayColour}#bads:${endColour}${redColour}$bad_plays_counter${endColour}  "


          
        elif [ "$(($random_number % 2))" -eq 0 ] ; then
          echo -e "${yellowColour}[+]${endColour}${grayColour}The random number is odd:${endColour}${yellowColour} $random_number${endColour}${greenColour}, We won!${endColour}"
          reward=$(($initial_bet*2))
          money=$(($money+$reward))
          echo -e "${yellowColour}[+]${endColour}${grayColour} Your current money is: ${endColour} ${yellowColour}$money${endColour}\n"
          initial_bet=$backup_initial_bet 
          good_plays_counter=$(($good_plays_counter+1))
          echo -e "${yellowColour}[?]${endColour} ${grayColour}#goods:${endColour} ${greenColour}$good_plays_counter${endColour} ${grayColour}#bads:${endColour}${redColour}$bad_plays_counter${endColour}  "

         


        else
          echo -e "${yellowColour}[-]${endColour}${grayColour}The random number is even:${endColour}${yellowColour} $random_number${endColour}${redColour}, We lost!${endColour}"
          echo -e "${yellowColour}[+]${endColour}${grayColour} Your current money is: ${endColour} ${yellowColour}$money${endColour}\n"
          initial_bet=$(($initial_bet*2))
          bad_plays_counter=$(($bad_plays_counter+1))
          echo -e "${yellowColour}[?]${endColour} ${grayColour}#goods:${endColour} ${greenColour}$good_plays_counter${endColour} ${grayColour}#bads:${endColour}${redColour}$bad_plays_counter${endColour}  "


        fi 
      else
        echo "${redColour}\n[!] You only can play (odd/even)\n${endColour}"
      fi 

    else 
      # You are broken
      echo -e "\n${redColour}[!] You lost all your money...!! ${endColour}\n"
      tput cnorm
      exit 0 
    fi 
done
}

function inverseLanbrouchere(){ 
  echo -e "${yellowColour}[+]${endColour} ${grayColour} Current money ${endColour}${yellowColour}$money${endColour}"
  echo -en "${yellowColour}[?]${endColour} ${grayColour} Where do you want to bet? (odd/even): ${endColour}${yellowColour}" && read even_odd
  echo -e "${endColour}"
  declare -a my_sequence=(1 2 3 4)
  echo -e "\n${yellowColour}[+]${endColour}${grayColour}We start with the sequence: ${endColour} ${greenColour}[${my_sequence[@]}]${endColour}"
  bet=$((${my_sequence[0]}+${my_sequence[-1]}))
  money=$(($money - $bet))
  unset my_sequence[0]
  unset my_sequence[-1]
  my_sequence=(${my_sequence[@]})

  echo -e "${yellowColour}[+]${endColour}${grayColour} we bet: ${endColour}${greenColour}\$$bet${endColour} ${grayColour}--> current sequence ${endColour}${blueColour}[${my_sequence[@]}]${endColour}"
  echo -e "${yellowColour}[+]${endColour} ${grayColour}Tenemos${endColour}${yellowColour} \$$money${endColour}"
  tput civis
  while [ true ]; do 
    random_number=$(($RANDOM % 37))
    
    if [ "$even_odd" == "even" ]; then
      if [ $random_number == 0 ]; then
        echo -e "${yellowColour}[!]${endColour} ${grayColour}We got the number:${endColour} ${blueColour}$random_number${endColour}${redColour} YOU LOSE!${endColour}"
        

      elif [ $(($random_number % 2)) -eq 0 ]; then 
        echo -e "${yellowColour}[+]${endColour} ${grayColour}We got the number:${endColour} ${blueColour}$random_number${endColour}${greenColour} YOU WON!${endColour}"
        reward=$(($bet*2))
        let money+=$bet 
        echo -e "${yellowColour}[+]${endColour}${grayColour} we have${endColour} \$$money"
        let my_sequence+=($bet)
        my_sequence=(${my_sequence[@]})
        if [ ${#my_sequence[@]} -gt 1 ]; then
          let bet=$((${my_sequence[0]}+${my_sequence[-1]}))
          echo "${yellowColour}[+]${endColour}${grayColour} Your new sequence is: ${endColour}${greenColour}${my_sequence[@]}${endColour}"
          echo "[+] The new Bet is: ${blueColour}$bet${endColour}"
        elif [ ${#my_sequence[@]} -eq 1 ];
          

        sleep 0.3
      else 
        echo -e "${yellowColour}[!]${endColour} ${grayColour}We got the number:${endColour} ${blueColour}$random_number${endColour}${redColour} YOU LOSE!${endColour}"
      fi 

    elif [ "$even_odd" == "odd" ]; then
      echo "todo: odd case"

    else 
      echo "\n${redColour}[-] You need to choose between (martingala/inverselabrouchere)\n"
      tput cnorm
      exit 0 
    fi 
  done
  tput cnorm



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
  elif [ "$technique" == "inverselabrouchere"  ]; then
    inverseLanbrouchere 
  else
    echo -e "\n${redColour} You choose a unavailable technique${endColour}\n"
    helpPanel
  fi
else 
  helpPanel
fi 

