#!/usr/bin/python3
#coding: utf-8

import sys
import ipaddress
import subprocess

if len(sys.argv) != 2:
    print("\n[!] Uso: python3 "+ sys.argv[0] + "<ip objetivo>\n")
    sys.exit(1)

ip_objetivo = sys.argv[1]

try:
    ip = ipaddress.ip_address(ip_objetivo)
except ValueError:
    print("\n[!] IP objetivo inválida")
    sys.exit(1)

try:
    subprocess.run(['qtile', 'cmd-obj', '-o', 'widget', 'target', '-f', 'update', '-a', ip_objetivo], check=True)    
    print(f"El texto del widget se actualizó a: {ip_objetivo}")
except subprocess.CalledProcessError as e:
    print(f"\n[!] Error al ejecutar el comando de Qtile: {e}")
    sys.exit(1)

