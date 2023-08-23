# una persona promedio dice 2 palabras por segundo
# dalto habla un 30% mas rapido

# le pedimos un texto al usuario, contamos cuantas palabras tiene el texto
# vemos cuanto tardaria en decirlo, y si dura mas de un minuto lo matamos,
# finalmente vemos cuanto tardaria dalto

txt = input("Ingrese su frase favorita: ")
# print(txt)
txt = txt.replace(",", "")
# print(txt)
txt = txt.split(" ")  # hacemos una lista con cada paabra
# print(txt)
# print(len(txt))
cant_p = len(txt)
if cant_p > 120:
    print("Para hermano no me cuentes tu vida")

dalto = round(len(txt)/2.6, 2)
persona = round(len(txt)/2, 2)
print(f"son {cant_p} palabras")
print(
    f"Dalto lo diria en {dalto} segundos, mientras que una persona normal lo diria en {persona} segundos")
