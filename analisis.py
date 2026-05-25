import pandas as pd
import duckdb


carpeta = r'C:\Users\Nt\Desktop\Carrera\Laboratorio de Datos\Analisis-fiestas-mayas-2026\\'

df = pd.read_csv(carpeta +'fiestas_mayas_2026.csv')

print("Filas descargadas:", len(df))
print("\nPrimeras 3 filas:")
print(df.head(3))
print("\nColumnas:", df.columns.tolist())