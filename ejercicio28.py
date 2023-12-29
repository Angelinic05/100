#algoritmo qu emuestra si un numero es primo
divisi = 0
num = int(input("INGRESE NÚMERO: "))
for i in range(1,num+1,1):
    if (num % i) == 0:
        divisi = divisi + 1
if (divisi == 2):
    print("NÚMERO PRIMO")
else:
    print("NO ES PRIMO")
                