import subprocess
import sys

#Cogemos las ip y las peticiones
ip = sys.argv[1]
peticiones = sys.argv[2]

#Ponemos el comando para hacer peticiones 
resultado = subprocess.run(["ping", "-i", "0.1", "-s", "1000", "-c", peticiones, ip], capture_output=True, text=True)

#Imprime resultado
print(resultado.stdout)
print(resultado.stderr)

