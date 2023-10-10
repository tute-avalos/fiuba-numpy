import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import resample

FINAL_SAMPLES = 4_000
#ORIGINAL_SAMPLES = 40_000  # scope_csv_47_0
ORIGINAL_SAMPLES = 400_000 # scope_csv_47_1

T_ORGIN = np.linspace(0, 1, ORIGINAL_SAMPLES, endpoint=False)
T_OVER = np.linspace(0, 1, FINAL_SAMPLES, endpoint=False)
# Cargar una señal electrónica desde un archivo (por ejemplo, un archivo CSV)
data = np.loadtxt('./resources/scope_csv_47_1.csv', delimiter=',', usecols=(0,1,2), skiprows=1)

over_sampled = resample(data[:,1:2],FINAL_SAMPLES)

# Visualizar la señal
plt.plot(T_ORGIN, data[:,1:2], color='lightblue')
plt.plot(T_OVER, over_sampled, color='orange', linewidth=2)#)data[:,1:3])
plt.title('Señal')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.show()

# Calcular la frecuencia de muestreo
frecuencia_muestreo = 1.0 / (data[0][0])
print(f'Frecuencia de muestreo: {frecuencia_muestreo}')

# Calcular el valor medio de la señal
valor_medio = np.mean(data[1])
print(f'Valor Medio:{valor_medio}')
