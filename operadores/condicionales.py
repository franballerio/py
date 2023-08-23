# condicionales: si algo pasa pedimos que pase algo, sino pedimos otra cosa

juegos = ["Mortal Kombat", "Pacman", "Fifa22", "call of duty"]

pelis = ["toy story", "cars", "chuky",]


if "Mortal Kombat" or "call of duty" in juegos:
    # si el nombre de un videojuego está en la lista
    print("No los puede jugar tu nene")
else:
    print("Los puede jugar tu nene")


if "chuky" in pelis:
    print("No las puede ver tu nene")
elif "american pie" in pelis:
    print("No las puede ver tu nene")
else:
    print("Las puede ver")

# a los condicionales 
# se le pueden sumar los operadores logicos
& # and
| # or
not # negación