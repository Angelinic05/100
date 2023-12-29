#algoritmo que calcule la bonififcacion a pagar
print("O4. CALCULAR BONIFICACION")
print("")
venta = float(input("INGRESE MONTO DE VENTA: $."))
if ( venta > 2000):
    print("BONIFICACION 10%: $.",(venta * 0.1))
else:
    print("BONIFICACION 50%: $.",(venta * 0.5))
