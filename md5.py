#!/usr/bin/env python3

import hashlib
import signal
import sys

banner = r"""
                 _  _
 |_| _. _|_ |\/|| \|_
 | |(_|_>| ||  ||_/ _)
           Anonymous17
"""
print(banner)

def handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)
# Ctrl + C
signal.signal(signal.SIGINT, handler)

def hash_md5():
    input_palabra = input(" [+] Inserte la palabra: ")
    palabra_cifrada = input_palabra.encode("utf-8")
    palabra_hasheada = hashlib.md5(palabra_cifrada.strip())
    digest = palabra_hasheada.hexdigest()
    print(" [+] Hash: " + digest + "\n")

hash_md5()
