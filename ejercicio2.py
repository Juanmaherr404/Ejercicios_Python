text = input("Ingresa Mensaje: ")
text = text.lower()

resultado = text.replace("s", "2").replace("o", "0").replace("i", "1").replace("e", "3").replace("a", "4").replace("s", "5").replace("g", "6").replace("t", "7").replace("b", "8").replace("g", "9").upper()

print("El mensaje alterado es: ", resultado)