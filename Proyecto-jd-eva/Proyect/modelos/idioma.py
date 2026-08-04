from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

modelo = "facebook/nllb-200-distilled-600M"

tokenizer = AutoTokenizer.from_pretrained(modelo)
model = AutoModelForSeq2SeqLM.from_pretrained(modelo)

detector = pipeline(
    "text-classification",
    model="papluca/xlm-roberta-base-language-detection"
)

idiomas = {
    "es": "spa_Latn",
    "en": "eng_Latn",
    "fr": "fra_Latn",
    "de": "deu_Latn",
    "it": "ita_Latn",
    "pt": "por_Latn",
    "nl": "nld_Latn",
    "pl": "pol_Latn",
    "ru": "rus_Cyrl",
    "ja": "jpn_Jpan",
    "zh": "zho_Hans",
    "ar": "arb_Arab",
    "hi": "hin_Deva",
    "tr": "tur_Latn",
    "th": "tha_Thai",
    "vi": "vie_Latn",
    "sw": "swh_Latn",
    "ur": "urd_Arab",
    "el": "ell_Grek"
}

def idioma(texto):

    deteccion = detector(texto)[0]["label"]
    
    select = idiomas[deteccion]
    tokenizer.src_lang = select

    entradas = tokenizer(
        texto,
        return_tensors="pt"
    )

    salida = model.generate(
        **entradas,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids("spa_Latn"),
        max_new_tokens=100
    )

    traduccion = tokenizer.batch_decode(
        salida,
        skip_special_tokens=True
    )[0]

    respuesta1 = f"El idioma detectado es: '{deteccion}'."
    respuesta2 = f"\nLa traducción al español es: {traduccion}"
    return respuesta1,respuesta2