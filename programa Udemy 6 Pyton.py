print("Condicionales En Pyton")
print("=====================")

dato = False 

while dato == False:
    
    nota1 = float ( input ("Ingrese la nota del 1 examen:") )

    if nota1 < 0 or nota1 > 10: 

        print("La nota debe estar ente 0 y 10")
        continue

    else:

        dato = True

dato = False 

while dato == False:
    
    nota2 = float ( input ("Ingrese la nota del 2 examen:") )

    if nota2 < 0 or nota2 > 10: 

        print("La nota debe estar ente 0 y 10")
        continue

    else:

        dato = True

dato = False 

while dato == False:
    
    clases = int ( input ( "Ingrese el numero de clases:") )

    if clases <= 0:

        print("La clases deben ser mayores 0")
        continue

    else:

        dato = True 

dato = False
    
while dato == False:
    
    ausencias = int ( input ( "Ingrese el numero de ausencias:") )

    if ausencias < 0 or ausencias > clases:

        print("Las ausencias no deben ser mayores o menores a las clases")
        continue

    else:

        dato = True 



notafinal = ( nota1 + nota2 ) / 2
asistencia = ( clases - ausencias ) / clases 

print("Sus notas son: ")
print("Sus nota final es de:", round(notafinal,2) )
print("Sus taza de asistencia es de:", round(asistencia * 100,2), "%")

if notafinal >= 7:

    if asistencia >= 0.8:

        print("Usted ah aprovado!")

    else:

        print("Usted ah desaprovado por faltas!")
    
elif asistencia >= 0.8:

    print ("Usted a desaprovado porque su nota es menor a 7")

else:

    print("Usted a suspendido porque la nota es menor a 7 y por faltas")

