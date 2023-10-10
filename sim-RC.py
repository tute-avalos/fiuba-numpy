import numpy as np
import matplotlib.pyplot as plt

# Crear un modelo de circuito simple
R = 100_000     # Resistencia en ohms
C = 4.7e-6      # Capacitancia en faradios
V_IN = 4.7      # Voltaje de entrada

# Simular la carga de un capacitor a través de la resistencia
T = np.linspace(0, 5, 1000)
V_OUT = V_IN * (1 - np.exp(-T / (R * C)))

# Visualizar la respuesta del circuito
plt.plot(T, V_OUT)
plt.title('Respuesta de un Circuito RC')
plt.xlabel('Tiempo [s]')
plt.ylabel('Voltaje de Salida [V]')
plt.grid()
plt.show()
