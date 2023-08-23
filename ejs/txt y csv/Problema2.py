import pandas as pd

df = pd.read_csv("/home/franb/Codin/python/dalto/archivos/datas3.csv")


# print(df)

# cambiando los datos de una columna

df[["Name", "Surname"]] = df["Name"].str.split(
    " ", n=1, expand=True)  # con este metodo separamos
# la col name en Name y Surname
# y asi movemos a surname a la 2da pos
df = df[["Name", "Surname", "Age", "Email", "Id"]]

# print(df)
# y ahora le cambiamos el nombre a David
df["Name"].replace("David", "Maria", inplace=True)
# xq se hizo mujer
print(df)
print("------------")

# ahora le agregamos manualmente filas con cosas en blanco, asi las podemos eliminar o completar
df = df.dropna()# adentro le podemos pasar el parametro axis=
# donde 0 son las filas y 1 las columns
print(df)

# eliminar las filas repe
df = df.drop_duplicates()
print(df)
print("------------")
# creando un df nuevo y limpito

df.to_csv("archivos/datas3_limpio.csv")

