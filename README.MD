# Análisis Fiestas Mayas 2026 🏃

Análisis exploratorio de los resultados de la carrera **Fiestas Mayas 2026** (10km), procesando tiempos, ritmos y distribución de participantes por género y rango de edad.

---

## Estructura del proyecto

```
Analisis-fiestas-mayas-2026/
│
├── fiestas_mayas_2026.csv      # Datos crudos de la carrera
│
├── carga_datos.py              # Lectura, limpieza y transformación de datos
├── tablas.py                   # Consultas DuckDB y resúmenes por grupo
├── visualizaciones.py          # Gráficos con matplotlib y seaborn
│
└── README.md
```

## Orden de ejecución

Los archivos deben ejecutarse en este orden, ya que cada uno depende del entorno generado por el anterior:

1. `carga_datos.py` → genera `df`, `hombres`, `mujeres`
2. `tablas.py` → genera `resumen`, `resumen_mujeres`, `resumen_genero`
3. `visualizaciones.py` → produce todos los gráficos

---

## Dependencias

```
pandas
duckdb
matplotlib
seaborn
numpy
```

Instalación:
```bash
pip install pandas duckdb matplotlib seaborn numpy
```

---

## Gráficos generados

- Tiempo promedio por rango de edad — Hombres
- Tiempo promedio por rango de edad — Mujeres
- Histograma de ritmos (min/km) — Hombres
- Histograma de ritmos (min/km) — Mujeres
- Comparación de tiempo promedio por género

---

## Análisis

> ✏️ *Esta sección es para completar con tus propias conclusiones.*

### Participación

<!-- ¿Cuántos participantes hubo en total? ¿Cómo se distribuyeron por género?
     ¿Qué rango de edad tuvo más participantes? -->

### Tiempos y ritmos

<!-- ¿Cuál fue el tiempo promedio general? ¿Hubo diferencias entre hombres y mujeres?
     ¿En qué ritmo se concentró la mayor parte de los participantes? -->

### Distribución por edad

<!-- ¿Cómo varía el tiempo promedio a medida que aumenta la edad?
     ¿Hay algún grupo etario que se destaque por sus tiempos? -->

### Observaciones generales

<!-- Cualquier patrón, anomalía o dato interesante que hayas notado en el análisis. -->

---

## Fuente de datos

Resultados oficiales de la carrera Fiestas Mayas 2026.