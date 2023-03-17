#Importaciones

import matplotlib.pyplot as plt
import time as t

#Declaracion de variables

time = []
errores = 0

#Presentacion del Porgrama

print("Este programa te ayudara a escribir mas rapido")
print("==============================================")

#Proceso

input("Presiones enter para continuar...")

while len(time) < 5:

    inicio = t.time()
    palabra = input("Escriba la palabra: ")
    fin = t.time()

    tiempof = fin - inicio

    time.append(tiempof)

    if (palabra.lower() != "programacion"):

        errores += 1 

print("Has cometido " + str(errores) + " errores. ")
print("Esta es su grafica...")
t.sleep(3)

x = [1,2,3,4,5]
y = time

plt.plot(x,y)
plt.show()