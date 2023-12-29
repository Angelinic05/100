#Calcula las ganancias de una garita de control, con cada vehiculo que pasa
tarifa = 0
bus = 0
van = 0
micro = 0
man = 0
noc = 0
print("GANANCIAS DE UNA GARITA DE CONTROL")
print("----------------------------------")
cantidad = int(input("CANTIDAD DE VEHICULOS: "))
for cont in range(1,cantidad+1,1):
    print(">> TIPO DE VEHICULO Nro ",cont,"/",cantidad," : ")
    print("1. OMnibus, ")
    print("2. Minivan")
    print("3. Micro")
    tipo = int(input("OPCION: "))
    if (tipo == 1 ):
        tarifa = 13
        bus = bus + tarifa
    elif (tipo == 2 ):
        tarifa = 10
        van = van + tarifa
    elif (tipo == 3 ):
        tarifa = 8
        micro = micro + tarifa
    turno = input("TURNO (M/N): ")
    if (turno == "M"):
        man = man + tarifa
    else:
        noc = noc + tarifa
print("")
print("IMPORTE DE TURNO MAÑANA: ",man)
print("IMPORTE DE TURNO NOCHE: ",noc)
print("")
print("IMPORTE DE OMNIBUS",bus)
print("IMPORTE DE MINIVAN",van)
print("IMPORTE DE MICRO",micro)

