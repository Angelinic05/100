#algoritmo que muestre el sueldo a pagar de un empleado segun su categoria
bonificacion = 0
sueldo = float(input("Sueldo Base: S/"))
categoria = int(input("[1.A - 2.B - 3.C - 4.D]: "))

if ( categoria == 1):
    bonificacion = sueldo * 0.1
elif ( categoria == 2):
    bonificacion = sueldo * 0.2
elif ( categoria == 3):
    bonificacion = sueldo * 0.3
elif ( categoria == 4):
    bonificacion = sueldo * 0.4

print("BONIFICACION: S/",bonificacion)
print("SUELDO NETO: S/",sueldo + bonificacion)
