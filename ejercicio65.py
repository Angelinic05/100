#algoritmo que muestre el area y volumen de un cilindro
r = float(input("RADIO: "))
h = float(input("ALTURA: "))
a = 2 * 3.1416 * r * (h + r)
v = 3.1416 * (r * r) * h
print("AREA TOTAL DEL CILINDRO ",a," cm2")
print("VOLUMEN DEL CILINDRO ",v," cm3")