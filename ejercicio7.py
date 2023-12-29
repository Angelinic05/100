#muestra una serie grafica de numeros del 9 al 1 en forma triangular
for i in range(1,10,1):
    s = 0
    serie = 0
    for j in range(1,10-i,1):
        s = 10 - i
        serie = (serie * 10) + s
    print(serie)