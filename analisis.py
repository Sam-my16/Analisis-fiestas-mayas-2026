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

carpeta = r'C:\Users\Nt\Desktop\Carrera\Laboratorio de Datos\Analisis-fiestas-mayas-2026\\'
#%%

df = pd.read_csv(carpeta +'fiestas_mayas_2026.csv')
print("Filas descargadas:", len(df))
print("\nPrimeras 3 filas:")
print(df.head(3))
print("\nColumnas:", df.columns.tolist())

#%%
consulta = '''SELECT DISTINCT "Categoría" AS "Categorías"
              FROM df
              ORDER BY "Categoría"
              '''

categorias = duckdb.sql(consulta).df
print(categorias)

#Hay categoría NULL, quizás personas no binarias?
df["Categoría"] = df["Categoría"].fillna("Sin categoría")

consulta_nb = """SELECT *
                FROM df
                WHERE "Categoría" = 'Sin categoría'
                ORDER BY "Posicion"
                """

nb = duckdb.sql(consulta_nb).df()
print(nb)

#%%

consulta_hombres = """SElECT *
                        FROM df
                        WHERE "Categoría" LIKE 'Male%'
                        ORDER BY "Posicion"
                               """

hombres = duckdb.sql(consulta_hombres).df()
print(hombres)

consulta_edad_hombres = """SELECT 
    REPLACE("Categoría", 'Male ', '') AS rango_edad,
    COUNT(*) as total,
    epoch(AVG(CAST("Tiempo neto" AS INTERVAL))) AS promedio_segundos
    FROM hombres
    GROUP BY rango_edad
    ORDER BY total DESC"""

edades_hombres = duckdb.sql(consulta_edad_hombres).df()
edades_hombres['minutos'] = edades_hombres['promedio_segundos'] / 60
print(edades_hombres)

edades_hombres.plot( 'minutos','rango_edad', kind='bar')
plt.axhline(y=46.17, xmin=0, xmax=1, color = 'r')
plt.show()




#%%