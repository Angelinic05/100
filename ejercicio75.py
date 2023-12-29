#algoritmo que calcule el descuento a pagar segun el mongo de compra
monto = float(input("MONTO DE COMPRA: S/."))
if (monto >= 350):
    desct = monto * 0.35
    print("DESCUENTO ES DE 35%: S/.",desct)
else:
    desct = monto * 0.1
    print("DESCUENTO ES DE 15%: S/.",desct)

print("MONTO A PAGAR: S/.",(monto - desct))

