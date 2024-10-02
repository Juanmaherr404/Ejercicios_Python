import sys

text = sys.argv[1]

text = text.upper()

correcto = "AUGC"

resultado = ""

for i in text:
    if i not in correcto:
        print("El mensaje no es válido.")
        sys.exit(1)  
    else:
        if i == "A":
            resultado += "A"
        elif i == "U":
            resultado += "T"
        elif i == "G":
            resultado += "G"
        elif i == "C":
            resultado += "C"

print(resultado)

