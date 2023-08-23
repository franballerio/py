# print()
# type() # dice que tipo de dato es

# que podemos hacer con los strings
cad1 = "la puuu, que hiciste"
cad2 = "QUE PASOOOO"
cad3 = "434223"
lis1 = ["pepe grillo", 3, 4, 10]
lis2 = [True, False]


print(cad1.upper())
print(cad2.lower())
print(cad2.capitalize())
print(cad1.capitalize())
print(cad1.find("que"))
print(cad1.index("que")) # es igual q find,
# solo que si no encuentra nada, da error 
# y find da -1

print(cad3.isnumeric()) # verifica que sea un numero,
# aunque sea un string
print(cad3.isalpha()) # verifica que sea alfanum,
# osea sin caract especiales ni espacios
cad3.count("4") # dice cuantas veces esta 
# lo que buscamos
len(lis1) # nos dice la cantidad de elemen q tiene

# .startswith("cadena") o .endsewith("cadena")
# ya entendemos q hace

cad3 = cad3.replace("5", "Se la comen") # reemplaza
cad3 = cad3.replace("4", "hola")
print(cad3)

print(cad2.split(" "))