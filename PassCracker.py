#!/usr/bin/env python3

import hashlib, signal, sys

def handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, handler)

banner = r'''

 __  __ ____  ____     ____                _    _             
|  \/  |  _ \| ___|   / ___|_ __ __ _  ___| | _(_)_ __   __ _ 
| |\/| | | | |___ \  | |   | '__/ _` |/ __| |/ / | '_ \ / _` |
| |  | | |_| |___) | | |___| | | (_| | (__|   <| | | | | (_| |
|_|  |_|____/|____/___\____|_|  \__,_|\___|_|\_\_|_| |_|\__, |
                 |_____|                                |___/
                                                   Anonymous17
'''
print(banner)

encontrado = 0
input_hash = input("\n [*] Inserte la contraseña hasheada: ")
pass_doc = input(" [*] Inserte el diccionario: ")

try:
    pass_file = open(pass_doc, 'r', encoding="utf-8", errors="ignore")
except FileNotFoundError:
    print(f"  [!] Error: {pass_doc} no ha sido encontrado")
    sys.exit(1)

for palabra in pass_file:
    palabra = palabra.strip()  # Elimina espacios y saltos de línea
    palabra_cifrada = palabra.encode('utf-8')
    palabra_hasheada = hashlib.md5(palabra_cifrada)  # No necesitas `.strip()` aquí
    digest = palabra_hasheada.hexdigest()

    if digest == input_hash:
        print(" [+] Contraseña encontrada!!!")
        print(f" [+] La contraseña es: {palabra}\n")
        encontrado = 1
        break

pass_file.close()

if not encontrado:
    print(" [!] Contraseña no encontrada en el diccionario...")


