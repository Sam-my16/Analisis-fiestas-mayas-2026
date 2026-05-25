
import pandas as pd
import requests  

#%%%

#Dirección de extración de datos 

URL = 'https://my-br-1.raceresult.com/399720/results/list?key=9db424ed2100d587dddba7baadce52ff&listname=Clasificacion%7CGeneralWeb2&page=results&contest=1&r=all&l=0&openedGroups=%7B%7D&term='

# Acá le digo al servidor que soy un USUARIO, no un bot
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# Descargamos los datos de la carrera
print("Descargando datos desde RaceResult...")
response = requests.get(URL, headers=headers)
data = response.json()


print("Estructura del JSON detectada:", data.keys())

# Extraemos la matriz de datos pura 
if 'data' in data:
    clave_datos = 'data'
elif 'aaData' in data:
    clave_datos = 'aaData'
else:
    clave_datos = list(data.keys())[0] # Intenta agarrar la primera si cambia

filas_corredores = data[clave_datos]

# Convertimos la lista de listas en un DataFrame de Pandas
df = pd.DataFrame(filas_corredores)

#%%
# Limpio el Dataframe para quedarme solo con la información que me interesa

eliminar = [0,1,3,4,8,9,11,12]
df = df.drop(df.columns[eliminar],axis=1)

# Renombro las columnas por algo legible

encabezado = ['Posicion', 'Nombre', 'Tiempo bruto', 'Tiempo neto','Categoría']
df.columns = encabezado

# finalmente descargo el archivo .csv, sín guardar los índices
df.to_csv('fiestas_mayas.csv', index=False)

