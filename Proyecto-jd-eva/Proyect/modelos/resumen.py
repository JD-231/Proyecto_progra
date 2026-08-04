from transformers import pipeline

summarizer = pipeline(
"summarization",
model="facebook/bart-large-cnn",
framework="pt")


def resumir(texto):
    tamaño_texto = len(texto.split())
    if tamaño_texto>=30:
        max = int(tamaño_texto)
        min = int(tamaño_texto*0.75)   
        resumen = summarizer(
        texto,
        max_length=max,
        min_length=min,
        do_sample=False
)       

        # print("\n=== RESUMEN ===")
        return(resumen[0]["summary_text"])
    else:
        return "El texto es muy pequeño"
    
