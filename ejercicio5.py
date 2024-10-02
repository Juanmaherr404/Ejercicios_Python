import requests
import sys

url = sys.argv[1]
#Creamos un bucle para que se ejecute hasta que se produzca un error
while True:
    #mientras no se produzca un error, se ejecuta el bucle
    try:
        respuesta = requests.get(url)
        print(respuesta.text)
    except requests.exceptions.RequestException:
        print("Error")
        break

