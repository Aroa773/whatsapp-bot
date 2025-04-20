# Definir las funciones
def detectar_emocion(textos):
    # Función para detectar emoción (el código que ya tienes)
    ...

def detectar_dudas(textos):
    # Función para detectar dudas (el código que ya tienes)
    ...

# Aquí definimos las variables necesarias, como la lista de alumnas y los mensajes
alumnas = ['Alumna 1', 'Alumna 2', 'Alumna 3']
df = pd.DataFrame({
    'Remitente': ['Alumna 1', 'Alumna 2', 'Alumna 1'],
    'Mensaje': ['Estoy agobiada con el proyecto.', 'No entiendo el ejercicio.', 'Tengo una duda sobre el tema.']
})

# Aquí va el código para generar el resumen de cada alumna y el DataFrame
resumenes = []

for alumna in alumnas:
    mensajes = df[df["Remitente"] == alumna]["Mensaje"].dropna().astype(str).tolist()

    entrada = {
        "Nombre": alumna,
        "Equipo": "",  # Rellenar manualmente si es necesario
        "Estado Emocional": detectar_emocion(mensajes),
        "Dudas Detectadas": detectar_dudas(mensajes),
        "Interacción en Grupo": "",  # Rellenar si tienes la lógica
        "Problemas/Dudas Importantes": "",
        "Comentarios alumna": "",
        "Comentarios Tutora": "",
        "Observaciones": "",
    }

    resumenes.append(entrada)

df_resumen = pd.DataFrame(resumenes)
print(df_resumen)

# Guardar en CSV o Excel si lo deseas
df_resumen.to_csv('resumenes_alumnas.csv', index=False)
