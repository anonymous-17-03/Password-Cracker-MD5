import hashlib, signal, sys

def handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)
# Ctrl + C
signal.signal(signal.SIGINT, handler)

banner = '''

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
input_hash = input("\n [*] Inserte la contraña hasheada: ")
pass_doc = input(" [*] Inserte el diccionario: ")

try:
    pass_file = open(pass_doc, 'r')
except:
    print("  [!] Error:" + pass_doc + " no a sido encontrado")

for palabra in pass_file:
    palabra_cifrada = palabra.encode('utf-8')
    palabra_hasheada = hashlib.md5(palabra_cifrada.strip())
    digest = palabra_hasheada.hexdigest()

    if digest == input_hash:
        print(" [+] Contraseña encontrada!!!")
        print(" [+] La contraseña es: " + palabra)
        encontrado = 1
        break

if not encontrado:
    print(" [!] Contraseña no encontrada en el diccinario...")
