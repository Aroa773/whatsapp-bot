import os
import json
from flask import Flask, request
import gspread
from datetime import datetime
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Leer desde variables de entorno
GOOGLE_CREDENTIALS = os.environ['GOOGLE_CREDENTIALS']
SPREADSHEET_ID = os.environ['SPREADSHEET_ID']
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# Función para guardar en Google Sheets
def guardar_en_sheets(remitente, mensaje):
    creds_dict = json.loads(GOOGLE_CREDENTIALS)
    creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SPREADSHEET_ID).sheet1
    sheet.append_row([remitente, mensaje, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

# Webhook para recibir mensajes de Twilio
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.form
    mensaje = data.get('Body')
    remitente = data.get('From')
    guardar_en_sheets(remitente, mensaje)
    return "Mensaje recibido", 200

if __name__ == "__main__":
    # Escuchar en 0.0.0.0 y usar el puerto proporcionado por Render
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))


 
