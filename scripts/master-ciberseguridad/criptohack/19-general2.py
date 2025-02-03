#!/usr/bin/env python3

import signal 
import sys
import re
import subprocess

def def_handler(sig, frame):
    print(f'\n[!] Saliendo...')
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)

regex = r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b'

def get_crt_domain_html():
    comando = "curl -s 'https://crt.sh/?q=cryptohack.org&dir=^&sort=1&group=none'"
    response = subprocess.run(comando, shell=True, capture_output=True, text=True)
    
    if response != None:
        print(f'\t[+] Peticion exitosa\n')
    else:
        print(f'\t[-] Peticion no exitosa')
    
    with open('cert_dominios_ids.txt', 'w') as f:
        f.write(response.stdout)



def get_domains_list():
    with open("cert_dominios_ids.txt", 'r', encoding="utf-8") as file:
        content = file.read()

    domains = re.findall(regex, content)
    unique_domains = sorted(set(domains))
    for domain in unique_domains:
        print(domain)



if __name__=='__main__':
    get_crt_domain_html()
    get_domains_list()
