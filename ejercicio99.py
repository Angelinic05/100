#calcular el monto a pagar por la compra de teclados, el precio varia segun su cantidad
cantidad = int(input("INGRESE CANTIDAD A COMPRAR: "))
if cantidad in range(1,4):
    costo = 15
elif cantidad in range(4,9):
    costo = 11
else:
    costo = 10

print("COSTO POT TECLADO: S/",costo)
print("TOTAL A PAGAR: S/",(costo * cantidad))
