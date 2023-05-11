def ordenada(listap):
    lista = []
    for num in listap:
        lista.append(num)
    
    
    for i in range(len(lista) - 1):

        menor_valor = lista[i]
        posicao_menor_valor = i

        for j in range(i+1,len(lista)):
            if lista[j] < menor_valor:
                menor_valor = lista[j]
                posicao_menor_valor = j

        lista[i], lista[posicao_menor_valor] = lista[posicao_menor_valor], lista[i]

    if lista == listap:
        return True
    return False