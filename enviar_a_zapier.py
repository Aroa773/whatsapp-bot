# Recorrer la lista de alumnas y enviar sus datos a Zapier
for alumna in lista_de_alumnas:
    enviar_a_zapier(alumna)  # Llamamos a la función para enviar a Zapier
# enviar_a_zapier.py
# -*- coding: utf-8 -*-
import requests

def enviar_a_zapier(datos_alumna):
    url = "https://hooks.zapier.com/hooks/catch/19363068/205d8yx/"

    payload = {
        "nombre": datos_alumna.get("Nombre", ""),
        "equipo": datos_alumna.get("Equipo", ""),
        "estado_emocional": datos_alumna.get("Estado Emocional", ""),
        "estado_reto": datos_alumna.get("Estado reto", ""),
        "interaccion_grupo": datos_alumna.get("Interacción en Grupo", ""),
        "problemas_dudas": datos_alumna.get("Problemas/Dudas Importantes", ""),
        "comentarios_alumna": datos_alumna.get("Comentarios alumna", ""),
        "comentarios_tutora": datos_alumna.get("Comentarios Tutora", ""),
        "observaciones": datos_alumna.get("Observaciones", "")
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print(f"✅ Enviado correctamente: {payload['nombre']}")
    else:
        print(f"⚠️ Error al enviar {payload['nombre']}: {response.status_code} - {response.text}")

