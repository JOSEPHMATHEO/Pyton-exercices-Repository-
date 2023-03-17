import matplotlib.pyplot as plt

print("Frecuencia de de horas jugadas en la Semana")
print("================================")
x = [1,2,3,4,5,6,7]
y = [2,3,0,1,2,3,4]

dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

plt.xticks(x,dias)
plt.plot(x,y)
plt.bar(x,y)
plt.ylabel("Dias de la Semana")
plt.title("Frecuencia de horas jugadas en la Semana")
plt.show()