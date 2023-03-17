print("Listas y Tuplas")
print("===============")

students =["Jhon","Mary","Steve"]
students.append("Luis")
students.insert(1,"Peter")
students.pop(0)

studiantes = ("Jhon","Mary","Steve")

print(students[1])
print(studiantes[0])

print("Listas y Tuplas")
print("===============")

name = input("Ingrese su nombre: ")

students.append(name)

print(students)

print("Listas y Tuplas")
print("===============")

meses = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Noviembre','Diciembre')
date = input('Ingrese la fecha de su nacimiento en el siguiente formato: "DD-MM-YYYY:" ')

indice = int(date[3:5])

print("\n Usted nacion en",meses[indice-1])