#Algoritmo que calcule el iva del monto total a pagar
print("")
costo = float(input("Costo de la casa: S/"))
iva = float(input("Valor del IVA: %"))
print("")

totpagar = costo + (costo * (iva / 100))
print("IVA DE ",iva,"%: S/",(costo * (iva / 100)))
print("TOTAL A PAGAR: S/",totpagar)
