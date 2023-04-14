def computador_escolhe_jogada(n, m):
    i = n
    numQueVaiFicar = -100
    while (i > 0):
        if (i % (m + 1) == 0):
            numQueVaiFicar = i
            break
        i = i - 1

    if (numQueVaiFicar % (m + 1) == 0 and numQueVaiFicar != (-100)):
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
        while(n > 0):
            usuarioVaiTirar = usuario_escolhe_jogada(n, m)
            n = n - usuarioVaiTirar
            if(usuarioVaiTirar > 1):
                print("Você tirou " + str(usuarioVaiTirar) + " peças.")
            else:
                print("Você tirou uma peça.")
            if(n > 1):
                print("Agora restam " + str(n) + " peças no tabuleiro.")
            else:
                print("Agora resta apenas uma peça no tabuleiro.")


            compVaiTirar = computador_escolhe_jogada(n, m)
            n = n - compVaiTirar
            if(compVaiTirar > 1):
                print("O computador tirou " + str(compVaiTirar) + " peças.")
            else:
                print("O computador tirou uma peça.")

            if(n > 1):
                print("Agora restam " + str(n) + " peças no tabuleiro.")
            else:
                print("Agora resta apenas uma peça no tabuleiro.")

        print("O computador ganhou!")
            
    else:
        print("Computador começa!")
        while(n > 0):
            compVaiTirar = computador_escolhe_jogada(n, m)
            n = n - compVaiTirar
            if(compVaiTirar > 1):
                print("O computador tirou " + str(compVaiTirar) + " peças.")
            else:
                print("O computador tirou uma peça.")

            if(n > 1):
                print("Agora restam " + str(n) + " peças no tabuleiro.")
            else:
                print("Agora resta apenas uma peça no tabuleiro.")

            usuarioVaiTirar = usuario_escolhe_jogada(n, m)
            n = n - usuarioVaiTirar
            if(usuarioVaiTirar > 1):
                print("Você tirou " + str(usuarioVaiTirar) + " peças.")
            else:
                print("Você tirou uma peça.")
            if(n > 1):
                print("Agora restam " + str(n) + " peças no tabuleiro.")
            else:
                print("Agora resta apenas uma peça no tabuleiro.")

        print("O computador ganhou!")



def main():
   # n = int(input("Digite o número de peças "))
   # m = int(input("Digite o número max de peças a serem retiradas "))
   # print(computador_escolhe_jogada(n, m))
   partida()

main()
