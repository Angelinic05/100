#algoritmo que muestre el total a pagar por la compra de teclados 
cantidad = int(input("Cantidad a comprar: "))

if cantidad in range (1,4):
    costo = 15
elif cantidad in range(4,9):
    costo = 11
else:
    costo = 10

print("Costo por teclado: S/",costo)
print("Total a pagar: S/",costo * cantidad)
