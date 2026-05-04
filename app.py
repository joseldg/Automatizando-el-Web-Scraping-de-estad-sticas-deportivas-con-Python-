from pybaseball import batting_stats_bref
import pandas as pd

# 1. Obtener estadísticas de bateo para la temporada 2023 desde Baseball Reference
data = batting_stats_bref(2023)

# 2. Como es un DataFrame de Pandas, podemos filtrar fácilmente
# Por ejemplo: Jugadores con más de 20 Home Runs ordenados de forma descendente
power_hitters = data[data['HR'] > 20].sort_values(by='HR', ascending=False)

# 3. Mostrar los primeros 10
print(power_hitters[['Name', 'Tm', 'HR', 'BA', 'OPS']].head(10))

# 4. Exportar a CSV (muy útil para tus otros proyectos de automatización)
power_hitters.to_csv("power_hitters_2023.csv", index=False)