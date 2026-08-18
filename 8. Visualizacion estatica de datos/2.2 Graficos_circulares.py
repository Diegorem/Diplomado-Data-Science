import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# ==========================================
# 1. PREPARACIÓN DE DATOS DE EJEMPLO
# ==========================================
# Distribución de ventas por canal
data = {
    'Canal': ['Tienda Física', 'Sitio Web', 'App Móvil', 'Distribuidores'],
    'Ventas': [4500, 3200, 2100, 1200],
}
df_ventas = pd.DataFrame(data)

# Paleta de colores consistente
colores = ['#2b5c8f', '#4682b4', '#6baed6', '#9ecae1']

# ==========================================
# 2. MATPLOTLIB: Gráfico Circular Tradicional con Explode
# ==========================================
plt.figure(figsize=(7, 7))

# Destacar el canal líder (Tienda Física)
explode = (0.08, 0, 0, 0)

plt.pie(
    df_ventas['Ventas'],
    labels=df_ventas['Canal'],
    autopct='%1.1f%%',
    startangle=140,
    explode=explode,
    colors=colores,
    shadow=True,
    textprops={'fontsize': 11},
)

plt.title(
    'Distribución de Ventas por Canal (Matplotlib Pie)',
    fontsize=14,
    pad=20,
    weight='bold',
)
plt.tight_layout()
plt.show()

# ==========================================
# 3. MATPLOTLIB: Gráfico de Dona (Donut Chart)
# ==========================================
plt.figure(figsize=(7, 7))

# wedgeprops con width crea el hueco central
plt.pie(
    df_ventas['Ventas'],
    labels=df_ventas['Canal'],
    autopct='%1.1f%%',
    startangle=90,
    colors=colores,
    pctdistance=0.75,  # Ubicación del texto del porcentaje
    wedgeprops=dict(width=0.35, edgecolor='white', linewidth=2),
)

# Texto en el centro de la dona
plt.text(
    0,
    0,
    'Total\n11,000',
    ha='center',
    va='center',
    fontsize=12,
    weight='bold',
)

plt.title('Participación de Mercado (Gráfico de Dona)', fontsize=14, pad=20)
plt.tight_layout()
plt.show()

# ==========================================
# 4. PANDAS API (.plot)
# ==========================================
# Pandas requiere usar la columna de categorías como índice
df_pie = df_ventas.set_index('Canal')

ax = df_pie.plot(
    kind='pie',
    y='Ventas',
    figsize=(7, 7),
    autopct='%1.0f%%',
    colors=colores,
    legend=False,
    ylabel='',  # Elimina la etiqueta lateral del eje Y que pone Pandas por defecto
)

plt.title('Ventas por Canal (Pandas API)', fontsize=14)
plt.tight_layout()
plt.show()

# ==========================================
# 5. ALTERNATIVA SEABORN (Barplot)
# ==========================================
# Ya que Seaborn no soporta pie charts, se usa un gráfico de barras horizontal
plt.figure(figsize=(8, 4))
sns.set_theme(style='whitegrid')

ax = sns.barplot(
    data=df_ventas,
    x='Ventas',
    y='Canal',
    palette='Blues_r',
    hue='Canal',
    legend=False,
)

plt.title(
    'Alternativa Recomendada en Seaborn (Barplot Visualmente Preciso)',
    fontsize=12,
)
plt.xlabel('Volumen de Ventas')
plt.ylabel('')

# Agregar etiquetas de porcentaje en las barras
total = df_ventas['Ventas'].sum()
for p in ax.patches:
    percentage = f'{100 * p.get_width() / total:.1f}%'
    x = p.get_width() + 100
    y = p.get_y() + p.get_height() / 2
    ax.annotate(percentage, (x, y), ha='left', va='center', fontsize=10)

plt.xlim(0, 5500)
plt.tight_layout()
plt.show()