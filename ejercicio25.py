#algoritmo que muestre la serie: 1 + 2/3 + 3/5 + 4/7
n = int(input("VALOR DE N: "))
suma = 1
d = 3
if (n > 1):
    print(suma," + ")
    for i in range(2,n+1,1):
        if(i == n):
            print(i,"/",d)
        else:
            print(i,"/",d," + ")
        suma = suma + (i/d)
        d = d + 2
print("")
print("La suma es: ",suma)