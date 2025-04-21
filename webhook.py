import os
import gspread
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from flask import Flask, request

app = Flask(__name__)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '16ZMWnRrzvD_RCN3xSEp4RCDD7f6m3bfu3nNW4-UA-uc'  # 🔁 Reemplaza esto

# Lee las credenciales desde la variable de entorno
GOOGLE_CREDS_JSON = os.getenv('GOOGLE_CREDS_JSON')

# Función para guardar en Google Sheets
def guardar_en_sheets(remitente, mensaje):
    creds = Credentials.from_service_account_info(
        json.loads(GOOGLE_CREDS_JSON), scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SPREADSHEET_ID).sheet1
    sheet.append_row([remitente, mensaje])

# Webhook para recibir mensajes de Twilio
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.form
    mensaje = data.get('Body')
    remitente = data.get('From')
    guardar_en_sheets(remitente, mensaje)
    return "Mensaje recibido", 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))




 
