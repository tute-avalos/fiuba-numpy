import numpy as np
import matplotlib.pyplot as plt

# Cargar una señal electrónica desde un archivo (por ejemplo, un archivo CSV)
data = np.loadtxt('./resources/scope_csv_47_1.csv', delimiter=',', usecols=(0,1,2), skiprows=1)

# Visualizar la señal
plt.plot(data[:,1:3])
plt.title('Señal')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.show()

# Calcular la frecuencia de muestreo
frecuencia_muestreo = 1.0 / (data[0][0])
print(f'Frecuencia de muestreo: {frecuencia_muestreo}' )

# Calcular el valor medio de la señal
valor_medio = np.mean(data[1])
print(f'Valor Medio CH1:{valor_medio}')
