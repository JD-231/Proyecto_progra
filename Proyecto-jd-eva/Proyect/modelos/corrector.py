from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import re
from spellchecker import SpellChecker

MODELO = "SkitCon/gec-spanish-BARTO-SYNTHETIC"

tokenizer = AutoTokenizer.from_pretrained(MODELO)
model = AutoModelForSeq2SeqLM.from_pretrained(MODELO)
spell = SpellChecker(language='es')



correcciones = {}

def corregir_ortografia(texto):
    def corregir_palabra(match):
        palabra = match.group(0)

        corregida = spell.correction(palabra.lower())

        if corregida and corregida != palabra.lower():
            correcciones[palabra] = corregida

            # Mantener mayúscula inicial
            if palabra[0].isupper():
                return corregida.capitalize()

            return corregida

        return palabra

    return re.sub(r'[A-Za-zÁÉÍÓÚáéíóúÑñÜü]+', corregir_palabra, texto)


def corregir_gramatica(oracion):
    inputs = tokenizer(
        oracion,
        return_tensors="pt",
        truncation=True,
        max_length=128
    )

    outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_new_tokens=128
    )

    return tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )


def corrector(texto):   
    texto_corregido = corregir_ortografia(texto)
    oraciones = texto_corregido.split("\n")

    respuesta = ""
    for oracion in oraciones:
        if oracion.strip():
            respuesta += corregir_gramatica(oracion)+"\n"
    return respuesta

