#algoritmo que muestra todos los numeros que eson capicua de 3 cifras 

c = 0
r = 0
c1 = 0
r1 = 0
for f in range(100,999+1,1):
    c = (f-(f % 100))/100
    r = f % 100
    c1 = (r-(r % 10))/10
    r1 = r % 10
    if (f == ( (r1*100) + (c1*10) + c ) ):
        print (f, " ")
print("")