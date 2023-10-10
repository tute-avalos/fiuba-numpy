import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter

# Crear una señal de ejemplo
T = np.linspace(0, 1, 1000, endpoint=False)
SIGNAL = np.sin(2 * np.pi * 5 * T) + 0.5 * np.random.normal(size=1000)

# Crear un filtro pasa-bajas
def butter_lowpass(cutoff, fs, order=5):
    NYQUIST = 0.5 * fs
    NORMAL_CUTOFF = cutoff / NYQUIST
    return butter(order, NORMAL_CUTOFF, btype='low', analog=False)

def butter_lowpass_filter(data, cutoff, fs, order=5):
    numerator, denominator = butter_lowpass(cutoff, fs, order=order)
    return lfilter(numerator, denominator, data)

# Aplicar el filtro
FS = 1000.0
CUTOFF = 10.0
FILTERED_SIGNAL = butter_lowpass_filter(SIGNAL, CUTOFF, FS, order=1)

# Visualizar la señal original y la señal filtrada
plt.figure(figsize=(10, 6))
plt.plot(T, SIGNAL, '-', color='lightblue' ,label='Señal Original')
plt.plot(T, FILTERED_SIGNAL, '-', color='green',linewidth=2, label='Señal Filtrada')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend(loc='best')
plt.grid()
plt.show()
