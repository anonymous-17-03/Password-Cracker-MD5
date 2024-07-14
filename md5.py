import hashlib, signal, sys

def handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)
# Ctrl + C
signal.signal(signal.SIGINT, handler)

def hash_md5():
    input_palabra = input("\n [+] Inserte la palabra: ")
    palabra_cifrada = input_palabra.encode('utf-8')
    palabra_hasheada = hashlib.md5(palabra_cifrada.strip())
    digest = palabra_hasheada.hexdigest()
    print(" [+] Hash: " + digest + "\n")

hash_md5()
