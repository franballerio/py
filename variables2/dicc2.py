diccio = dict(name="fb", apellido="balle",dni="45073850")
diccio2 = {("apellido", "surname"):"fernandes"}
# en un diccionario, las keys pueden ser 
# solo elementos no iterables, por ejemplo las tuplas
# o un frozen set

print(diccio)
print(diccio2)

# podemos crear un diccionario con las keys vacias
diccio3 = dict.fromkeys(["Numero 1", "Numero 2", "Numero3"]) # siosi hay q pasarle
# una lista de las keys que vamos a querer
# sino nos iterara el primer elemento que le pasemos
# ejemplo -->
diccio4 = dict.fromkeys("abcde") # a este le podemos pasar otro valor 
# e igualara el iterable a ese valor que le pasamos
diccio5 = dict.fromkeys(["valor1", "valor2"], "valor predet")
print(diccio3)
print(diccio4)
print(diccio5)
