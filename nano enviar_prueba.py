import requests

url = 'https://hooks.zapier.com/hooks/catch/19363068/205d8yx/'  # tu webhook de Zapier

datos = {
    "mensaje": "Hola, esto es una prueba",
    "alumna": "Laura",
    "estado": "Motivada"
}

response = requests.post(url, json=datos)
print("Respuesta de Zapier:", response.status_code)
