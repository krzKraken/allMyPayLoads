#!/bin/bash 

# Descargando community rules 
echo -ne "\n[+] Descargando snorf community rules\n"

wget -O snort.tar.gz https://www.snort.org/downloads/community/snort3-community-rules.tar.gz

# Descomprimiendo reglas
echo -ne "\n[+] Descomprimiendo fichero\n"
tar -xvzf snort.tar.gz

rm snort.tar.gz

