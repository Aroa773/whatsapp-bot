import pandas as pd
from datetime import datetime

# Leer el archivo CSV con los datos procesados
df = pd.read_csv("datos_procesados.csv")

# Ejemplo: Filtrar por emoción (Positiva, Negativa, Neutra)
df_filtrado_emocion = df[df['Emoción'] == 'Positiva']

# Ejemplo: Filtrar por equipo (Equipo A o Equipo B)
df_filtrado_equipo = df[df['Equipo'] == 'Equipo A']

# Ejemplo: Filtrar por edad (por ejemplo, mayores de 30 años)
df_filtrado_edad = df[df['Edad'] > 30]

# Guardar los datos filtrados en archivos CSV
df_filtrado_emocion.to_csv("datos_filtrados_emocion.csv", index=False)
df_filtrado_equipo.to_csv("datos_filtrados_equipo.csv", index=False)
df_filtrado_edad.to_csv("datos_filtrados_edad.csv", index=False)

# Imprimir mensaje de confirmación
print("Archivos filtrados generados.")
