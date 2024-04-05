#PromedioNotas
sw = 1
listaNotas = []

print("Presione 1 para ingresar sus notas")
print("Presione cualquier tecla para salir")
op = int(input("Seleccione opción: "))
if (op == 1):
    while sw == 1:
        try:
            print("-------------------------------------------------------------")
            nota = int(input("Incorpore una nota, si desea salir, presione 0: "))
            if (nota != 0):
    #Codigo faltante --------------------------------------------------------------------
                listaNotas.append(nota)
                print("sus notas son:") 
                for i in listaNotas:    
                    print(i,end=" ")
                print(f"\nla lista tiene {len(listaNotas)} notas")
                print(f"El promedio de las notas es {round(sum(listaNotas)/len(listaNotas))}")
    #Codigo faltante --------------------------------------------------------------------
            else:
                print("Adiós!")
                sw = 0
        except:
            print("Ingreso Erróneo")
else:
    print("Adiós!")