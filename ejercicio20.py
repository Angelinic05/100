#algoritmo que busque un numero que se ha generado de forma aleatoria
import random
sw = 0
numA = random.randint(1,20)
for i in range(1,3+1,1):
    num = int(input("ENCUENTRE EL NUMERO [1 - 20]: "))
    if ( num == numA):
        print("NÚMERO ENCONTRADO")
    else:
        if ( num > numA):
            print("INGRESE UN NÚMERO MENOR")
        else:
            print("INGRESE UN NÚMERO MAYOR")
    print("")
if ( sw == 0):
    print ("EL NÚMERO A ENCONTRAR ERA: ",numA)
        