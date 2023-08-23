# son funciones anonimas, asociadas a nada
# sirven para crear funciones simples con una sola instruccion
# ej:

# frase_pred = lambda x : f"Buen dia {x}"

# print(frase_pred("luquitas")


def es_par(num):
    if num % 2 == 0:  # el simobolo % en nums, nos da el resto de la div
        return True


# mira lo que hace filter
nums = [1, 2, 3, 4, 5, 6, 7, 8]

pares = filter(es_par, nums)  # es como un bucle y a cada elemen
# de la lista nums, lo usa de arg en es_par()


def cuales_son_pares(numes):
    numers = filter(es_par, numes)
    return numers


print(list(pares))

# ahora lo mismo con lambda, sin es_par()

pars = filter(lambda x: x % 2 == 0, nums)

print(list(pars))
