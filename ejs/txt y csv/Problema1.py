# concatenamos una lista con nombres y otra con apellidos

lis1 = ["Carlos", "Raul", "Saul", "Marco", "Carla", "Pedro"]
lis2 = ["Peres", "Perez", "caman", "Laurens", "Migueletes", "Gonzales"]

# lo metemos en un txt de forma optima


#with open("/home/franb/Codin/python/dalto/ejs/txt y csv/Names_Surnames.txt", "a", encoding="UTF-8") as txt:
#    txt.write("Los Nombres y Apellidos son:\n\n")
#    for i,y in zip(lis1, lis2): 
    # el zip hace q vaya primero al lis1[0]
    # y despues al lis2[0] y asi sucesivamente
#        txt.writelines(f"Nombre: {i}\nApellido: {y}")
#        if y in lis2:
#            txt.writelines("\n----------\n")


# pero podemos optimizar varias lineas de la sig manera:
with open("/home/franb/Codin/python/dalto/ejs/txt y csv/Names_Surnames.txt", "a", encoding="UTF-8") as txt:
    txt.write("Los Nombres y Apellidos son:\n\n")
    [(txt.writelines(f"Nombre: {i}\nApellido: {y}\n-----\n")) for i,y in zip(lis1,lis2)]
# para q el for en una linea ande, hay q poner todo adentro de []
