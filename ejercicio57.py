#algoritmo que muestra la cantidad de años, meses y dias que hay en una fecha ingresada
dias = int(input("INGRESE CANTIDAD DE DIAS: "))
a = int(dias / 365)
m = int((dias - (a * 365)) / 30)
d = int(dias -((a * 365) + (m * 30)))
print("Año: ",a)
print("Mes: ",m)
print("Dia: ",d)