#algoritmo que muestre el area y perimetro de un trapecio
print("AREA DEL TRAPECIO")
B = float(input("BASE MAYOR: "))
Bb = float(input("BASE MENOR: "))
h = float(input("ALTURA: "))

A = ((B * Bb) * h)/2
print("AREA: ",A, "cm2")
print("")
print("PERIMETRO DEL TRAPECIO")
l1 = float(input("LASO 01: "))
l2 = float(input("LASO 02: "))
l3 = float(input("LASO 03: "))
l4 = float(input("LASO 04: "))

P = l1 + l2 + l3 + l4
print("PERIMETRO: ",P," cm2")