#algoritmo que muestra el factorial de un numero ingresado
fact = 1
num = int(input("FACTORIAL A CALCULAR: "))
for i in range(1,num+1,1):
    print (((num+1)-i), "")
    fact = fact * i
print("")
print("EL FACTORIAL ES: ",fact)
print("")