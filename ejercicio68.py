#algoritmo qu calcule el salario a pagar de un trabajador
sueldobase = 0
num_hijos = 0
dias_no_lab = 0
sueldo_final = 0
print("Calcular el sueldo final de un empleado: ")
print("")
sueldobase = float(input("Ingrese sueldo base: $"))
num_hijos = int(input("Ingresar numero de hijos: "))
dias_no_lab = int(input("Ingresar Dias no Laborales Trabajados: "))

sueldo_final = sueldobase + (num_hijos * 100) + (dias_no_lab * 25)

print("")
print("SUELDO FINAL: $",sueldo_final)