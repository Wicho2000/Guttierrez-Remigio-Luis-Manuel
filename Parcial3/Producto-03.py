from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "18a3c1a80f2d45b2be214e04ec926296"

@app.route('/')
def obtener_juegos():
    url = f"https://api.rawg.io/api/games?key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    juegos_filtrados = [
        {
            "nombre": juego["name"],
            "lanzamiento": juego["released"],
            "imagen": juego.get("background_image", "")  # Obtener la URL de la imagen
        }
        for juego in data.get("results", [])
    ]
    
    # Renderiza la página HTML con los juegos
    return render_template("index.html", juegos=juegos_filtrados)

if __name__ == '__main__':
    app.run(debug=True)
