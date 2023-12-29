#algoritmo que calcule el monto a pagar por 10 compras realizadas
total = 0
desc = 0
for i in range(1,10,1):
    consumo = float(input(f"CONSUMO {i} : $"))
    total = total + consumo
if(total > 50):
    desc = total * 0.07
print("CONSUMO TOTAL: $",total)
print("DESCUENTO: $",desc)
print("PAGO TOTAL: $",(total-desc))    