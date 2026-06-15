# Análisis Fiestas Mayas 2026 🏃

Análisis exploratorio de los resultados de la carrera **Fiestas Mayas 2026** (10km), 50ª edición realizada el 25 de mayo en los Bosques de Palermo, Buenos Aires. Se procesan tiempos, ritmos y distribución de participantes por género y rango de edad.

---

## Estructura del proyecto

```
Analisis-fiestas-mayas-2026/
│
├── fiestas_mayas_2026.csv          # Datos crudos de la carrera
│
├── carga_datos.py                  # Lectura, limpieza y transformación de datos
├── tablas.py                       # Consultas DuckDB y resúmenes por grupo
├── visualizaciones.py              # Gráficos con matplotlib y seaborn
│
├── imagenes/                       # Gráficos generados automáticamente
│   ├── tiempo_edad_hombres.png
│   ├── tiempo_edad_mujeres.png
│   ├── ritmos_hombres.png
│   ├── ritmos_mujeres.png
│   └── comparacion_genero.png
│
└── README.md
```

## Orden de ejecución

Los archivos deben ejecutarse en este orden, ya que cada uno depende del entorno generado por el anterior:

1. `carga_datos.py` → genera `df`, `hombres`, `mujeres`
2. `tablas.py` → genera `resumen`, `resumen_mujeres`, `resumen_genero`
3. `visualizaciones.py` → produce y guarda todos los gráficos en `imagenes/`

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

## Gráficos

### Tiempo promedio por rango de edad

![Tiempo por edad - Hombres](imagenes/tiempo_edad_hombres.png)
![Tiempo por edad - Mujeres](imagenes/tiempo_edad_mujeres.png)

### Distribución de ritmos (min/km)

![Ritmos Hombres](imagenes/ritmos_hombres.png)
![Ritmos Mujeres](imagenes/ritmos_mujeres.png)

### Comparación por género

![Comparación género](imagenes/comparacion_genero.png)

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

Resultados oficiales de la carrera Fiestas Mayas 2026 — Club de Corredores.