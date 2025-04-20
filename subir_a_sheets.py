import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

def subir_datos_a_sheets(df, spreadsheet_id, rango='Hoja1!A1'):
    """
    Sube un DataFrame a una hoja de cálculo de Google Sheets.

    Parámetros:
    - df: DataFrame de pandas con los datos.
    - spreadsheet_id: ID de la hoja de cálculo.
    - rango: Rango inicial (por defecto A1 en Hoja1).
    """
    creds = service_account.Credentials.from_service_account_file(
        'credenciales_google.json',
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )

    servicio = build('sheets', 'v4', credentials=creds)
    hoja = servicio.spreadsheets()

    valores = [df.columns.tolist()] + df.values.tolist()

    hoja.values().update(
        spreadsheetId=spreadsheet_id,
        range=rango,
        valueInputOption='RAW',
        body={'values': valores}
    ).execute()

    print("✅ Datos subidos correctamente a Google Sheets.")

