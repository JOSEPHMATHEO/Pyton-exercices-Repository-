print("Bucles En Pyton")
print("=====================")

x = 0 
people = []

while len(people) < 5:

    persona = ( input(" Ingrese el nombre de una persona:" ) )
    people.append(persona)

print(people)

print("Bucles 2 En Pyton")
print("=====================")

import random

number = random.randint(0,10)

adivinanza = int ( input ("Ingrese un numero al azar: ") ) 

while True:
    
    if adivinanza == number:
        
        break
    
    else:

        adivinanza = int ( input ("Incorrecto, Ingrese otro numero: " ) )

print ("Correcto!")