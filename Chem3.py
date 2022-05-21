"""

Práctica 3 - Química
Grado en Física - Universidad de Alicante
Luis Lucas García

"""

import numpy as np
import matplotlib.pyplot as plt

entrada = open("datos", "r")

V, pH = [], []

for linea in entrada:
    
    V.append(float(linea.split()[0]))
    pH.append(float(linea.split()[1]))
    
entrada.close()

plt.figure(figsize=(9, 5))
plt.plot(V, pH, "r*")
plt.xlabel("V (mL)")
plt.ylabel("pH")
plt.savefig("scatter.png", dpi=1200)

medioV = [(V[i+1] + V[i])/2 for i in range(len(V)-1)]
dV = [(pH[i+1] - pH[i])/(V[i+1] - V[i]) for i in range(len(V)-1)]

plt.figure(figsize=(9, 5))
plt.plot(medioV, dV)
plt.xlabel(r'$ \frac{V_{i+1} + V_{i}}{2} $')
plt.ylabel(r'$ \frac{pH_{i+1} - pH_{i}}{V_{i+1} - V_{i}} $')
plt.savefig("derivada.png", dpi = 1200)

ki = np.argmax(dV[:16:])
ki2 = np.argmax(dV[16::])
print(medioV[ki], medioV[ki2 + 16])