largura = int(input("digite a largura: "))
altura = int(input("Digite a altura: "))

i = 0
j = 0
while(i < altura):
    while(j < largura):
        if(i == 0 or i == (altura - 1)):
            print("#", end= "")
        else:
            if(j == 0 or j == (largura - 1)):
                print("#", end= "")
            else:
                print(" ", end= "")
        j = j + 1
    i = i + 1
    print()
    j = 0