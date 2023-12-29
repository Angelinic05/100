#ALGORITMO QUE MUESTRA EL TOTAL A PAGAR POR UN PRESTAMO DE BANCO
monto = 100
meses = int(input("Nro de meses: "))
intereses = (monto * (meses * 0.02))
totalp = monto + intereses

print("INTERESES: ",intereses)
print("TOTAL A PAGAR: ",totalp)