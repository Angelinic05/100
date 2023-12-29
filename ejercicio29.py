#Cantidad de numeros pares e impares 
sumaP = 0
sumaI = 0
num = int(input("INGRESE NÚMERO: "))
for x in range(1,num+1,1):
    if (x % 2) == 0:
        sumaP = sumaP + x
    else:
        sumaI = sumaI + x
print("Suma de pares: ",sumaP)
print("Suma de impares: ",sumaI)
        