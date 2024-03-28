a = 100
b = 100

#for i in range(a):
#    for j in range(b):
#        print("*", end="")
#
#    print()


#bucles de variable declarativa
#while True:
#    valor = input("variable: ")
#    try:
#        valor = int(valor)
#        break
#    except ValueError:
#        print("porfavor introduce un int")

#bucles de numeros
#while True:
#    opcion = input("elige 1: ")
#    if opcion == "1":
#        opcion =  int(opcion)
#        break 
#    else:
#        print("elige 1 puta: ")

#mezclar los 2
while True:
    opcion = input("elige 1: ")
    if opcion == "1":
        try:
            opcion = int(opcion)
            break
        except ValueError:
            print("porfavor elige 1")