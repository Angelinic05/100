#algoritmo que muestra los numeros primos de 1 hasta n
divisible = 0
num = int(input("INGRESE UN VALOR: "))
for cont in range(2,num+1,1):
    for divi in range(1,cont+1,1):
        if ( (cont % divi) == 0):
            divisible = divisible +1
    if (divisible == 2):
        print(cont)
    divisible = 0
print("")