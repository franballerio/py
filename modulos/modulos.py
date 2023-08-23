# un modulo es cualquier archivo q tiene .py
# desde un modulo podemos llamar a otros
# osea como ya creamos una funcion fibonacci en un modulo
# en este modulo lo podremos llamar de una manera

# lo hacemos asii
import modulo_saludar as md  # con el as lo que hacemos es
# cambiarle el nombre al namespace, asi lo podemos llamar
# de una manera mas facil
# importamos el nombre del modulo que queremos usar
# alu = md.saludo("Pedrito")
# print(alu)

# para no tener que importar todas las funciones de un modulo
# podemos usar el from e importar solo una

from modulo_saludar import saludo as sd, saludar_raro as srr
# y si queremos importar mas solo las agregamos dsp de una coma
print(sd("Caca"))
print(srr("Pedro"))

# para ver todas las opciones q tiene usamos el dir
print(dir(md))

# para acceder a modulos dentro de carpetas es asi
import carpet.args as fa

rsu = fa.suma(12341,54325,2,1244,14,1241) 
print(rsu)

# y si esta afuera de nuestra carpeta
import sys
print(sys.path)
sys.path.append('e:\\Codin\\python\\dalto\\functions')
# from functions import contraseña_aleat # aca nos tira error pero si pusimos bien el path no pasa nada, funca igual
# print(contraseña_aleat(5))