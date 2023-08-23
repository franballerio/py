# los elementos iterables son listas, tuplas, diccionarios, sets, strings....

zoo = ["perro", "gato", "cocodrilo", "jirafa", "buitre"]
granja = ["vaca", "caballo", "pez", "chancho", "gallina"]

for animal in zoo:
    if animal == "jirafa":
        print("Hay jirafas en el zoo")
        break
# animal es una variable que se crea con el for
# y cambia de valor segun lo que queramos hacer

# ahora para iterar dos listas distintas al mismo tiempo
# primero tienen que tener la misma cant de elemen
for animales_de_zoo,animales_de_granja in zip(zoo, granja):
    #zip me permite unir las posiciones de ambos arrays
    if animales_de_zoo.endswith("a"):
        print(f"en el zoo hay una {animales_de_zoo}")
    else: 
        print(f"en el zoo hay un {animales_de_zoo}")
    if animales_de_granja.endswith("a"):
        print(f"en la granja hay una {animales_de_granja}")
    else: 
        print(f"en la granja hay un {animales_de_granja}")
# esto itera primero un elemen de zoo, y despues uno de granja y asi sucesivamente
# tambien lo podemos hacer con mas de dos listas

# ahora el in range
for num in range(8,10): # esto itera con numeros del 0 hasta el 
    print(num)   # (en 10 termina osea q no lo cuenta), y si le damos uno antes que el 10, 
                 # arranca con ese

# ahora podemos pedir que recorra la lista y nos indique que indice tiene cada valor
for i,animal in enumerate(zoo):
    print(f"- La posicion es {i} y el elemento es {animal}")
else: 
    print("- No hay mas animales")
    # asi desempaquetamos la tupla que crea el enumerate()
# y al final del for, podemos agregar un else, q se ejecuta cuando el bucle ya termino    
# a menos que haya un break antes del else

# todo esto funca igual para las tuplas, pero no para los diccionarios