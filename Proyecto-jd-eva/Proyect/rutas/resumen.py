from flask import request, jsonify
from app import app
import modelos.resumen
from database.conexion import historial

@app.route("/resumen", methods=["POST"])
def resumir():

    texto = request.json["texto"]

    respuesta = modelos.resumen.resumir(texto)

    historial.insert_one({

        "modulo": "Resumen",

        "entrada": texto,

        "salida": respuesta

    })

    return jsonify({
        "resultado": respuesta
    })