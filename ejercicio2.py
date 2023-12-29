#algoritmo que muestra la cantidad de numeros pares e impares ingresados 
par = 0
impar = 0
for i in range (1,10,1):
    num = int(input(f"Número {i} : "))
    if (num % 2) == 0:
        par = par+1
    else:
        impar = impar+1  
print("Cantidad de pares: ",par) 
print("Cantidad de impares: ",impar) 

