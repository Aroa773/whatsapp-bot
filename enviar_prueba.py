#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

# Webhook de Zapier
url = "https://hooks.zapier.com/hooks/catch/19363068/205d8yx/"

# Datos de prueba que se enviarán
payload = {
    "nombre": "Eva Egea",
    "equipo": "AITED Dream Team",
    "estado": "motivada"
}

# Enviar los datos a Zapier
response = requests.post(url, json=payload)

# Mostrar la respuesta en la terminal
print("Código de respuesta:", response.status_code)
print("Respuesta:", response.text)


