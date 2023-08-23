# now we are creating functions
# son basicamente pedazos de codigo que podemos reutulizar en
# cualquier parte del codigo

# por ejemplo bool
 
# bool() --> nos devuelve false si le damos algo igual a cero,
# none o algun valor vacio

# all() --> comprueba si todos los elementos del iterable que le 
# pasamos existen o son validos o son 0

#  ahora asi creamos nuestras funciones 
# con parametros 

def saludar(nombre, sexo):
    sexo = sexo.lower()
    
    if (sexo == "mujer" or sexo == "femenino"): 
        print(f"Hola reina {nombre}")
    elif (sexo == "hombre" or sexo == "masculino"):
        print(f"Como andas {nombre}")
    else:
        print(f"Como andas {nombre} bebe")

def contraseña_aleat(num):
    numm = str(num)
    numm = numm[0]
    numm = int(num)
    chars = "fueifbcouebcOIUEWNuiecCUIQCUQICNQUauhadjajdOJAJDJWOnoawinwoafjakdwmvaoinaownaoudjoOANCUBUIE"
    a1 = numm + 4
    a2 = numm
    a3 = numm**2
    contra = f"{a2}{chars[a3]}{chars[a2]}{chars[a1]}{a1}{a3}"
    return(contra)
    
contra = contraseña_aleat(6)
print(contra)  



def frase(nombre,apellido,legusta = "la japi"):
    return (f"A {nombre} {apellido}, le gusta {legusta}")

fra1 = frase("carlos", "vargas", legusta="el futbol")
fra2 = frase(apellido="Borges", nombre="Jorge")
# esto se llaman keyword parameters
print(fra1)
print(fra2)