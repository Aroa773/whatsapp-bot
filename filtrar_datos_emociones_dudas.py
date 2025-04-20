from transformers import pipeline
import pandas as pd

# Leer el archivo de datos procesados
df = pd.read_csv('datos_procesados.csv')

# Cargar el modelo de análisis de sentimientos (Sentiment Analysis)
sentiment_analyzer = pipeline("sentiment-analysis")

# Función para detectar la emoción en los mensajes
def detectar_emocion(texto):
    resultado = sentiment_analyzer(texto)
    return resultado[0]['label']  # Positivo, Negativo, Neutro

# Función para detectar dudas en los mensajes
def detectar_duda(texto):
    palabras_clave = ['duda', 'incertidumbre', 'no sé', 'pregunta']
    for palabra in palabras_clave:
        if palabra in texto.lower():
            return 'Duda'
    return 'No Duda'

# Aplicar la detección de emociones a la columna 'Mensaje'
df['Emoción Detectada'] = df['Mensaje'].apply(detectar_emocion)

# Aplicar la detección de dudas
df['Duda Detectada'] = df['Mensaje'].apply(detectar_duda)

# Guardar los resultados filtrados en un nuevo archivo CSV
df.to_csv('datos_emociones_dudas.csv', index=False)

print("Detección de emociones y dudas completada. Los datos se guardaron en 'datos_emociones_dudas.csv'.")
