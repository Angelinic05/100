#algoritmo que calcule el igv si el monto de compra es mayor a $100 usa
igv = 0
monto = 0
print("05. CALCULAR IGV SEGUN EL MONTO DE COMPRA")
precio = float(input("INGRESE PRECIO: S/."))
cant = int(input("INGRESE CANTIDAD: "))

monto = (precio * cant)

if (monto > 100):
    igv = monto * 0.18

print("")
print("TOTAL            : S/",monto)
print("IGV 18%          : S/",igv)
print("TOTAL A PAGAR    : S/",(monto + igv))