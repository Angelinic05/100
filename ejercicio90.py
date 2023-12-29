#algoritmo que muestre las cuatro operaciones basicas
num1 = int(input("NUMERO 1: "))
num2 = int(input("NUMERO 2: "))

operador = int(input("[1 +][2 -][3 *][4 /]: "))

if (operador == 1):
    print("SUMA: ",(num1 + num2))
elif (operador == 2):
    print("RESTA: ",(num1 - num2))
elif (operador == 3):
    print("MULTIPLICACION: ",(num1 * num2))
elif (operador == 4):
    print("DIVISION: ",(num1 / num2))
else:
    print("OPERADOR INCORRECTO")