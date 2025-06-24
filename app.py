from flask import Flask, request, jsonify
from recommender import recomendar_libros
from rules_loader import get_rules  # Importar el loader
from flask_cors import CORS 

app = Flask(__name__)
CORS(app, origins=["*"])  # <-- CORS seguro y explícito
@app.route("/recomendar", methods=["POST"])
def recomendar():
    data = request.get_json()
    libros = data.get("libros")

    if not libros or not isinstance(libros, list):
        return jsonify({"error": "Se requiere una lista de libros"}), 400

    rules = get_rules()
    reglas = recomendar_libros(libros, rules)

    recomendaciones = []
    for r in reglas:
        for libro_rec in r['consequents']:
            if libro_rec not in libros and libro_rec not in recomendaciones:
                recomendaciones.append(libro_rec)

    return jsonify({
        "recomendaciones": recomendaciones,
    })

if __name__ == "__main__":
    app.run()
