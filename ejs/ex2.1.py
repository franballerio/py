# falto el profe y hay que organizar la clase
# pedir nombre y edad de los alumnos
# que vinieron hoy a clase, siendo el mas grande
# el profe y el menor el asistente

alumnos = []
cant_alumnos = 0
cant_alumnos = input("Ingrese cantidad de alumnos ")
cant_alumnos = int(cant_alumnos)

if cant_alumnos > 0:
    for alum in range(int(cant_alumnos)):
        alum = input("Ingrese nombre y apellido, edad: ")
        alum = list(alum.split(","))
        alum[1] = int(alum[1])
        alumnos.append(alum)
    alumnos.sort(key=lambda x: x[1]) # esto ordena la lista segun 
    # el 2do elemento de cada elemento de la lista, porq la lista es de la forma
    # alumnos = [[nombre, edad],[nombre, edad]]
    # alumnos = sorted(alumnos, key=lambda x: x[1]), hace lo mismo
else:
    print("Faltaron todos boludooo")
print(
    f"Entonces el profesor suplente fue {alumnos[-1][0]} y el ayudante fue {alumnos[0][0]} ")
print(alumnos)

# soy un crack
