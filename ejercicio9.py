#algoritmo que muestre la grafica de asteriscos
xn = 7
for f in range(1,7,1):
    serie = ""
    if f >= 5:
        xn = xn + 2
    for c in range (1,xn-f,1):
        serie = (serie + " * ")
    print(serie)