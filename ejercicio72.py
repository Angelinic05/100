#algoritmo que simule un login o clave de acceso
ususario = input("INGRESE USUARIO: ")
clave = input("INGRESE CLAVE: ")

if (ususario == "ADMIN" and clave == "123456"):
    print("ACCESO PERMITIDO")
else:
    print("ACCESO DENEGADO")