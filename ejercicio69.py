#algoritmo qiue muestra el porcentaje de almunos aprobados y desaprobados
print("MSOTRAR EL PORCENTAJE DE ALUMNOS APROBADOS Y DESAPROBADOS")
print("")
apro = float(input("INGRESE CANTIDAD DE ALUMNOS APROBADOS: "))
desa = float(input("INGRESE CANTIDAD DE ALUMNOS DESAPROBADOS: "))
print("")

pora = (apro * 100) / (apro + desa)
pord = (desa * 100) / (apro + desa)


print("APROBADOS: ",round((pora * 100)/100),"%")
print("DESAPROBADOS: ",round((pord * 100)/100),"%")