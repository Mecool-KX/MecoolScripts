#!/usr/bin/python
# -*- coding: latin-1 -*-

import os, sys
import urllib
import fcntl, socket, struct
import time

# Script que tenemos que descargar y ejecutar

URL_SCRIPT="https://raw.githubusercontent.com/Mecool-KX/MecoolScripts/master/mecoolscripts.pyo?raw=true"
NOM_SCRIPT=os.path.dirname(os.path.realpath(__file__)) + "/mecoolscripts.pyo"

def main(argv):  

	if (len(argv) > 0 and argv[0].upper() == "INICIO") or not os.path.exists(NOM_SCRIPT):
		# Descargamos el script de inicio
		descarga_fichero(URL_SCRIPT, NOM_SCRIPT)
		
	# Ejecutamos el script y le pasamos los parámetros que hos hayan pasado
	os.system("python " + NOM_SCRIPT + " " + " ".join(argv)) # Pasamos los parámetros que se le hayan pasado al script

def descarga_fichero(url, fichero, silent=True):
	"""
		Función para descargar un fichero donde nos digan
	"""
	borrar_fichero(fichero)
	try:
		if not silent: 
			urllib.urlretrieve(url, fichero, reporthook)
		else: 
			urllib.urlretrieve(url, fichero)
	except:
		print ("Error al descargar: " + url); exit(1)

def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\t\r%d KB/s, %d/%d MB, %d%%" %
                    (speed, progress_size / (1024 * 1024), total_size / (1024 * 1024), percent))
    sys.stdout.flush()
	
def borrar_fichero(fichero):
	"""
		Borramos el fichero que nos pasen por parámetro
	"""
	# Borramos el fichero .zip si existiera en local
	if os.path.exists(fichero): os.remove(fichero)

# this runs when the script is called from the command line
if __name__ == '__main__':  
	main(sys.argv[1:])