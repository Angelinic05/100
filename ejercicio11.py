#algoritmo que muestre el producto de varios numeros ingresados
pro = 1
n = int(input("VALOR DE N: "))
for i in range(1,n+1,1):
    print(i, " ")
    pro = pro * i
print("")
print("PRODUCTO DE ",n," ES: ",pro)
