#algoritmo que muestre el nivel academico de un alumno segun la nota ingresada
n1 = int(input("INGRESE NOTA 1: "))
n2 = int(input("INGRESE NOTA 2: "))
n3 = int(input("INGRESE NOTA 3: "))

prom = round((n1 + n2 + n3) / 3)
print(prom)

if prom in range(1, 11):
    print("NIVEL MALO")
elif prom in range(11, 14):
    print("NIVEL REGULAR")
elif prom in range(14, 17):
    print("NIVEL BUENO")
elif prom in range(17, 21):
    print("NIVEL MUY BUENO")


    
