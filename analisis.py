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
#%%

df = pd.read_csv(carpeta + nombre)
print("Filas descargadas:", len(df))
print("\nPrimeras 3 filas:")
print(df.head(3))
print("\nColumnas:", df.columns.tolist())


#%% Obtenemos todas las categorías posibles
consulta = '''SELECT DISTINCT "Categoría" AS "Categorías"
              FROM df
              ORDER BY "Categoría"
              '''

categorias = duckdb.sql(consulta).df
print(categorias)
#%%
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
consulta_hombres = """
    SELECT *, 
           REPLACE("Categoría", 'Male ', '') AS rango_edad 
    FROM df
    WHERE "Categoría" LIKE 'Male%'
    ORDER BY "Posicion"
"""

hombres = duckdb.sql(consulta_hombres).df()

# %% Transformación de tiempo a minutos decimales
# Separamos el string 'HH:MM:SS' en columnas numéricas
tiempos = hombres['Tiempo bruto'].str.split(':', expand=True).astype(float)

# Multiplicamos horas por 60, sumamos minutos, y dividimos segundos por 60
hombres['Tiempo'] = (tiempos[0] * 60) + tiempos[1] + (tiempos[2] / 60)

hombres = hombres.drop(columns=['Tiempo bruto', 'Tiempo neto'])

hombres = hombres.sort_values(by='rango_edad').reset_index(drop=True)

print(hombres)

#%% Acá obtengo solo los rangos de edad, el numero de participantes y el tiempo promedio
consulta_t_edad = """SELECT 
    rango_edad, 
    COUNT(*) AS total,
    AVG(Tiempo) AS promedio
    FROM hombres
    GROUP BY rango_edad
    ORDER BY rango_edad"""

resumen = duckdb.sql(consulta_t_edad).df()
# 1. Obtenemos los minutos enteros
minutos = resumen['promedio'] // 1

# 2. Obtenemos los segundos (el resto decimal multiplicado por 60)
segundos = (resumen['promedio'] % 1) * 60

# 3. Creamos la nueva columna formateada como texto MM:SS (redondeando los segundos)
resumen['promedio_formateado'] = (
    minutos.astype(int).astype(str) + ":" + 
    segundos.round().astype(int).astype(str).str.zfill(2)
)

print(resumen)
#%%
plt.figure(figsize=(10, 6))

# Graficamos usando los valores numéricos reales (promedio)
plt.scatter(resumen['rango_edad'], resumen['promedio'], color='tab:pink', zorder=3)
plt.plot(resumen['rango_edad'], resumen['promedio'], color='tab:pink', alpha=0.5, linestyle='--')

plt.xlabel('Rango de edad (Hombres)')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Tiempo promedio (Minutos)')
plt.title('Distribución de tiempos promedio por rango de edad - Hombres')
plt.grid(True, linestyle=':', alpha=0.6)

plt.show()



#%%
consulta_mujeres = """
    SELECT *, 
           REPLACE("Categoría", 'Female ', '') AS rango_edad 
    FROM df
    WHERE "Categoría" LIKE 'Female%'
    ORDER BY "Posicion"
"""

mujeres = duckdb.sql(consulta_mujeres).df()

# %% 2. Transformación de tiempo a minutos decimales
tiempos_mujeres = mujeres['Tiempo bruto'].str.split(':', expand=True).astype(float)

# HH*60 + MM + SS/60
mujeres['Tiempo'] = (tiempos_mujeres[0] * 60) + tiempos_mujeres[1] + (tiempos_mujeres[2] / 60)
mujeres = mujeres.drop(columns=['Tiempo bruto', 'Tiempo neto'])

# %% 3. Agrupación por rango de edad y cálculo de promedios
consulta_t_edad_mujeres = """
    SELECT 
        rango_edad, 
        COUNT(*) AS total,
        AVG(Tiempo) AS promedio
    FROM mujeres
    GROUP BY rango_edad
    ORDER BY rango_edad
"""

resumen_mujeres = duckdb.sql(consulta_t_edad_mujeres).df()


