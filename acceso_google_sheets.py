import gspread
from oauth2client.service_account import ServiceAccountCredentials
import traceback

# Usa el archivo de credenciales para autenticarte
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'credenciales_google.json',
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file"
    ]
)
client = gspread.authorize(creds)

# Intenta abrir tu hoja de Google Sheets
try:
    sheet = client.open_by_key("1i9cSM-2xVozOcVc72FJPglaJg-sevNItZ5ARNSFNNU8").worksheet("Seguimiento Alumnas")
    print("✅ Acceso exitoso a Google Sheets!")
except Exception as e:
    print("❌ Error al acceder a Google Sheets:")
    traceback.print_exc()



