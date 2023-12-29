#algoritmo que calcule el costo de una llamada telefonica
llamada = int(input("CANTIDAD DE MINUTOS: "))

if(llamada <= 5):
    costo = llamada * 0.9
else:
    costo = (5 * 0.9) + ((llamada - 5) * 1.1)

print("EL COSTO ES: S/.",costo)