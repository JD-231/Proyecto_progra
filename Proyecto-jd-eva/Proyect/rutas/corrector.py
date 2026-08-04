from flask import request, jsonify
from app import app
import modelos.corrector
from database.conexion import historial

@app.route("/api/corrector", methods=["POST"])
def corrector():

    texto = request.json["texto"]

    respuesta = modelos.corrector.corrector(texto)
    
    historial.insert_one({

        "modulo": "Correción",

        "entrada": texto,

        "salida": respuesta

    })

    return jsonify({
        "resultado": respuesta
    })