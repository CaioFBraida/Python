def cria_matriz(num_linhas, num_colunas, valor):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)
        
        matriz.append(linha)
    return matriz

def le_matriz():
    num_linhas = int(input("Digite numero de linhas da matriz: "))
    num_colunas = int(input("Digite numero de colunas da matriz: "))
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("DIgite o elemento [" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)
        
        matriz.append(linha)
    return matriz

def imprime_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j != (len(matriz[0]) - 1):
                print(matriz[i][j], end=" ")
            else:
                print(matriz[i][j])