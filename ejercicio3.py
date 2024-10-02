chars = "┌┐ ┘└|─"
#Este programa dibujará cajas en la terminal dado el ancho y alto de los mismos
#Ejemplo con ancho 3 y alto 6 tendríamos: 
# 123
#┌───┐
#│   │1
#│   │2
#│   │3
#│   │4
#│   │5
#│   │6
#└───┘


print("---Ejercicio rectangulo---")

simodoble = input("¿lo quieres doble o simple?")
simodoble = simodoble.lower()
altura = input("¿Cual es la altura que quieres que tenga tu rectangulo? ")
anchura = input("¿Cual es la anchura que quieres que tenga tu rectangulo? ")
if not altura.isdigit() or not anchura.isdigit():
    print("No has introducido un valor válido")
    exit()
if simodoble == "simple":
    for i in range(1):
        print("•"+"──"* int(anchura)+"•")
    for i in range(int(altura)):
        print("│"+" "*(int(anchura))+"│")
    for i in range(1):
        print("•"+"──"* int(anchura)+"•")
elif simodoble == "doble":
    for i in range(1):
        print("╔"+"══"* int(anchura)+"╗")
    for i in range(int(altura)):
        print("║"+" "*(int(anchura))+"║")
    for i in range(1):
        print("╚"+"══"* int(anchura)+"╝")
else:
    print("No has introducido un valor válido")
    exit()

