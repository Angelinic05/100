#algoritmo que dibuje un triangulo con un caracter
alt = int(input("ALTURA DEL TRIANGULO: "))
caract = input("INGRESE UN CARACTER: ")
for i in range (1,alt+1,1):
    for j in range(1,(alt+1)-i):
        print(end=' ')
    for j in range(1,((i+1)*2)-1):
        print(caract, end=' ')
    print("")