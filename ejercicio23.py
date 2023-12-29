#promedio de varias notas ingresadas
suma = 0
n = int(input("INGRESE LA CANTIDAD DE NOTAS: "))
for i in range(1,n+1,1):
    nota = int(input(f"NOTA {i} :"))
    suma = suma + nota
print ("PROMEDIO: ", suma/n)