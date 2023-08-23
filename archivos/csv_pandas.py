import pandas as pd

# le ponemos df por dataframe
df = pd.read_csv("/home/franb/Codin/python/dalto/archivos/datas.csv")
df2 = pd.read_csv("/home/franb/Codin/python/dalto/archivos/datas2.csv")
# los dataframes son como hojas de calculo, no son el archivo datas
print(df)
# y podemos operar con ellos asi
# names = df["Name"]
# print(names)  # esto nos muestra la columna Names

# ahora ordenamos el df

sorted_df = df.sort_values(by="Id")
# y para ordfenarlo al reves
sorted_df_reverse = df.sort_values(by="Id", ascending=False)
# print(sorted_df_reverse)

# como concatenar los df
df_concat = pd.concat([df, df2])
print(df_concat)
# print(df_concat.head(2)) # muestra las 2 primeras filas del df
# print(df_concat.tail(2)) # muestra las ultimas 2 filas

# viendo cant de col y filas
df.shape  # nos da una tupla con cant de (filas, columnas)
filas, columnas = df.shape
print(f"El archivo tiene {filas} filas y {columnas} columnas")

# obteniendo estadisticas
# print(df.describe())


# accediendo a un elemento especifico
elemen = df.loc[2, "Age"]
elemen2 = df.iloc[2, 3]  # hace lo mismo q el de arriba
# el primer arg es el indice al q queremos acceder(en fila) y el segundo arg, la key o el indice
# de la columna
# print(elemen)
# print(elemen2)


# ahora accedemos a todas las filas (sin el for)
namess = df.loc[:, "Name"] 
names = df.iloc[:, 0]
# estos nos pasan todos los nombres, xq en fila pusimos ":" (q te da todos)
# y en columna pusimos una especifica
# print(namess)

# ahora accedemos a todos los datos de una fila
fila1 = df.loc[0, :]
# esto nos pasa todo lo que dice la fila q elegimos 
# (ahi eloegimos la primer fila )
# print(fila1)
