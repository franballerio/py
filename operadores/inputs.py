# el input pide un dato al usuario
name1 = input("Ingrese su nombre ")
name1 = name1.capitalize()

print(f"Te llamas {name1}")
# el input siempre devuelve un string

# si queremos usar numeros podemos hacer asi
num1 = int(input("Dame tu documento: "))
# o num1 = int(num1) o float(num1) que lo hace con coma
# entonces ahora podemos operar con ese dato como numero
print(num1*3)