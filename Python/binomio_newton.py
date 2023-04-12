def fatorial(n):
    i = n
    fat = 1
    while(i > 0):
        fat = fat * i
        i = i - 1
    return fat    


def binomioNewton(n, k):
    return fatorial(n)/fatorial(k)*fatorial(n-k)


n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

print(binomioNewton(n,k))    