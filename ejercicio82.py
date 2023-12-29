#algoritmo que calcule el igv del monto a pagar, si el monto es a $500
print("17. MOSTRAR 18% SI MONTO ES MAYOR A $500")
print("")
num = int(input("INGRESE MONTO: $"))

if (num > 500):
    print("El 18 ES: $",num * 0.18)