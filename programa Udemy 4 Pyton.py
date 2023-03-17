print("Diccionarios en Pyton")
print("=====================")
diccionario = {"name":"luis Morales","gender":"Male","age":"20","addres":"'El Plateado'","phone":"0991526892"}
n = input("Ingrese la informacion que desea saber sobre la persona: ").lower()
resp = diccionario.get(n, "la informacion no esta disponible")
print(resp)