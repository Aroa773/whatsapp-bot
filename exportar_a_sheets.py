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
    # Paso 2: Abre la hoja de cálculo por su key
    sheet = client.open_by_key("1i9cSM-2xVozOcVc72FJPglaJg-sevNItZ5ARNSFNNU8").worksheet("Seguimiento Alumnas")
    print("✅ Acceso exitoso a Google Sheets!")

    # Paso 3: Lee el archivo CSV
    df = pd.read_csv("datos_whatsapp.csv", delimiter=",")
    df.columns = df.columns.str.replace('"', '').str.replace("'", "").str.strip()

    # Paso 4: Limpia y convierte a lista de listas (incluyendo encabezados)
    data = [df.columns.tolist()] + df.values.tolist()

    # Paso 5: Borra el contenido actual de la hoja y escribe los nuevos datos
    sheet.clear()
    sheet.update('A1', data)

    print("📤 Exportación exitosa a Google Sheets!")

except Exception as e:
    print("❌ Error durante la exportación:")
    traceback.print_exc()
