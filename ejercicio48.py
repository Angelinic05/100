num = int(input("INGRESE Nro. DE 3 CIFRAS: "))
cen = int((num - (num % 100))/100)
res = int(num % 100)
dec = int((res - (res % 10))/10)
uni = int(res % 10)

print("CENTENA: ",cen)
print("DECENA: ",dec)
print("UNIDAD: ",uni)