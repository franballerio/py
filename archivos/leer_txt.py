text = open("archivos\\texto.txt", encoding="UTF-8") 
# print(text.read()) # asi leemos el texto que tiene el archivo

print(text.readline()) # nos muestra la primer linea del archivo
# y si le pasamos un numero a la funcion, 
# nos lee (num) cantidad de caracteres de la primer linea

# print(text.readlines()) nos muestra un array con todas las lineas del archivo

# para volver a operar con el archivo en el mismo programa, hay q cerrarlo
text.close() # esto cancela la funcion open, y si queremos operar con el archivo
# hay q abrirlo denuevo
# o lo q podemos hacer es guardar como variables los datos q necesitamos

# ejemplo
text = open("archivos\\texto.txt", encoding="UTF-8") 
# necesitamos la linea 20
lin20 = text.readlines()[20]
print(lin20)
# entonces sacamos la linea 20 y cerramos el archivo
text.close()
# y ahora podemos operar igual con la linea 20 sin abrir el archivo otra ve
print(lin20.split())