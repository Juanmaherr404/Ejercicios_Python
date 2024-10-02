import requests
import sys

# Verificar si se ha pasado un argumento (URL)
if len(sys.argv) == 2:
    url = sys.argv[1]  # Si el usuario pasa una URL
else:
    url = 'https://jsonplaceholder.typicode.com/users'  # URL por defecto

#Hace la peticion
peticion = requests.get(url)

#PIde el archivo en formato json
usuarios = peticion.json()

#creamos una lista para guardar los nombres
lista_nombres = []

#Bucle para recoger los usuarios de json y guardarlos en lista
for usuario in usuarios:
        nombre = usuario['name']
        lista_nombres.append(nombre)
        print(nombre)

#Abrir un archivo con permiso de escritura
with open('nombres_usuarios.txt', 'w') as file:
    #Bucle para recorrer la lista y escribir los nombres en el archivo
    for nombre in lista_nombres:
        file.write(nombre + '\n')


