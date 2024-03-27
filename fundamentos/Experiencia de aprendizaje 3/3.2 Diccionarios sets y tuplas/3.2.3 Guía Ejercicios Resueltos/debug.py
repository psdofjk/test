diccionario = {}
palabras = ["pepe", "papo", "pepe","alberto"]
pepe = ["alberto"]

for i in palabras:
    i = i.lower()
    diccionario[i] = diccionario.get(i, 0) + 1

diccionario["alberto"] = diccionario.get("alberto",0) + 1

for i in pepe:
    diccionario[i] = diccionario.get(i, 0) + 1

juan = ["ronaldo"]
juancito = {}
for i in juan:
    juancito[i] = juancito.get(i, 0) + 2
print(juancito)

print("Frecuencia de palabras:")
for i, j in diccionario.items():
    print(f"{i}: {j}")

