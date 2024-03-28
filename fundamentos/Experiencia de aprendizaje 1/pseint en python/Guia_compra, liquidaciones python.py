#Ejercicio 1

valor_compra = int(input("Ingrese valor de compra: "))
liquidacion = str(input("Hay Liquidacion(Si/No): "))

if valor_compra < 100000 and liquidacion == "no":
    print("valor compra: ", valor_compra)
    print("Descuento: 0")
    print("Toal a pagar: ", valor_compra)

elif valor_compra < 100000 and liquidacion == "si":
    desc_liquidacion = valor_compra * 0.05
    total_final = valor_compra - desc_liquidacion
    print("valor compra: ", valor_compra)
    print("Descuento: ", desc_liquidacion)
    print("Total a pagar: ", total_final)

elif 100000 < valor_compra < 500000 and liquidacion == "no":
    descuento = valor_compra * 0.1
    total_final = valor_compra - descuento
    print("valor compra: ", valor_compra)
    print("Descuento: ", descuento)
    print("Total a pagar: ", total_final)

elif 100000 < valor_compra < 500000 and liquidacion == "si":
    descuento = valor_compra * 0.1
    total_compra = valor_compra - descuento
    desc_liquidacion = total_compra * 0.05
    descuento_total = descuento + desc_liquidacion
    total_final = valor_compra - descuento_total
    print("valor compra: ", valor_compra)
    print("Descuento: ", descuento_total)
    print("Total a pagar: ", total_final)

elif 500000 < valor_compra and liquidacion == "no":
    descuento = valor_compra * 0.2
    total_final = valor_compra - descuento
    print("valor compra: ", valor_compra)
    print("Descuento: ", descuento)
    print("Total a pagar: ", total_final)

elif 500000 < valor_compra and liquidacion == "si":
    descuento = valor_compra * 0.2
    total_compra = valor_compra - descuento
    desc_liquidacion = total_compra * 0.05
    descuento_total = descuento + desc_liquidacion
    total_final = valor_compra - descuento_total
    print("valor compra: ", valor_compra)
    print("Descuento: ", descuento_total)
    print("Total a pagar: ", total_final)

elif liquidacion != "si" or liquidacion != "no":
    print("Respuesta no disponible, solo se puede responder si o no.")