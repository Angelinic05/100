#algoritmo que al ongresar las horas, minutos y segundos calcule el costo total
H = int(input("HORAS: "))
M = int(input("MINUTOS: "))
S = int(input("SEGUNDOS: "))

costo = ((H * 3600) + (M * 60) + S) * 0.25

print("COSTO TOTAL: ",costo)
