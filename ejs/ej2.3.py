# mostrar la serie de fibonaci entre un rango de numeros

def fibonacci_hasta(num):
    z = [0,1]
    for i in range(num+1):
        z.append(z[i]+z[1+i])
    print(z)    
    # z = z.append(z[2]+z[1])
    # z = z.append(z[3]+z[2])
    # z = z.append(z[4]+z[3])
    # z = z.append(z[2]+z[1])
    # z = z.append(z[2]+z[1])
    # z = z.append(z[2]+z[1])
    # z = z.append(z[2]+z[1])
    # z = z.append(z[2]+z[1])
    # z = z.append(z[2]+z[1])
    # z = z.append(z[2]+z[1])



fibonacci_hasta(10)
