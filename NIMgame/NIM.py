def computador_escolhe_jogada(n, m):
    i = n
    while (i > 0):
        if (i % (m + 1) == 0):
            numQueVaiFicar = i
            break
        i = i - 1

    if (numQueVaiFicar % (m + 1) == 0):
        numParaRetirar = n - numQueVaiFicar
    else:
        numParaRetirar = m

    return numParaRetirar


def usuario_escolhe_jogada(n, m):
    naoAcertou = True
    valorJogadoUsuario = int(input("Quantas peças você vai tirar? "))
    while (naoAcertou):
        if (valorJogadoUsuario <= m and valorJogadoUsuario > 0):
            naoAcertou = False
        else:
            print("Oops! Jogada inválida! Tente de novo.")
            valorJogadoUsuario = int(input("Quantas peças você vai tirar? "))
    return valorJogadoUsuario

def partida():
    n = int(input("Digite o número de peças "))
    m = int(input("Digite o número max de peças a serem retiradas "))
    if(n % (m+1) == 0):
        print("Você começa!")
        while():
            computador_escolhe_jogada(n, m)
            usuario_escolhe_jogada(n, m)
    else:
        print("Computador começa!")
        while():
            usuario_escolhe_jogada(n, m)
            computador_escolhe_jogada(n, m)
        
    #atualiza n
    #identifica que jogo acabou


def main():
    partida()

main()
