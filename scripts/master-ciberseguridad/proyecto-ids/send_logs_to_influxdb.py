#!/usr/bin/env python3


# send_logs_to_influxdb.py
import os
import re
import glob
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# Configuración de InfluxDB
token = "Rry39yZ5YOzls9yIn0WTYU1dUyDeFv9zEaNbp8J7yWpnHeTgrBLTMNrmu01pQSMc-hQU4zVh52VCtUuKGbIF7Q=="
org = "krakeninsane"
bucket = "krakeninsane"
url = "http://localhost:8086"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Ruta del log de Snort
log_path = "/var/log/snort/snort.log.*"

def parse_snort_log(line):
    # Ejemplo de log: [**] [1:1000001:1] ICMP Packet Detected [**] [Priority: 0] {ICMP} 192.168.1.1 -> 192.168.1.2
    match = re.match(r'\[\*\*\] \[\d+:(\d+):\d+\] (.+?) \[\*\*\] \[Priority: \d+\] \{(.+?)\} (.+?) -> (.+?)', line)
    if match:
        return {
            "sid": match.group(1),
            "message": match.group(2),
            "protocol": match.group(3),
            "src_ip": match.group(4),
            "dst_ip": match.group(5)
        }
    return None

def send_log_to_influxdb(log_entry):
    point = Point("snort_logs") \
        .tag("sid", log_entry["sid"]) \
        .tag("protocol", log_entry["protocol"]) \
        .tag("src_ip", log_entry["src_ip"]) \
        .tag("dst_ip", log_entry["dst_ip"]) \
        .field("message", log_entry["message"])
    write_api.write(bucket=bucket, org=org, record=point)

def main():
    for log_file in sorted(glob.glob(log_path)):
        with open(log_file, 'rb') as f:  # Modo binario
            for line in f:
                try:
                    line = line.decode('utf-8')  # Intentar decodificar a UTF-8
                except UnicodeDecodeError:
                    continue  # Ignorar líneas que no se pueden decodificar
                log_entry = parse_snort_log(line)
                if log_entry:
                    send_log_to_influxdb(log_entry)

if __name__ == "__main__":
    main()
