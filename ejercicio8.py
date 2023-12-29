#algoritmo que muestre la serie grafica de numeros 123456789 en forma decreciente
for i in range(1,10,1):
    serie = 0
    for j in range(1,10-i,1):
        serie = serie * 10 + j
    print (serie)