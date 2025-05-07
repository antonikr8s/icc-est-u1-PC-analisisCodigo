#pin install matplotlib

import matplotlib
import matplotlib.pyplot as plt

x=[1,2,3,4,5,7,2]
y=[2,4,6,8,10,57,5]
nombre_linea1 = "Linea1"

plt.plot(x,y, label=nombre_linea1, color="blue")

#agregar parametros
plt.title("Primer grafico") #Titulo
plt.xlabel("Datos eje X")
plt.ylabel("Datos eje Y")

plt.legend()
plt.show()