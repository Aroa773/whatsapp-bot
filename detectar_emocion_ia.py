from transformers import pipeline

# Cargar el modelo de emociones (puede tardar un poquito la primera vez)
clasificador = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-emotion")

def detectar_emocion(texto):
    resultado = clasificador(texto[:512])  # Limita a 512 caracteres
    return resultado[0]['label']

