from transformers import pipeline

clasificador = pipeline(
    "text-classification",
    model="pysentimiento/robertuito-emotion-analysis"
)

def sentimientos(texto):

    resultado = clasificador(texto)
    
    emociones = {
    "joy": "Alegría",
    "sadness": "Tristeza",
    "anger": "Ira",
    "fear": "Miedo",
    "surprise": "Sorpresa",
    "disgust": "Asco",
    "others": "Neutral",
    "neutral": "Neutral"
}
    sentimiento = emociones[resultado[0]["label"]]
    puntaje = resultado[0]["score"]*100

    return f"{sentimiento}\nScore: {puntaje:.2f}"