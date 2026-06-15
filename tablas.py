# Requiere haber ejecutado carga_datos.py previamente
# (hombres y mujeres deben estar en el entorno)

import duckdb

# --- Categorías disponibles ---
consulta_categorias = '''
    SELECT DISTINCT "Categoría" AS "Categorías"
    FROM df
    ORDER BY "Categoría"
'''
categorias = duckdb.sql(consulta_categorias).df()
print("Categorías encontradas:")
print(categorias)

# --- Participantes sin categoría ---
consulta_nb = """
    SELECT *
    FROM df
    WHERE "Categoría" = 'Sin categoría'
    ORDER BY "Posicion"
"""
nb = duckdb.sql(consulta_nb).df()
print("\nParticipantes sin categoría:")
print(nb)

# --- Resumen hombres por rango de edad ---
consulta_t_edad = """
    SELECT
        rango_edad,
        COUNT(*) AS total,
        AVG(Tiempo) AS promedio
    FROM hombres
    GROUP BY rango_edad
    ORDER BY rango_edad
"""
resumen = duckdb.sql(consulta_t_edad).df()

minutos = resumen['promedio'] // 1
segundos = (resumen['promedio'] % 1) * 60
resumen['promedio_formateado'] = (
    minutos.astype(int).astype(str) + ":" +
    segundos.round().astype(int).astype(str).str.zfill(2)
)
print("\nResumen hombres por rango de edad:")
print(resumen)

total_hombres = '''SELECT 
                    COUNT(*) AS total_hombres, 
                    AVG(Tiempo) AS tiempo_promedio
                   FROM hombres'''

total_hombres = duckdb.sql(total_hombres).df()

# --- Resumen mujeres por rango de edad ---
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

minutos = resumen_mujeres['promedio'] // 1
segundos = (resumen_mujeres['promedio'] % 1) * 60
resumen_mujeres['promedio_formateado'] = (
    minutos.astype(int).astype(str) + ":" +
    segundos.round().astype(int).astype(str).str.zfill(2)
)
print("\nResumen mujeres por rango de edad:")
print(resumen_mujeres)

#%%
total_mujeres = duckdb.sql('''SELECT 
                                COUNT(*) AS total,
                                AVG(Tiempo) AS tiempo_promedio
                              FROM mujeres''').df()
total_mujeres['genero'] = 'Mujeres'

total_hombres = duckdb.sql('''SELECT 
                                COUNT(*) AS total,
                                AVG(Tiempo) AS tiempo_promedio
                              FROM hombres''').df()
total_hombres['genero'] = 'Hombres'

resumen_genero = pd.concat([total_hombres, total_mujeres], ignore_index=True)
print(resumen_genero)
# %%
