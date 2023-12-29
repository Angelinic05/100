#algoritmo que muestra si un numero es o no capicúa
n = int(input("INGRESE NÚMERO: "))
num = n
test_num = 0 
while (num > 0):
    rest = num % 10 
    test_num = (test_num * 10) + rest
    num = num // 10
print("")
print("NÚMERO INGRESADO: ",n)
print("NÚMERO CAMBIADO: ",test_num)
print("")
if (n == test_num):
    print("SI ES UN NÚMERO CAPICÚA")
else:
    print("NO ES UN NÚMERO CAPICÚA")

