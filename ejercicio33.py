#Ingresar una frase y mostrar la cantidad de vocales que contiene
import re
a = 0
e = 0
i = 0
oo = 0
u = 0
consonante = 0
frase = input("Ingrese el frase: ")
frase = frase.replace(" ","")
print(frase)
for caracter in frase.upper():
    if caracter.isalpha():
        if (caracter == "A" or caracter == "Á"):
            a = a + 1
        if (caracter == "E" or caracter == "É"):
            e = e + 1
        if (caracter == "I" or caracter == "Í"):
            i = i + 1
        if (caracter == "O" or caracter == "Ó"):
            oo = oo + 1
        if (caracter == "U" or caracter == "Ú"):
            u = u + 1    
print("CANTIDAD DE A:", a)
print("CANTIDAD DE E:", e)
print("CANTIDAD DE I:", i)
print("CANTIDAD DE O:", oo)
print("CANTIDAD DE U:", u)
