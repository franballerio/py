# listas
cosas = ["cacaa", 2, 15, False, 10.10]  # o tambien array
print(cosas)
print(cosas[0])  # el primer elemen, tiene indice cero
print(cosas[1:4])  # mustra los elementos de indice 1,2,3
print(cosas[2])
cosas[2] = "pedrito"  # modifica el valor del indice 2
print(cosas)
print(cosas[2])
if "pedrito" in cosas:
    print("aparecio pedrito")
    cosas[3] = "carlito, el amigo de pedro"
print(cosas)

tupla = (1, 2, "wachin")  # se llama tupla,
# es una lista pero que no puede modificarse
print(tupla[1])

# ahora vemos los sets o conjuntos
cositas = {"cacaa", 2, 15, False, 10.10}
# los elementos de dentro tampoco pueden modificarse, y si se repiten
# solo aparece uno en la salida
# Y tampoco se puede llamar a sus elementos como en las listas

# diccionarios
dicc = {
    "nombre": "Fran",
    "apellido": "Ballerio",
    "dni": "45073850"
}
# esto es un diccionario, dnde cada clave tiene su valor
print(dicc["apellido"])
# print(dicc[0]) da error
print((dicc["nombre"] == "Fran") & (dicc["dni"] == "45073850"))
