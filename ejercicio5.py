#serie fibonacci
a = 0
b = 1
c = 0
for i in range (1,11,1):
    print(c," ")
    a = b
    b = c
    c = a+b