# %% 4. Crear formato de texto MM:SS para las etiquetas del gráfico
minutos = resumen_mujeres['promedio'] // 1
segundos = (resumen_mujeres['promedio'] % 1) * 60

resumen_mujeres['promedio_formateado'] = (
    minutos.astype(int).astype(str) + ":" + 
    segundos.round().astype(int).astype(str).str.zfill(2)
)

print(resumen_mujeres)

# %% 
plt.figure(figsize=(10, 6))

# Graficamos usando los valores numéricos reales (promedio)
plt.scatter(resumen_mujeres['rango_edad'], resumen_mujeres['promedio'], color='tab:pink', zorder=3)
plt.plot(resumen_mujeres['rango_edad'], resumen_mujeres['promedio'], color='tab:pink', alpha=0.5, linestyle='--')

plt.xlabel('Rango de edad (Mujeres)')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Tiempo promedio (Minutos)')
plt.title('Distribución de tiempos promedio por rango de edad - Mujeres')
plt.grid(True, linestyle=':', alpha=0.6)

plt.show()

#%%
distancia = 10 
limites = np.arange(25,150,5)

hombres['ritmos'] = hombres['Tiempo']/distancia
mujeres['ritmos'] = ['Tiempo']/distancia
print(hombres['ritmos'])



# %%
import matplotlib.ticker as ticker

# 1. Definimos los ritmos centrales que queremos mostrar (cada 30 segundos)
ritmos_centros = np.arange(3.0, 11, 0.5) 

# 2. Creamos las etiquetas formateadas en MM:SS para los centros (3:00, 3:30, 4:00...)
labels_centros = []
for c in ritmos_centros:
    minutos = int(c // 1)
    segundos = int(round((c % 1) * 60))
    labels_centros.append(f"{minutos}:{segundos:02d}")

# 3. Calculamos los bordes de los bines para que los centros queden en el medio
# Restamos y sumamos 15 segundos (0.25 minutos) a cada centro
ritmos_bordes = np.append(ritmos_centros - 0.25, ritmos_centros[-1] + 0.25)

# %% Graficamos
plt.figure(figsize=(11, 6))

# Dibujamos el histograma usando los bordes calculados
plt.hist(hombres['ritmos'], bins=ritmos_bordes, color='tab:pink', edgecolor="white", zorder=3)

plt.title("Distribución de Ritmos en Hombres", fontsize=14, pad=15)
plt.xlabel("Ritmo (minutos por kilómetro)", fontsize=12)
plt.ylabel("Número de participantes", fontsize=12)

# 4. Clavamos los ticks principales en los centros con sus etiquetas MM:SS
plt.xticks(ticks=ritmos_centros, labels=labels_centros, rotation=45, ha="right")

# 5. Ponemos los ticks menores en los bordes reales de las barras
ax = plt.gca()
ax.xaxis.set_minor_locator(ticker.FixedLocator(ritmos_bordes))

# 6. Rejilla y ajuste
plt.grid(axis="y", linestyle="--", alpha=0.7, zorder=0)
plt.tight_layout()

plt.show()
# %%
plt.figure(figsize=(11, 6))

# Dibujamos el histograma usando los bordes calculados
plt.hist(mujeres['ritmos'], bins=ritmos_bordes, color='tab:pink', edgecolor="white", zorder=3)

plt.title("Distribución de Ritmos en Mujeres", fontsize=14, pad=15)
plt.xlabel("Ritmo (minutos por kilómetro)", fontsize=12)
plt.ylabel("Número de participantes", fontsize=12)

# 4. Clavamos los ticks principales en los centros con sus etiquetas MM:SS
plt.xticks(ticks=ritmos_centros, labels=labels_centros, rotation=45, ha="right")

# 5. Ponemos los ticks menores en los bordes reales de las barras
ax = plt.gca()
ax.xaxis.set_minor_locator(ticker.FixedLocator(ritmos_bordes))

# 6. Rejilla y ajuste
plt.grid(axis="y", linestyle="--", alpha=0.7, zorder=0)
plt.tight_layout()

plt.show()