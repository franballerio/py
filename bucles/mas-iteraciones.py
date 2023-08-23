# hacemos un modelo que agarra pelis y sus generos 
# y te dice el genero, la pelicula 
# y si esta bueno que la veas


peliculas = {
    "barbie" : "comedia",
    "ken" : "accion",
    "scari movi" : "comedia",
    "kun fu panda" : "dibujitos",
    "american pie" : "porno",
    "american pie2" : "porno",
    "toy sotry" : "dibus"
    
}

for i,tup in enumerate(peliculas.items()):
    tit, gen = tup
    if gen == "porno":
        print(f" - La peli es {tit} de genero +18")
        print (f" ¡ No recomendamos ver {tit} si sos menor de 18 años !")
    else:
        print(f" - La peli es {tit} de genero {gen}")    
        


# ahora podemos usar for en una sola linea
numeros = [2,3,4,5,6,7,8]

numeros_negativos = [(-x) for x in numeros]
print(numeros_negativos)