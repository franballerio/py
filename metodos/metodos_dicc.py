dicc1 = {
    "nombre1": "Fran",
    "apellido1": "ballerio",
    "documento1": "45073850",
    "hobby1": "Hockey",
    "nombre2": "Pabo",
    "apellido2": "gonzales",
    "documento2": "293004",
    "hobby2": "hanbol",
    "nombre3": "Pepe",
    "apellido3": "gomes",
    "documento3": "238595",
    "hobby3": "Paddle"
}

print(dicc1.keys())  # muestra las claves, osea los de adleante
key1 = dicc1.get("apellido1")  # nos devuelve el valor de la key
# hace lo mismo que --> dicc1["apellido1"], pero si no existe lo que le paso,
# da error, en cambio el get da None
print(key1)

# .pop("key") borra ese elemento que le pasamos
dicc1.pop("documento2")

#el .items() hace el dicc iterable
dicc1_iter = dicc1.items() 
print(dicc1_iter)

# otro metodo es .clear(), que elimina todo
dicc1.clear()
print(dicc1)
