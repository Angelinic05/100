#algoritmo que muestre el triangulo de pascal
print("MOSTRAR EL TRIANGULO DE PASCAL")
n = int(input("INGRESE DIMENSION [MAS O IGUAL A 20]: "))

# Inicializar la matriz m
m = [[0] * (n + 1) for _ in range(n + 1)]
print (m)

# Llenar la matriz con los valores del Triángulo de Pascal
for i in range(n + 1):
    m[i][0] = 1
    for j in range(1, i + 1):
        m[i][j] = m[i - 1][j - 1] + m[i - 1][j]

# Mostrar el Triángulo de Pascal
for i in range(n + 1):
    espacios = " " * (n - i)
    print(espacios, end=' ')
    for j in range(i + 1):
        val = m[i][j]
        if val != 0:
            print(val, end=' ')
    print()
