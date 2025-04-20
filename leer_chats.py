import re
import pandas as pd

def leer_chat(path):
    with open(path, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    datos = []
    patron = r'^(\d{2}/\d{2}/\d{4}), (\d{2}:\d{2}) - (.*?): (.*)$'

    for linea in lineas:
        match = re.match(patron, linea)
        if match:
            fecha, hora, remitente, mensaje = match.groups()
            datos.append({
                'fecha': fecha,
                'hora': hora,
                'remitente': remitente,
                'mensaje': mensaje
            })

    return pd.DataFrame(datos)
