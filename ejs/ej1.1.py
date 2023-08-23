# vamos a calcular los promedios y eso q dice dalto xd

# usamos de ejemplo 4 cursos, uno promedio,
# uno mas rapido, uno mas lento y el de dalto
# 1.5 dalto(3 crudo), 2.5 min(3.5 crudo), 4 prom (5 crudo), 7 max

curso_min = 2.5
crudo_min = 3.5
curso_max = 7
curso_prom = 4
crudo_prom = 5
curso_dalto = 1.5
crudo_dalto = 3
print(
    f"Los cursos tienen una duracion, para llegar hasta aca, de: {curso_min}hs el minimo, {curso_dalto}hs el de dalto, {curso_max}hs el maximo y {curso_prom}hs uno promedio")

# ahora calculamos el porcentaje de cuan mas rapido es el curso de dalto

con_max = 100-(curso_dalto*100)/curso_max
con_min = 100-(curso_dalto*100)/curso_min
con_prom = 100-(curso_dalto*100)/curso_prom
promedio_gral = (con_prom + con_max + con_min)/3
promedio_gral = round(promedio_gral, 2)
print(
    f"Con respecto a los demas cursos el de dalto, en promedio es un {promedio_gral}% mas rapido")

por_crudo_dalto = round(100-(curso_dalto*100)/crudo_dalto, 2)
por_crudo_min = 100-(curso_min*100)/crudo_min
por_crudo_prom = 100-(curso_prom*100)/crudo_prom
prom_crudo_ = round((por_crudo_min+por_crudo_prom)/2, 2)

print(
    f"Los cursos eliminan un {prom_crudo_}% de material inservible, mientras que dalto elimina un {por_crudo_dalto}%")

prom_cursos = round((7+2.5+4)/3, 2)
vale_dal = round((10*prom_cursos)/1.5, 2)
print(
    f"Ver 10hs del curso de dalto equivalen a ver {vale_dal}hs de otros cursos"
)
