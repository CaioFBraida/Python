def remove_repetidos(lista):
    lista_removida = []
    for i in range(0,len(lista)):
        if(lista[i] not in lista_removida):
            lista_removida.append (lista[i])

    lista_removida.sort()
    return lista_removida

