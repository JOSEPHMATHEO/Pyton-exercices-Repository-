print("Bucles En Pyton")
print("=====================")

cadena = "Esto es una cadena"

for x in range(0,5):

    if x == " ":

        continue

    else:

        print(x)

diccionary = {'Name':'Luis','Age':'20','Genre':'Male'}

for x in diccionary:

    print(x,":",diccionary[x])

print("------------------------")

lenguajes = {"Pyton":["Pyton es un lenguaje de programacion Celeste","Pyton es usado en Inteligencia Artificial","Hola Mundo"],"JavaScript":["JavaScript es un lenguaje de programacion Naranja","JavaScript es usado en Desarrollo Web"]}

for i in lenguajes:

    print("\nMensjaes sobre el Lenguaje",i,)
    print("==========================================")

    for j in lenguajes(0,1):

        print(j)