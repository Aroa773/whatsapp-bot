import json
print(json.dumps({"test": "success"}))  # Esto debería imprimir {"test": "success"}

import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Configurar credenciales de Google desde una variable de entorno
GOOGLE_CREDS_JSON = os.getenv("GOOGLE_CREDS_JSON")

# Comprobar que la variable existe
if not GOOGLE_CREDS_JSON:
    raise ValueError("La variable de entorno GOOGLE_CREDS_JSON no está definida.")

# Crear cliente de Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = Credentials.from_service_account_info(json.loads(GOOGLE_CREDS_JSON), scopes=SCOPES)
client = gspread.authorize(creds)

# ID del spreadsheet (lo puedes definir como variable de entorno si prefieres)
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")  # por ejemplo: '1aBcD...xyz'

if not SPREADSHEET_ID:
    raise ValueError("La variable de entorno SPREADSHEET_ID no está definida.")

def guardar_en_sheets(remitente, mensaje):
    sheet = client.open_by_key(SPREADSHEET_ID).sheet1
    sheet.append_row([remitente, mensaje])

@app.route("/webhook", methods=["POST"])
def webhook():
    # Obtener mensaje de WhatsApp
    mensaje = request.form.get("Body")
    remitente = request.form.get("From")

    # Guardar en Google Sheets
    guardar_en_sheets(remitente, mensaje)

    # Responder al usuario
    respuesta = MessagingResponse()
    respuesta.message("¡Gracias por tu mensaje! 😊")
    return str(respuesta)

# Escuchar en el puerto definido por Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)




 
