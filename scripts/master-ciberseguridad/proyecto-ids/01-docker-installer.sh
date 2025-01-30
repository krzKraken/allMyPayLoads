#!/bin/bash

# Instalation script for Arch Linux distro
# install docker docker-compose 

echo -e "[+] Installing docker and docker compose\n"
sudo pacman -Syu docker docker-compose 

echo -e "\n[+] Enable Docker service"
sudo systemctl enable --now docker 

echo -e "\n[+] Verify Docker is running..."
docker --version
docker-compose --version
