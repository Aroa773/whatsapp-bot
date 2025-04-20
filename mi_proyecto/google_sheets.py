# -*- coding: utf-8 -*-
import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Cargar las credenciales de la cuenta de servicio (JSON)
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = '/Users/aroaagustinosoto/Documents/proyecto_whatsapp/credenciales_google.json'  # Asegúrate de poner la ruta correcta a tu archivo JSON

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Conexión con la API de Google Sheets
service = build('sheets', 'v4', credentials=creds)

# ID de la hoja de cálculo y nombre de la hoja que quieres modificar
SPREADSHEET_ID = '1i9cSM-2xVozOcVc72FJPglaJg-sevNItZ5ARNSFNNU8'
RANGE_NAME = 'Hoja1!A1:Z100'

# Lee datos de Google Sheets
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
values = result.get('values', [])

# Procesa los datos con pandas
df = pd.DataFrame(values)
print(df)
