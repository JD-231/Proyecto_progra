from flask import request, jsonify
from app import app
import modelos.sentimientos
from database.conexion import historial

@app.route("/api/emociones", methods=["POST"])
def setimientos():

    texto = request.json["texto"]

    respuesta = modelos.sentimientos.sentimientos(texto)
    
    historial.insert_one({

        "modulo": "sentimientos",

        "entrada": texto,

        "salida": respuesta

    })

    return jsonify({
        "resultado": respuesta
    })