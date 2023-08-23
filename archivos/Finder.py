import pandas as pd

df = pd.read_csv("/home/franb/Codin/python/dalto/archivos/datas3.csv")

# ahora buscamos todas las personas que sean menores de 29
mayores_30 = df.loc[df["Age"]>=30,:] 
# esto lo que hace es evaluar solo la parte que le pasamos de cada fila del df
# osea va a la edad de cada persona y nos pása la fila entera si 
# edad >= 30
print(mayores_30)


# ponele ahora nos va a decir solo el nombre
name_mayores_30 = df.loc[df["Age"]>=30,"Name"]
#name_mayores_30_2 = df.iloc[df["Age"]>=30,0]
print(name_mayores_30)
