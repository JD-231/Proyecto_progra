from flask import request, jsonify
from app import app
import modelos.preguntas
from database.conexion import historial

@app.route("/api/preguntas", methods=["POST"])
def preguntas():

    texto = request.json["texto"]

    respuesta = modelos.preguntas.preguntas_respuestas(texto)
    
    historial.insert_one({

        "modulo": "preguntas",

        "entrada": texto,

        "salida": respuesta

    })

    return jsonify({
        "resultado": respuesta
    })