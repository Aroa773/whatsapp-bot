import pandas as pd

# Cargar mensajes desde el CSV
df = pd.read_csv("datos_whatsapp.csv")

# Alumnas únicas
alumnas = df["Nombre"].unique()

resumen = []

# Funciones de análisis
def detectar_emocion(textos):
    emociones = ["agobiada", "contenta", "perdida", "motivada", "estresada", "ilusionada"]
    for e in emociones:
        for t in textos:
            if e in t.lower():
                return e
    return "neutral"

def detectar_dudas(textos):
    dudas = [t for t in textos if "no entiendo" in t.lower() or "tengo una duda" in t.lower()]
    return "Sí" if dudas else "No"

# Recorrer cada alumna
for alumna in alumnas:
    mensajes = df[df["Nombre"] == alumna]["Mensaje"].tolist()

    entrada = {
        "Nombre": alumna,
        "Equipo": "",  # Lo puedes rellenar después
        "Estado Emocional": detectar_emocion(mensajes),
        "Estado reto": "",
        "Interacción en Grupo": f"{len(mensajes)} mensajes",
        "Problemas/Dudas Importantes": detectar_dudas(mensajes),
        "Comentarios alumna": " | ".join(mensajes[-3:]),
        "Comentarios Tutora": "",
        "Observaciones": ""
    }

    resumen.append(entrada)

# Guardar resultados
df_resumen = pd.DataFrame(resumen)
df_resumen.to_csv("seguimiento_alumnas.csv", index=False)

print("✅ Archivo 'seguimiento_alumnas.csv' generado con éxito.")
from subir_a_sheets import subir_datos_a_sheets

df_resultado = pd.read_csv("seguimiento_alumnas.csv")
spreadsheet_id = "1i9cSM-2xVozOcVc72FJPglaJg-sevNItZ5ARNSFNNU8"  # 👈 Sustituye esto con el ID real de la hoja
subir_datos_a_sheets(df_resultado, spreadsheet_id)


