#Dibuja un triangulo equilatero de numeros en secuencia
num = 0
val = 0
contador = 1
print("MUESTRA GRAFICA DE NUMEROS COMO TRIANGULO: ")
while  (num < 3):
    num = int(input("INGRESE NUMERO: "))
for x in range(1,num+1,1):
    espa = ""
    for z in range(1,(num+1)-x,1):
        espa = (espa + " ")
    print(espa)
    contador = 1
    for f in range(1,val,1):
        print(contador, end=' ')
        if(contador == 9):
            contador = 0
        else:
            contador = contador + 1
    val = val + 2