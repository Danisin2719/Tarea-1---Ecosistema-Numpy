"""
Problema 4

Integrantes:
Daniel Salinas
Anthony Garcia

"""

import pandas as pd
import matplotlib.pyplot as plt


# 1. Cargar el archivo CSV
file_path = "yellow_tripdata_2023-01.parquet"  # Reemplazar con la ruta correcta del archivo
data = pd.read_parquet(file_path)

# 2. Elegir un mes particular entre los años 2019 y 2024
# Por ejemplo, elegir el mes de enero de 2023
start_date = '2019-01-01'
end_date = '2024-01-31'
selected_month_data = data[(data['tpep_pickup_datetime'] >= start_date) & (data['tpep_pickup_datetime'] <= end_date)]

# 3. a. Verificar cuántos registros tiene el archivo
total_records = len(selected_month_data)
print("Cantidad total de registros:", total_records)

# 3. b. Verificar cómo es la cabecera del archivo y el final del archivo
print("Cabecera del archivo:")
print(selected_month_data.head())
print("\nFinal del archivo:")
print(selected_month_data.tail())

# 4. Identificar cuántos suplidores únicos existen
unique_vendors = selected_month_data['VendorID'].nunique()
print("\nCantidad de suplidores únicos:", unique_vendors)

# Comprobar que la suma de los registros de cada vendedor concuerda con el número total de registros
vendor_records_sum = selected_month_data.groupby('VendorID').size()
total_records_check = vendor_records_sum.sum()
print("Suma de registros de cada vendedor:")
print(vendor_records_sum)
print("Número total de registros calculado:", total_records_check)

# 5. Identificar la cantidad de viajes con un solo pasajero y más de un pasajero para todos los VendorID
solo_pasajero = selected_month_data[selected_month_data['passenger_count'] == 1].groupby('VendorID').size()
mas_de_un_pasajero = selected_month_data[selected_month_data['passenger_count'] > 1].groupby('VendorID').size()
promedio_pasajeros_vendedor_1 = selected_month_data[selected_month_data['VendorID'] == 1]['passenger_count'].mean()
print("\nCantidad de viajes con un solo pasajero por VendorID:")
print(solo_pasajero)
print("Cantidad de viajes con más de un pasajero por VendorID:")
print(mas_de_un_pasajero)
print("Promedio total de pasajeros con VendorID = 1:", promedio_pasajeros_vendedor_1)

# 6. Identificar los viajes que costaron arriba de $16.50 para todos los VendorID y hacer un nuevo dataframe
viajes_costosos = selected_month_data[selected_month_data['fare_amount'] > 16.50]

# 7. a. Extraer aquellos que son de un mismo vendedor del nuevo dataframe creado
viajes_mismo_vendedor = viajes_costosos.groupby('VendorID').get_group(viajes_costosos.iloc[0]['VendorID'])

# 7. b. i. Graficar el costo en función de la distancia
plt.scatter(viajes_mismo_vendedor['trip_distance'], viajes_mismo_vendedor['fare_amount'], alpha=0.5)
plt.xlabel('Distancia del viaje')
plt.ylabel('Costo del viaje')
plt.title('Costo del viaje vs. Distancia del viaje')
plt.grid(True)
plt.show()

# 7. b. ii. Calcular el coeficiente de correlación de Pearson de ambas columnas
correlacion_pearson = viajes_mismo_vendedor['trip_distance'].corr(viajes_mismo_vendedor['fare_amount'])
print("\nCoeficiente de correlación de Pearson entre costo del viaje y distancia del viaje:", correlacion_pearson)

# 7. b. iii. Responder las preguntas
# 1. ¿Cómo es el comportamiento de los costos?
# 2. ¿Están correlacionados con la distancia?
# 3. ¿En qué grado?

# 8. Hacer un tercer filtro, enfocarse en la columna congestion_surcharge
viajes_con_sobrecargo = selected_month_data[selected_month_data['congestion_surcharge'] > 0]

# 8. c. i. Calcular el número de viajes con sobrecargo en cada categoría de "horas pico" versus "horas no pico"
horas_pico = viajes_con_sobrecargo[
    (viajes_con_sobrecargo['tpep_pickup_datetime'].dt.hour >= 6) & 
    (viajes_con_sobrecargo['tpep_pickup_datetime'].dt.hour < 8) |
    (viajes_con_sobrecargo['tpep_pickup_datetime'].dt.hour >= 12) & 
    (viajes_con_sobrecargo['tpep_pickup_datetime'].dt.hour < 13) |
    (viajes_con_sobrecargo['tpep_pickup_datetime'].dt.hour >= 17) & 
    (viajes_con_sobrecargo['tpep_pickup_datetime'].dt.hour < 19)
]

horas_no_pico = viajes_con_sobrecargo[~viajes_con_sobrecargo.index.isin(horas_pico.index)]

cantidad_sobrecargo_horas_pico = len(horas_pico)
cantidad_sobrecargo_horas_no_pico = len(horas_no_pico)

print("\nCantidad de viajes con sobrecargo en horas pico:", cantidad_sobrecargo_horas_pico)
print("Cantidad de viajes con sobrecargo en horas no pico:", cantidad_sobrecargo_horas_no_pico)

# 8. c. ii. Responder la pregunta sobre la relación entre sobrecargo y horas pico
if cantidad_sobrecargo_horas_pico > cantidad_sobrecargo_horas_no_pico:
    print("Sí, hay más viajes con sobrecargo en horas pico que en horas no pico.")
else:
    print("No, no hay más viajes con sobrecargo en horas pico que en horas no pico.")
