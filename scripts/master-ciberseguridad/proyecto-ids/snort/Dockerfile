FROM archlinux:latest
# instalar paquetes necesarios
RUN pacman -Syu --noconfirm && pacman -S --noconfirm snort
# Copiar configuración personalizada 
COPY snort.conf /etc/snort/snort.conf
# Ejecutar Snort en modo IDS
CMD ["snort", "-A", "console", "-q", "-c", "/etc/snort/snort.conf", "-i", "wlan0"]
