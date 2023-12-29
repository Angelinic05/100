#algoritmo que muestre el descuento a pagar segun el monto de compra en un supermercado
import os
import random
desct = 0
compra = 0
compra = float(input("VALOR DE COMPRA: S/"))
os.system("pause")
color = random.randint(0,5)
if (color == 1):
    print("COLOR: BLANCO")
    desct = 1
elif (color == 2):
    print("COLOR: VERDE")
    desct = 0.5
elif (color == 3):
    print("COLOR: NEGRO")
    desct = 0.4
elif (color == 4):
    print("COLOR: CELESTE")
    desct = 0.5
elif (color == 5):
    print("COLOR: ROJO")
    desct = 0
print("DESCUENTO: S/",desct)
print("IMPORTE DESCT: S/",compra * desct)
print("PAGO FINAL: S/",compra - (compra * desct))

