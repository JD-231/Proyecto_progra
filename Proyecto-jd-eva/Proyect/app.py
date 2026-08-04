from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/resumen")
def pagina_resumen():
    return render_template("resumen.html")

@app.route("/corrector")
def pagina_corrector():
    return render_template("correccion.html")

@app.route("/emociones")
def pagina_emociones():
    return render_template("emociones.html")

@app.route("/idioma")
def pagina_idioma():
    return render_template("traduccion.html")

@app.route("/preguntas")
def pagina_preguntas():
    return render_template("preguntas.html")

from rutas.resumen import *
from rutas.corrector import *
from rutas.sentimientos import *
from rutas.idioma import *
from rutas.preguntas import *

if __name__ == "__main__":
    app.run(debug=True)