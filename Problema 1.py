import numpy as np
import matplotlib.pyplot as plt

# Paso 1: Generar 1000 números aleatorios con media 0 y desviación estándar 0.1
mu = 0
sigma = 0.1
random_numbers = np.random.normal(mu, sigma, 1000)

# Paso 2: Mostrar una gráfica de estos valores utilizando Matplotlib
plt.figure(figsize=(8, 6))
plt.hist(random_numbers, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribución de 1000 números aleatorios')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()
 