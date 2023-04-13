def computador_escolhe_jogada(n, m):
    
    #n - numParaRetirar == numQueVaiFicar
    i = n
    while(i > 0):
        if(i % (m + 1) == 0):
            numQueVaiFicar = i
        i = i - 1
        
    if(numQueVaiFicar % (m + 1) == 0):
        numParaRetirar = n - numQueVaiFicar
    else:
        numParaRetirar = m


    return numParaRetirar

#def usuario_escolhe_jogada():


def main():
    n = int(input("Digite o número de peças "))
    m = int(input("Digite o número max de peças a serem retiradas "))
    print(computador_escolhe_jogada(n, m))

main()