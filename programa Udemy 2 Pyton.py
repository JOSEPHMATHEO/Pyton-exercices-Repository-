import math
import time as date

print("Enteros en Pyton")
print("================")

radio = float( input("\nIngrese el radio del circulo: " ) )

area = math.pi * (radio ** 2)
circunferencia = 2 * math.pi * radio

print("\nEl area del circulo es:",round(area,2) )
print("\nEla circunferencia del circulo es:",round(circunferencia,2) )

print(date.localtime())