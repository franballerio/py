with open("archivos\\texto2.txt","a", encoding="UTF-8") as txt: 
    # con el permiso de a podemos agregar al archivo
    txt.write("jaja agregue lo mnismo \n") # esto borra todo lo del archivo y escribe lo q le pasamos
    txt.writelines(["Los teclados mecánicos superan a los normales \n",  
                    "con su retroalimentación táctil precisa, durabilidad de primera clase y opciones de personalización \n" 
                    "brindando una experiencia de escritura y juego excepcionalmente mejorada. \n"]) # nos pide una lista con todas las lineas del texto
#   PERO ACORDATE QUE PARA PONER PUNTO Y APARTE ERA /n