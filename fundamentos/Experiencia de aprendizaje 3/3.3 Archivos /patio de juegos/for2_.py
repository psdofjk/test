diccionario = {"juan":23,"alberto":24,"fuguet":25}
algo = {i: diccionario[i] for i in diccionario}
print(algo)

datos_personales = [("e",2),("e",3)]
edades_unicas = {(i,j) for i, j in datos_personales}
print(edades_unicas)
edades_unicas = {i for j,i in datos_personales}
print(edades_unicas)

nombres = ["Juan", "María", "Pedro"]
edades = [25, 30, 25]
datos_personales = zip(nombres, edades)
conjunto_datos_personales = {(nombre, edad) for nombre, edad in datos_personales}
print(conjunto_datos_personales)