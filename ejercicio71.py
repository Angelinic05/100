#algoritmo que muestre si un numero es par o impar
num = int(input("INGRESE NUMERO: "))

c = round(num/2)
r = c * 2
re = num - r

if (re == 0):
    print("NUMERO PAR")
else:
    print("NUMERO IMPAR")  