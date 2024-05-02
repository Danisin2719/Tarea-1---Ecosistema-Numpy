"""
Problema 3

Integrantes:
Daniel Salinas
Anthony Garcia

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Paso 1: Cargar el conjunto de datos
data = pd.read_csv("airfoil_self_noise.dat", sep="\t", header=None)
# Asignar nombres a las columnas
data.columns = ["Frequency", "Angle of Attack", "Chord Length", "Free Stream Velocity", "Suction Side Displacement Thickness", "Scaled Sound Pressure Level"]

# Paso 2: Identificar variables numéricas
numeric_columns = data.select_dtypes(include=[np.number]).columns

# Paso 3: Aplicar la normalización estándar a 3 columnas
scaler = StandardScaler()
data_normalized = data.copy()
data_normalized[numeric_columns[:3]] = scaler.fit_transform(data_normalized[numeric_columns[:3]])

# Paso 4: Visualizar la distribución de los datos antes y después de la normalización
plt.figure(figsize=(15, 10))
for i, column in enumerate(numeric_columns[:3]):
    plt.subplot(3, 2, 2*i+1)
    plt.hist(data[column], bins=30, color='skyblue', alpha=0.7, label='Original', edgecolor='black')
    plt.title("Distribución de " + column + " (Original)", fontsize=12, color='blue')
    plt.xlabel(column, fontsize=10, color='blue')
    plt.ylabel("Frecuencia", fontsize=10, color='blue')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xlim(left=data[column].min(), right=data[column].max())
    
    plt.subplot(3, 2, 2*i+2)
    plt.hist(data_normalized[column], bins=30, color='salmon', alpha=0.7, label='Normalizado', edgecolor='black')
    plt.title("Distribución de " + column + " (Normalizado)", fontsize=12, color='red')
    plt.xlabel(column, fontsize=10, color='red')
    plt.ylabel("Frecuencia", fontsize=10, color='red')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xlim(left=data_normalized[column].min(), right=data_normalized[column].max())

plt.tight_layout()
plt.show()
