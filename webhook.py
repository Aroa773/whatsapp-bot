import os
import json
from flask import Flask, request
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Cargar las credenciales de Google desde la variable de entorno
google_creds = json.loads(os.getenv("GOOGLE_CREDS_JSON"))

# Configuración de Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '16ZMWnRrzvD_RCN3xSEp4RCDD7f6m3bfu3nNW4-UA-uc'  # Reemplaza esto con tu ID de hoja de cálculo

# Función para guardar en Google Sheets
def guardar_en_sheets(remitente, mensaje):
    creds = Credentials.from_service_account_info(google_creds, scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SPREADSHEET_ID).sheet1
    sheet.append_row([remitente, mensaje])

# Webhook para recibir mensajes de Twilio
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.form
    mensaje = data.get('Body')
    remitente = data.get('From')
    
    if mensaje and remitente:
        # Guardar mensaje en Google Sheets
        guardar_en_sheets(remitente, mensaje)
        return "Mensaje recibido y guardado", 200
    else:
        return "Datos incompletos", 400

if __name__ == "__main__":
    # Escuchar en 0.0.0.0 y usar el puerto proporcionado por Render
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))



 
