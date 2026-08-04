from transformers import pipeline

qa = pipeline(
"question-answering",
model="deepset/roberta-base-squad2"
)   


def preguntas_respuestas(texto):
    pregunta = ""
    texxto = ""
    
    if "/pregunta" in texto:
        for i in texto[texto.index("/pregunta")+1:]:
            pregunta += i 
        for i in texto[:texto.index("/pregunta")]:
            texxto += i
        
        resultado = qa(
        question=pregunta,
        context=texxto)

        return resultado["answer"]
    else:
        return "Comando mal ejecutado"


