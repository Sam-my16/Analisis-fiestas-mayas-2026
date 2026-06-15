import pandas as pd
import duckdb
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

plt.rc('figure', dpi=100)
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams.update({
    'font.size': 16,
    'font.family': 'monospace',
    'font.monospace': ['Courier New']
})

nombre = 'fiestas_mayas_2026.csv'
carpeta = r'C:\Users\Nt\Desktop\Carrera\Laboratorio de Datos\Analisis-fiestas-mayas-2026\\'

df = pd.read_csv(carpeta + nombre)
print("Filas descargadas:", len(df))
print("\nPrimeras 3 filas:")
print(df.head(3))
print("\nColumnas:", df.columns.tolist())

# Rellenamos categoría NULL
df["Categoría"] = df["Categoría"].fillna("Sin categoría")

# --- Hombres ---
consulta_hombres = """
    SELECT *,
           REPLACE("Categoría", 'Male ', '') AS rango_edad
    FROM df
    WHERE "Categoría" LIKE 'Male%'
    ORDER BY "Posicion"
"""
hombres = duckdb.sql(consulta_hombres).df()

tiempos = hombres['Tiempo bruto'].str.split(':', expand=True).astype(float)
hombres['Tiempo'] = (tiempos[0] * 60) + tiempos[1] + (tiempos[2] / 60)
hombres = hombres.drop(columns=['Tiempo bruto', 'Tiempo neto'])
hombres = hombres.sort_values(by='rango_edad').reset_index(drop=True)

# --- Mujeres ---
consulta_mujeres = """
    SELECT *,
           REPLACE("Categoría", 'Female ', '') AS rango_edad
    FROM df
    WHERE "Categoría" LIKE 'Female%'
    ORDER BY "Posicion"
"""
mujeres = duckdb.sql(consulta_mujeres).df()

tiempos_mujeres = mujeres['Tiempo bruto'].str.split(':', expand=True).astype(float)
mujeres['Tiempo'] = (tiempos_mujeres[0] * 60) + tiempos_mujeres[1] + (tiempos_mujeres[2] / 60)
mujeres = mujeres.drop(columns=['Tiempo bruto', 'Tiempo neto'])

# --- Ritmos ---
distancia = 10
hombres['ritmos'] = hombres['Tiempo'] / distancia
mujeres['ritmos'] = mujeres['Tiempo'] / distancia  # CORRECCIÓN: era ['Tiempo'] en vez de mujeres['Tiempo']
