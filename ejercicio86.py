#algoritmo que ingrese un numero del 1 al 7 y muestra que dia de la semana es
dia = int(input("INGRESE DIA [1-7]: "))

if (dia == 1):
    print("LUNES")
elif (dia == 2):
    print("MARTES")
elif (dia == 3):
    print("MIERCOLES")
elif (dia == 4):
    print("JUEVES")
elif (dia == 5):
    print("VIERNES")
elif (dia == 6):
    print("SABADO")
elif (dia == 7):
    print("DOMINGO")
else:
    print("Dia invalido")
