# una variable es un espacio que guardamos en la memoria,
# y que puede variar a lo largo del programa

nombre = "pedro"

print(nombre)  # imprime el valor de la variable en pantalla
# se puede operar dentro de las variables

numero = 1
numero -= 1
numero += 100
print(numero)
# a la variable numero le restamos uno y le sumamos 100

bienvenida = "Hola " + nombre + " todo bien?"
print(bienvenida)

bienv2 = f"hola {nombre} todo bien?"  # se llama f string
# porque agarra un dato y lo pasa a string,
# si nombre no fuese un string,
# bienvenida daria error y bienv2 no
print(bienv2)

# con del eliminamos datos
del nombre  # elimina nombre,
# pero como esta al final de todo las variables que lo usaron
# ya tienen su valor con "nombre"
# print(nombre) nos da error, porque nombre no existe mas

if "fran" in bienvenida:
    print("Bienvenido fran")
else:
    print("Donde esta fran")
# busca lo que le pedimos dentro de la variable
if "Pedro" not in bienvenida:
    print("Donde esta Pedro")
else:
    print("Hola pedo")
