#algoritmo que muestre el promedio de 3 notas y muestre si esta aprobado o desaprobado
n1 = int(input("INGRESE NOTA 01: "))
n2 = int(input("INGRESE NOTA 02: "))
n3 = int(input("INGRESE NOTA 03: "))

prom = (n1 + n2 + n3)/ 3
if (prom > 10.5):
    print("APROBADO CON ",prom)
else: 
    print("DESAPROBADO CON ",prom)