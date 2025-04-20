import pandas as pd

# 1. Carga el CSV con los mensajes ya extraídos
df = pd.read_csv("/Users/aroaagustinosoto/Documents/proyecto_whatsapp/datos_whatsapp.csv", delimiter=",")

# Verifica las columnas del DataFrame
print("'fecha', 'remitente', 'mensaje'", df.columns)
print(df.columns)


# Verifica las primeras filas para ver el contenido
print("Primeras filas del archivo:")
print(df.head())

# 2. Lista de alumnas (puedes personalizarla luego)
alumnas = df["remitente"].unique()

# 3. Crea una lista para guardar los resultados por alumna
resumen = []

# 4. Funciones básicas de análisis (muy iniciales, luego las mejoramos con IA)
def detectar_emocion(textos):
    emociones = ["agobiada", "contenta", "perdida", "motivada", "estresada", "ilusionada"]
    for e in emociones:
        for t in textos:
            if e in t.lower():
                return e
    return "neutral"

def detectar_dudas(textos):
    dudas = [t for t in textos if isinstance(t, str) and ("no entiendo" in t.lower() or "tengo una duda" in t.lower())]
    return dudas

# 5. Recorre cada alumna para hacer su resumen
for alumna in alumnas:
    mensajes = df[df["remitente"] == alumna]["mensaje"].dropna().astype(str).tolist()


    entrada = {
        "Nombre": alumna,
        "Equipo": "",  # Esto puedes rellenarlo tú manualmente
        "Estado Emocional": detectar_emocion(mensajes),
        "Estado reto": "",  # A completar según contenido o avance
        "Interacción en Grupo": f"{len(mensajes)} mensajes",
        "Problemas/Dudas Importantes": detectar_dudas(mensajes),
        "Comentarios alumna": " | ".join(mensajes[-3:]),  # Últimos 3 mensajes
        "Comentarios Tutora": "",
        "Observaciones": ""
    }

    resumen.append(entrada)

# 6. Convertimos a DataFrame y exportamos a nuevo CSV
df_resumen = pd.DataFrame(resumen)
df_resumen.to_csv("seguimiento_alumnas.csv", index=False)

print("✅ Archivo 'seguimiento_alumnas.csv' generado con éxito.")
