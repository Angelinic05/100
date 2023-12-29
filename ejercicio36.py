#sumatoria de 4/2 - 9/1 + 15/1 - 23/2 - 34/8 - 49/64
sumatoria = float(0)
v = 4
v1 = 5
v2 = 1
x = 2
x1 = 0.5
ope = "-"
print("MUESTRA SERIE DE NUMEROS: ")
print("")
n = int(input("VALOR DE N: "))

for i in range(1,n+1,1):
    if (1 != n):
        print(v,"/",x," ",ope," ",end=' ')
    else:
        print(v,"/",x," ",opr," ...",end=' ')
    if ( (i % 2) == 1):
        ope = "+"
        sumatoria = sumatoria + (v/x)
    else:
        ope = "-"
        sumatoria = sumatoria - (v/x)
    v = v + v1
    v1 = v1 + v2
    v2 = v2 + 1
    x = x * x1
    x1 = (x1 + x1)
print("SUMATORIA: ",sumatoria)