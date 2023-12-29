#algoritmo que muestra el nombre y promedio del alumno con mejor nota 
xpro = 0
for i in range (1,5,1):
    nom = input("NOMBRE: ")
    pro = int(input("PROMEDIO: "))
    if (xpro < pro):
        xpro = pro
        xnom = nom
print("ALUMNO CON MAYOR NOTA: ",xnom)
print("PROMEDIO: ",xpro)        