import gspread
from oauth2client.service_account import ServiceAccountCredentials

def subir_a_google_sheets(phone_number, message_body):
    # Definir el alcance
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Cargar credenciales desde el archivo JSON
    creds = ServiceAccountCredentials.from_json_keyfile_name("credenciales_google.json", scope)

    # Autorizar y conectar con Google Sheets
    client = gspread.authorize(creds)

    # Abrir el documento y seleccionar la hoja
    sheet = client.open("datos_whatsapp").Seguimiento Edición 9  # Asegúrate que este nombre coincide con tu archivo de Sheets

    # Agregar una nueva fila
    sheet.append_row([phone_number, message_body])


