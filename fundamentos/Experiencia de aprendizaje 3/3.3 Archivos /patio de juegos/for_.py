num = 10
numeros_primos = {num for num in range(10) if num >= 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))}
print(numeros_primos)

#2,3,5,7

numeros_primos = {num for num in range(10) if num > 1 and all(num % i != 0 for i in range(2,10))}

datos_personales = [("juan",23),("alberto",24),("pepe",23)]

edades_unicas = {pap for pap, pap in datos_personales}
edades_unicas2 = {edad for edad in datos_personales}

print("Edades únicas presentes:", edades_unicas)
print(edades_unicas2)

diccionario = {"juan":23,"alberto":24,"fuguet":25}
algo = {i:i for i in diccionario}
print(algo)
algo = {i for i in diccionario if i == "juan"} # este funciona bien
print(algo)
algo = [i for i in diccionario] #ni idea como llamar las llaves
print(algo)

lista = ["juan",23,"alberto","fuguet",25]
algo = [i for i in lista]
print(algo)

matriz = [["juan",23],["alberto",24],["fuguet",25]]
algo = [i for i in matriz]
print(algo)

listadetuplas = [("juan",23),("alberto",24),("fuguet",25)]
algo = [i for i in listadetuplas]
print(algo)
