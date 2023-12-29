#algoritmo que muestre el suelo de un trabajador
boni = 0
sueldof = 0
print("09. CALCULAR EL SUELDO FINAL")
nom = input("INGRESE NOMBRE: ")
sueldoB = float(input("Sueldo basico: S/."))
hijos = int(input("Nro Hijos: "))

if (hijos > 0):
    boni = round(sueldoB * 0.7)

sueldof = sueldoB + boni
print("")
print("BONIFICACION: S/.",boni)
print("SUELDO FINAL: S/.",sueldof)

