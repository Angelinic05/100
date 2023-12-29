#algoritmo que muestre todos los numeros que esten en el rango de a y b
a = int(input("NUMERO A: "))
b = int(input("NUMERO B: "))
if (a < b):
    for i in range(a+1,b,1):
        print(i)
else:
    for i in range(b+1,a,1):
        print(i)