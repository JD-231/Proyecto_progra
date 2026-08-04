from flask import request, jsonify
from app import app
import modelos.idioma
from database.conexion import historial

@app.route("/api/idioma", methods=["POST"])
def idioma():

    texto = request.json["texto"]

    respuesta = modelos.idioma.idioma(texto)
    
    historial.insert_one({

        "modulo": "traducción",

        "entrada": texto,

        "salida": respuesta

    })

    return jsonify({
        "resultado": respuesta
    })