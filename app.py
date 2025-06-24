from flask import Flask, request, jsonify
from recommender import recomendar_libros
from graph_generator import generar_grafo
import pandas as pd
app = Flask(__name__)

# Carga las reglas ya calculadas
rules = pd.read_pickle('modelos/rules.pkl.gz')

@app.route("/recomendar", methods=["POST"])
def recomendar():
    data = request.get_json()
    libros = data.get("libros")
    if not libros:
        return jsonify({"error": "Se requiere una lista de libros"}), 400

    reglas = recomendar_libros(libros, rules)
    grafo = generar_grafo(reglas, libros)
    
    # Extraer solo los consequents para enviar como recomendaciones simples
    recomendaciones = []
    for r in reglas:
        for libro_rec in r['consequents']:
            if libro_rec not in libros and libro_rec not in recomendaciones:
                recomendaciones.append(libro_rec)

    return jsonify({
        "recomendaciones": recomendaciones,
        "grafo": grafo
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200  

 