from flask import Flask, request
import gspread
from google.oauth2.service_account import Credentials

# Inicializa Flask
app = Flask(__name__)

# Configuración Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '16ZMWnRrzvD_RCN3xSEp4RCDD7f6m3bfu3nNW4-UA-uc'  # 🔁 Reemplaza esto
CREDENTIALS_FILE = 'token.json'

# Función para guardar en Google Sheets
def guardar_en_sheets(remitente, mensaje):
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
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
    app.run(debug=True, port=5000)
