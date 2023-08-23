# creamos un set o conjunto

conj = set(["dato1", "dato2"])
# no le podemos meter listas o dicc,
# ya que pueden modificarse, solo podemos meterle
# al set tuplas

# los sets son conjuntos desordenados

conj.add(("datoentup1", "datoentup2"))
print(conj)
conj.discard("dato1")  # eliminamos un elemento del set
# y si no lo encuentra, no da error
print(conj)

# conj2 = set([conj, "tupla", ("datotu1", "datotu2")])
# no se puede, pero si hacemos -->
conj = frozenset(["dato1", "dato2"])
conj2 = {conj, "tupla", ("datotu1", "datotu2")}
print(conj2)
# lo que hace frozenset es congelar el conj, para poder
# hacer operaciones de union etc sin modificarlo directamente
# en este caso conj es un subconjunto de conj2,
# o conj2 es un superconjunto de conj,
# ylo verificamos con estas funciones

conj = {1,3,4,5,9}
conj2 = {1,3,4,5,9,10,1.4,1/2,3.14}
conj3 = {100, 200, 2.4}

print(conj.issubset(conj2)) 
# devuelve True porque todos elementos de conj existen en conj2
# con esta sintaxis verificamos lo mismo --> conj <= con2
print(conj2.issuperset(conj))
print(conj < conj2) 
# aca preguntamos si conj2 es superconjunto de conj

# con .isdisjoint(), vemos si no hay ninguna igualdad entre conj,
# y si hay x lo menos una --> nos da false
print(conj.isdisjoint(conj2))
print(conj.isdisjoint(conj3))
