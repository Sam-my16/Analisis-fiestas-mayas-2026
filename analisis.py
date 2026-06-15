# Requiere haber ejecutado carga_datos.py y tablas.py previamente
# (resumen, resumen_mujeres, hombres, mujeres, resumen_genero deben estar en el entorno)

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import seaborn as sns
import os

# Carpeta donde se guardan las imágenes
os.makedirs('imagenes', exist_ok=True)

# ── Tiempo promedio por rango de edad - Hombres ──────────────────────────────
plt.figure(figsize=(10, 6))
plt.scatter(resumen['rango_edad'], resumen['promedio'], color='tab:blue', zorder=3)
plt.plot(resumen['rango_edad'], resumen['promedio'], color='tab:blue', alpha=0.5, linestyle='--')
plt.xlabel('Rango de edad (Hombres)')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Tiempo promedio (Minutos)')
plt.title('Distribución de tiempos promedio por rango de edad - Hombres')
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.savefig('imagenes/tiempo_edad_hombres.png', dpi=100, bbox_inches='tight')
plt.show()

# ── Tiempo promedio por rango de edad - Mujeres ──────────────────────────────
plt.figure(figsize=(10, 6))
plt.scatter(resumen_mujeres['rango_edad'], resumen_mujeres['promedio'], color='tab:pink', zorder=3)
plt.plot(resumen_mujeres['rango_edad'], resumen_mujeres['promedio'], color='tab:pink', alpha=0.5, linestyle='--')
plt.xlabel('Rango de edad (Mujeres)')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Tiempo promedio (Minutos)')
plt.title('Distribución de tiempos promedio por rango de edad - Mujeres')
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.savefig('imagenes/tiempo_edad_mujeres.png', dpi=100, bbox_inches='tight')
plt.show()

# ── Configuración de bines de ritmo (compartida) ─────────────────────────────
ritmos_centros = np.arange(3.0, 11, 0.5)
ritmos_bordes = np.append(ritmos_centros - 0.25, ritmos_centros[-1] + 0.25)

labels_centros = []
for c in ritmos_centros:
    minutos = int(c // 1)
    segundos = int(round((c % 1) * 60))
    labels_centros.append(f"{minutos}:{segundos:02d}")

# ── Histograma de ritmos - Hombres ───────────────────────────────────────────
plt.figure(figsize=(11, 6))
plt.hist(hombres['ritmos'], bins=ritmos_bordes, color='tab:blue', edgecolor='white', zorder=3)
plt.title("Distribución de Ritmos en Hombres", fontsize=14, pad=15)
plt.xlabel("Ritmo (minutos por kilómetro)", fontsize=12)
plt.ylabel("Número de participantes", fontsize=12)
plt.xticks(ticks=ritmos_centros, labels=labels_centros, rotation=45, ha='right')
ax = plt.gca()
ax.xaxis.set_minor_locator(ticker.FixedLocator(ritmos_bordes))
plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)
plt.tight_layout()
plt.savefig('imagenes/ritmos_hombres.png', dpi=100, bbox_inches='tight')
plt.show()

# ── Histograma de ritmos - Mujeres ───────────────────────────────────────────
plt.figure(figsize=(11, 6))
plt.hist(mujeres['ritmos'], bins=ritmos_bordes, color='tab:pink', edgecolor='white', zorder=3)
plt.title("Distribución de Ritmos en Mujeres", fontsize=14, pad=15)
plt.xlabel("Ritmo (minutos por kilómetro)", fontsize=12)
plt.ylabel("Número de participantes", fontsize=12)
plt.xticks(ticks=ritmos_centros, labels=labels_centros, rotation=45, ha='right')
ax = plt.gca()
ax.xaxis.set_minor_locator(ticker.FixedLocator(ritmos_bordes))
plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)
plt.tight_layout()
plt.savefig('imagenes/ritmos_mujeres.png', dpi=100, bbox_inches='tight')
plt.show()

# ── Comparación hombres vs mujeres ───────────────────────────────────────────
plt.figure(figsize=(8, 6))
sns.barplot(data=resumen_genero, x='genero', y='tiempo_promedio',
            palette=['tab:blue', 'tab:pink'])
plt.ylabel('Tiempo promedio (minutos)')
plt.title('Tiempo promedio por género')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('imagenes/comparacion_genero.png', dpi=100, bbox_inches='tight')
plt.show()