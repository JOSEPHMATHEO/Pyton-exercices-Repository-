print("Bucles En Pyton")
print("=====================")

import random
nombres = []

for i in range(0,8):

    
    persona = input("Ingrese el nombre: " )
    nombres.append(persona)

indice = random.randint(0,7)

person_a = nombres[indice]

print (person_a)

print("=========================")
print("Juego Adivinanza")

colores = ["rojo","azul","amarillo","verde","negro","morado","rosado"]

while True:

    color = colores[random.randint( 0,len( colores ) -1 ) ]
    adivinanza = input("Ingresa el Color: ")

    while True: 
        
        if (color == adivinanza.lower()): 
            break

        else:

            adivinanza = input("Ingresa el Color: ")

    print("si! Adivinzaste el color era ", color)

    nuevojuego = input("Quiere jugar de nuevo? Escriba 'si' o 'no' ")

    if nuevojuego.lower() == 'no':

        break 




        