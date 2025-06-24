from flask import Flask, request, jsonify
from recommender import recomendar_libros
from graph_generator import generar_grafo

app = Flask(__name__)

@app.route("/recomendar", methods=["POST"])
def recomendar():
    data = request.get_json()
    libro = data.get("libro")
    reglas = recomendar_libros(libro)
    grafo = generar_grafo(reglas, libro)
    return jsonify({
        "recomendaciones": reglas,
        "grafo": grafo  # imagen en base64
    })

if __name__ == "__main__":
    app.run()
