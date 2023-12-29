#algoritmo que muestre el monto a pagar segun el tipo de seguro elegido [x y z]
print("TIPOS DE SEGURO")
print("1. X")
print("2. Y")
print("3. Z")
seguro = int(input("OPCION: "))

if (seguro == 1):
    print("Pago Mensual: $45")
elif (seguro == 2):
    print("Pago Mensual: $30")
elif (seguro == 3):
    print("Pago Mensual: $15")
else:
    print("Error en el tipo de seguro")