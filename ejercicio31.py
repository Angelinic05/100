#algoritmo que ingrese un refrán y muestre el numero de letras C,S,D,L,R y M que hay
import re
C = 0
S = 0
D = 0
L = 0
R = 0
M = 0
consonante = 0
refran = input("Ingrese el refrán: ")
refran = refran.replace(" ","")
print(refran)
for caracter in refran.upper():
    if caracter.isalpha():
        if (caracter == "C"):
            C = C + 1
        if (caracter == "S"):
            S = S + 1
        if (caracter == "D"):
            D = D + 1
        if (caracter == "L"):
            L = L + 1
        if (caracter == "R"):
            R = R + 1     
        if (caracter == "M"):
            M = M + 1     
    if (caracter != "A" and caracter != "E" and caracter != "I" and caracter != "O" and caracter != "U" ):
        consonante = consonante +1
print("CANTIDAD DE C:", C)
print("CANTIDAD DE S:", S)
print("CANTIDAD DE D:", D)
print("CANTIDAD DE L:", L)
print("CANTIDAD DE R:", R)
print("CANTIDAD DE M:", M)
print("CANTIDAD DE CONSONANTES: ",consonante)
                  
