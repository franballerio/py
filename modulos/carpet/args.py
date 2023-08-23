# los args son parametros basicamente infinitos xd

def suma(*num): # lo que hace es meterlos es una lista y con ella
# podemos operar, pero no podemos poner ningun argumento mas en la funcion 
# despues del arg
    return sum(num)

resu = suma(1,4,7,9,1,5,10)
print(resu)
