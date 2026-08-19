import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# ==========================================
# 1. PREPARACIÓN Y SIMULACIÓN DE DATOS
# ==========================================
np.random.seed(42)

# Simulación de salarios anuales en dos departamentos (distribución log-normal)
salarios_ti = np.random.lognormal(mean=10.8, sigma=0.4, size=500)
salarios_mkt = np.random.lognormal(mean=10.4, sigma=0.35, size=500)

df_ti = pd.DataFrame({'Salario': salarios_ti, 'Departamento': 'TI'})
df_mkt = pd.DataFrame({'Salario': salarios_mkt, 'Departamento': 'Marketing'})

df_empleados = pd.concat([df_ti, df_mkt], ignore_index=True)

# Configuración global
plt.rcParams['figure.figsize'] = (10, 5)
sns.set_theme(style='whitegrid', palette='muted')

# ==========================================
# 2. HISTOGRAMA + KDE CON SEABORN
# ==========================================
plt.figure()
sns.histplot(
    data=df_empleados,
    x='Salario',
    hue='Departamento',
    bins=30,
    kde=True,
    element='step',
    alpha=0.4,
)
plt.title(
    'Distribución Salarial por Departamento (Histograma + KDE)', fontsize=14
)
plt.xlabel('Salario Anual (USD)')
plt.ylabel('Frecuencia / Conteo')
plt.tight_layout()
plt.show()

# ==========================================
# 3. DIAGRAMA DE CAJA (BOXPLOT) CON SEABORN
# ==========================================
plt.figure()
sns.boxplot(
    data=df_empleados,
    x='Departamento',
    y='Salario',
    palette='Set2',
    width=0.4,
    fliersize=5,
)
plt.title(
    'Comparativa de Distribución y Outliers por Departamento (Boxplot)',
    fontsize=14,
)
plt.xlabel('Departamento')
plt.ylabel('Salario Anual (USD)')
plt.tight_layout()
plt.show()

# ==========================================
# 4. HISTOGRAMA Y BOXPLOT CON MATPLOTLIB / PANDAS API
# ==========================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Histograma en Pandas
df_empleados[df_empleados['Departamento'] == 'TI']['Salario'].plot(
    kind='hist', bins=25, ax=ax1, color='skyblue', edgecolor='black'
)
ax1.set_title('Histograma Pandas (Solo TI)')
ax1.set_xlabel('Salario')

# Boxplot en Matplotlib
ax2.boxplot(
    [
        df_empleados[df_empleados['Departamento'] == 'TI']['Salario'],
        df_empleados[df_empleados['Departamento'] == 'Marketing']['Salario'],
    ],
    labels=['TI', 'Marketing'],
    patch_artist=True,
)
ax2.set_title('Boxplot Matplotlib')
ax2.set_ylabel('Salario')

plt.tight_layout()
plt.show()