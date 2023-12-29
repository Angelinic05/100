#Algoritmo que muestra la tabla de multiplicarde cualquier número ingresado
num = int(input("ingrese numero: "))

for i in range(1,12,1):
    print(num," x ",i," = ", (num*i))