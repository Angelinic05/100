#algoritmo que calcula el total de ventas realizadas por hombres y mujeres de n empleados
tv_h = 0
tv_m = 0
muj = 0
empleados = int(input("CANTIDAD DE EMPLEADOS: "))
print("")

for cont in range(1,empleados+1,1):
    print(f"Empleado Nro {cont} / ",empleados)
    nom = input("NOMBRE: ")
    genero = input("GÉNERO (H/M): ")
    ventas = int(input("VENTAS: "))
    print("")

    if ( genero == "H"):
        tv_h = tv_h + ventas
    else:
        tv_m = tv_m + ventas
        muj = muj + 1

print("TOTALK DE VENTAS HOMBRES: ",tv_h)
print("TOTALK DE VENTAS MUJERES: ",tv_m) 
print("")
print("PORCENTAJE DE MUJERES: ", (muj * 100)/empleados,"%")
