#algoritmo que muestra el area, la base y altura de un triangulo
print("MENU DE OPCIONES DE UN TRIANGULO")
print("---------------------------------")
print("1. Area de un triangulo, dada la base y la altura")
print("2. Base de un ttriangulo, dada la altura y el area")
print("3. Altura de un triangulo, dada la base y el area")
opc = int(input("Selecciona una opcion: "))

if (opc == 1):
    base = float(input("BASE: "))
    altura = float(input("ALTURA: "))

    area = (base * altura)/2
    print("EL AREA ES: ",area)
elif (opc == 2):
    altura = float(input("ALTURA: "))
    area = float(input("AREA: "))

    base = (area * 2)/altura
    print("LA BASE ES: ",base)
elif (opc == 3):
    base = float(input("BASE: "))
    area = float(input("AREA: "))

    altura = (area * 2)/base
    print("LA BASE ES: ",altura)
else:
    print("Error... Opcion invalida")

