import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import traceback

# Paso 1: Autenticación con Google
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'credenciales_google.json',
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file"
    ]
)
client = gspread.authorize(creds)

try:
    # Paso 2: Carga las hojas
    sheet = client.open_by_key("1i9cSM-2xVozOcVc72FJPglaJg-sevNItZ5ARNSFNNU8").worksheet("Seguimiento Alumnas")
    print("✅ Acceso exitoso a Google Sheets!")

    # Paso 3: Lee CSVs
    df_mensajes = pd.read_csv("datos_whatsapp.csv")
    df_datos = pd.read_csv("seguimiento_alumnas.csv")

    # Limpieza de columnas
    df_mensajes.columns = df_mensajes.columns.str.strip()
    df_datos.columns = df_datos.columns.str.strip()

    # Paso 4: Agrupa mensajes por alumna
    conversaciones = df_mensajes.groupby("remitente").apply(
        lambda x: "\n".join(f"{row['fecha']} - {row['remitente']}: {row['mensaje']}" for _, row in x.iterrows())
    ).reset_index().rename(columns={0: "Conversación", "remitente": "Nombre"})

    # Paso 5: Une con los datos de seguimiento
    df_final = pd.merge(df_datos, conversaciones, on="Nombre", how="left")

    # Paso 6: Selecciona y ordena columnas
    columnas_finales = [
        "Nombre", "Equipo", "Estado Emocional", "Estado reto",
        "Interacción en Grupo", "Problemas/Dudas Importantes",
        "Comentarios alumna", "Comentarios Tutora",
        "Observaciones", "Conversación"
    ]
    df_final = df_final[columnas_finales]

    # Paso 7: Exporta a Google Sheets
    data = [df_final.columns.tolist()] + df_final.values.tolist()
    sheet.clear()
    sheet.update(values=data, range_name='A1')

    print("📤 Conversaciones exportadas con éxito a Google Sheets!")

except Exception as e:
    print("❌ Error durante la exportación:")
    traceback.print_exc()
