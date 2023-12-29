#algoritmo que dibuje un rombo de asteriscos
altura = int(input("Altura del rombo: "))

for i in range(1,altura+1,2):
    for j in range(1,(altura-i)//2 + 1):
        print(" ", end=' ')
    for j in range(1,i + 1,1):
        print("*", end=' ')
    print("")

for i in range((altura-2),0,-2):
    for j in range(1,(altura-i)//2 + 1):
       print(" ", end=' ') 
    for j in range(1,i + 1,1):
       print("*", end=' ') 
    print("")
