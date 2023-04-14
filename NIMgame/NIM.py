def computador_escolhe_jogada(n, m):
    if (n <= m):
        numParaRetirar = n
    else:
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
    print("")
    while (naoAcertou):
        if (valorJogadoUsuario <= m and valorJogadoUsuario > 0):
            naoAcertou = False
        else:
            print("Oops! Jogada inválida! Tente de novo.")
            print("")
            valorJogadoUsuario = int(input("Quantas peças você vai tirar? "))
    return valorJogadoUsuario


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if (n % (m+1) == 0):
        print("")
        print("Você começa!")
        print("")
        while (n > 0):
            usuarioVaiTirar = usuario_escolhe_jogada(n, m)
            n = n - usuarioVaiTirar
            if (usuarioVaiTirar > 1):
                print("Você tirou " + str(usuarioVaiTirar) + " peças.")
            else:
                print("Você tirou uma peça.")
            if (n > 1):
                print("Agora restam " + str(n) + " peças no tabuleiro.")
                print("")
            if (n == 1):
                print("Agora resta apenas uma peça no tabuleiro.")
                print("")

            compVaiTirar = computador_escolhe_jogada(n, m)
            n = n - compVaiTirar
            if (compVaiTirar > 1):
                print("O computador tirou " + str(compVaiTirar) + " peças.")
            else:
                print("O computador tirou uma peça.")

            if (n > 1):
                print("Agora restam " + str(n) + " peças no tabuleiro.")
                print("")
            if (n == 1):
                print("Agora resta apenas uma peça no tabuleiro.")
                print("")

        print("Fim do jogo! O computador ganhou!")

    else:
        print("")
        print("Computador começa!")
        print("")
        while (n > 0):
            compVaiTirar = computador_escolhe_jogada(n, m)
            n = n - compVaiTirar
            if (compVaiTirar > 1):
                print("O computador tirou " + str(compVaiTirar) + " peças.")
            else:
                print("O computador tirou uma peça.")

            if (n > 1):
                print("Agora restam " + str(n) + " peças no tabuleiro.")
                print("")
            if (n == 1):
                print("Agora resta apenas uma peça no tabuleiro.")
                print("")

            if (n > 0):
                usuarioVaiTirar = usuario_escolhe_jogada(n, m)
                n = n - usuarioVaiTirar
                if (usuarioVaiTirar > 1):
                    print("Você tirou " + str(usuarioVaiTirar) + " peças.")
                else:
                    print("Você tirou uma peça.")
                if (n > 1):
                    print("Agora restam " + str(n) + " peças no tabuleiro.")
                    print("")
                if (n == 1):
                    print("Agora resta apenas uma peça no tabuleiro.")
                    print("")

        print("Fim do jogo! O computador ganhou!")

def campeonato():
    print("**** Rodada 1 ****")
    print("")
    partida()
    
    print("")
    print("**** Rodada 2 ****")
    print("")
    partida()

    print("")
    print("**** Rodada 3 ****")
    print("")
    partida()
    print("")
    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você 0 X 3 Computador")



def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    
    verifica = int(input("2 - para jogar um campeonato "))
    if(verifica == 1):
        partida()
    else:
        print("")
        print("Voce escolheu um campeonato!")
        print("")
        campeonato()


main()
