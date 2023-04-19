def verificaPrimo(n):
    i = 2
    while(i < n):
        if(n % i == 0):
            return 0
        i = i + 1
    return n
            

def maior_primo(n):
    verifica = 0
    while(verifica == 0):
        verifica = verificaPrimo(n)
        n = n - 1
    return verifica

