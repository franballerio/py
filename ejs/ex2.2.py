# queremos una funcion que si le damos un numero nos de numeros primos hasta llegar a ese numero

def es_primo(num):
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True


def llegar_con_primos(num):
    nums = list(range(2,num+1))
    for i in nums:
        if es_primo(i):
            print(i)


llegar_con_primos(23)
