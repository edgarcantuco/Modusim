import os
import sys
cwd = os.getcwd()

for folder in os.listdir(cwd + '\Modulos'):
    for file in os.listdir(cwd + '\Modulos\ '[:-1] + folder):
        if file.endswith(".py"):
            try:
                bloque = __import__('Modulos.' + folder + '.' + file.replace(".py", ""), fromlist=["Main"])
            except:
                print("No se pudo importar el módulo")