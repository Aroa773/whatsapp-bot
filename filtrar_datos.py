# Importar las librerías necesarias
import pandas as pd
from datetime import datetime, timedelta

# Leer el archivo CSV con los datos procesados
df = pd.read_csv("datos_procesados.csv")

# Convertir la columna 'Fecha' a formato datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Filtrar por la última semana (últimos 7 días)
hoy = datetime.today()  # Fecha de hoy
una_semana_atras = hoy - timedelta(days=7)  # Fecha de hace 7 días
df_filtrado_semana = df[df['Fecha'] >= una_semana_atras]  # Filtrar los datos de la última semana

# Filtrar por emoción específica (por ejemplo, 'Positiva')
df_filtrado_emocion = df[df['Emoción'] == 'Positiva']  # Filtrar los datos con emoción 'Positiva'

# Filtrar por equipo específico (por ejemplo, 'Equipo A')
df_filtrado_equipo = df[df['Equipo'] == 'Equipo A']  # Filtrar los datos del equipo 'Equipo A'

# Guardar los datos filtrados en archivos CSV
df_filtrado_semana.to_csv("datos_filtrados_semana.csv", index=False)  # Guardar los datos filtrados por semana
df_filtrado_emocion.to_csv("datos_filtrados_emocion.csv", index=False)  # Guardar los datos filtrados por emoción
df_filtrado_equipo.to_csv("datos_filtrados_equipo.csv", index=False)  # Guardar los datos filtrados por equipo

# Imprimir mensaje de confirmación
print("Archivos filtrados generados.")

