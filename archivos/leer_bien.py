with open("archivos\\texto.txt") as txt: 
# asi le cambiamos la forma de invocar al archivo
    print("El archivo existe")
    print(txt.readlines()[10])
# esto lo que hace es: si el archivo existe
# lo abre y ejecuta las instrucines que le damos,
# y al finalizar cierra el archivo 
