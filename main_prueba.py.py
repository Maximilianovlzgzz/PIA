import logging
import argparse
from metadatapdf import printMeta
from python_powershellhash import valor_hash
import subprocess
from envio_prueba import enviar_correos
from puertos import *
parser = argparse.ArgumentParser()
from web_scraping import *
from uso_socket import socket_uso
try:
    from googlesearch import search 
except ImportError:
    os.system('pip install requeriments.txt')
    exit()
# opc: opciones
parser.add_argument("-opc", type=int,
help = """-opc (1=Extraer y enviar informacion, 2=nmap,
           3=web scraping)""")
# Si quieres codificar/decodificar/hackear un mensaje,
# tienes que escoger entre cifrado cesar o de transposicion
parser.add_argument("-tipo_archivo", type=int, help="-tipo_archivo (1=Pdf)")
#Metadatospdf: 
parser.add_argument("-ruta_metadatos", type=str, help='-ruta_metadatos "pon la ruta completa en donde quieres sacar los metadatos del pdf"')
#Aqui empieza lo del envio de correo
parser.add_argument("-remitente", type=str, help='-remitente "pon el correo al que quieres enviar"')
# Si quieres saber que puertos estan abiertos
parser.add_argument("-url_socket", type=str, help='-url_socket "escribe el dominio al cual quieres sacar su ip"')
parser.add_argument("-ip", type=str, help='-ip "IP a escanear"')
parser.add_argument("-i", type=int, help='-i "Inicio de los puertos a escanear"')
parser.add_argument("-f", type=int, help='-f "Final de los puertos a escanear"')
parser.add_argument("-url", type=str, help='-url "Escribe la url para hacer el web scraping"')
data = parser.parse_args()

if __name__ == '__main__':
    #elige la opcion 1 que es extraer y enviar info
    if(data.opc == 1):
         #despues escoge si quiere analizar pdf o imagen
         if(data.tipo_archivo == 1 or data.tipo_archivo == 2):
         # Pdf
             if data.tipo_archivo == 1:
             	printMeta(data.ruta_metadatos)
             	valor_hash()
             	enviar_correos(data.remitente)
    #Aqui ejecutamos nmap
    if(data.opc == 2):
         nmap_funcion(data.ip, data.i, data.f)
         socket_uso(data.url_socket)
    if(data.opc == 3):
         web(data.url)            