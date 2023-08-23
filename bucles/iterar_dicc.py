dicc = dict(nombre="franb",apellido="ballerio",dni="45073850",hobby="joki")

for key,value in dicc.items():
    print(key, value)
# asi los pasa como separados, si le damos una sola
# variable al for, nos da una tupla --> (key : value)

# si queremos saltearnos algun valor, podemos usar continue
for i,key in enumerate(dicc.items()):
    v1, v2 = key
    if v2 == "franb":
        continue
    print(f"el {i+1} elemento es: {v1}")


