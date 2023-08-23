# list() --> crea una lista

lista = [1,2]
lista.append("elemento") # agrega al final
lista.insert(0,"jaja") # agrega en el indice 
# q quieras, y si hay uno en ese lugar lo corre
lista.extend([2,0.1,12,1.2,10,"jiji"]) # agrega una 
# lista a la lista
print(lista)
print(len(lista))
lista.pop(3) # elimina el elemen 3
lista.pop(-1) # elimina el ultimo, -2 el pen, etc
print(lista)
print(len(lista))
lista.remove("jaja") 
lista.sort() # solo anda si hay numeros o bool
# .sort(reverse=True) lo ordena al reve
print(lista)
lista.reverse() # la da vuelta

lista.index("elemento") # busca el elemen
# y devuelve el indice

