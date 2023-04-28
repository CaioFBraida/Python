##PROJETO ESTUDO
##ESQUELETO DE CÓDIGO PRONTO - 7 PRIMEIRAS FUNÇÃO FEITAS - TODAS AS OUTRAS AUTORIA PRÓPRIA.

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def transforma_listadelista_em_lista(lista):
    lista_unica = []
    for lista in lista:
        lista_unica.extend(lista)
    return lista_unica

def tamanhos_palavras(lista_palavras):
    lista_tamanhos_palavras = []
    for palavra in lista_palavras:
        lista_tamanhos_palavras.append(len(palavra))
    return lista_tamanhos_palavras

def calcula_tamanho_medio_palavras(tamanhos_palavras_texto, lista_palavras_texto_unica):
    
    #tamanho_medio_palavra = soma_tamanho_palavras / numero_total_palavras
    
    soma_tamanho_palavras = 0
    for tam in tamanhos_palavras_texto:
        soma_tamanho_palavras = soma_tamanho_palavras + tam

    tamanho_medio_palavra = soma_tamanho_palavras / len(lista_palavras_texto_unica)

    return tamanho_medio_palavra

def calcula_razao_type_token(num_palavras_diferentes ,numero_total_palavras):
    razao_type_token = num_palavras_diferentes / numero_total_palavras
    return razao_type_token
    
def calcula_razao_Hapax_legomana(numero_palavras_aparecem_umavez, numero_total_palavras):
    razao_Hapax_legomana = numero_palavras_aparecem_umavez / numero_total_palavras
    return razao_Hapax_legomana

def calcula_tamanho_medio_sentenca(tamanhos_palavras_texto,lista_sentencas_texto):
    #essa função precisa calcular o total de caracteres excluindo os caracteres que separam as sentenças e dividir pelo 
    #numero de sentencas para achar o tamanho medio de sentencas
    numero_sentencas = len(lista_sentencas_texto)
    numero_total_caracteres_palavras_texto = 0
    quantidade_espacos_entre_palavras = len(tamanhos_palavras_texto)
    for tamanhos in tamanhos_palavras_texto:
        numero_total_caracteres_palavras_texto = numero_total_caracteres_palavras_texto + tamanhos
    numero_real_caracteres_texto = numero_total_caracteres_palavras_texto + (quantidade_espacos_entre_palavras - 1) - (numero_sentencas - 1)
    tamanho_medio_sentencas = numero_real_caracteres_texto / numero_sentencas

    return tamanho_medio_sentencas

def calcula_complexidade_sentenca(lista_frases_texto, lista_sentencas_texto):
    #complexidade_sentenca = numero_total_frases / numero_total_sentencas
    numero_total_frases = len(lista_frases_texto)
    numero_total_sentencas = len(lista_sentencas_texto)
    complexidade_sentenca = numero_total_frases / numero_total_sentencas
    return complexidade_sentenca

def calcula_tamanho_medio_frase(tamanhos_palavras_texto,lista_frases_texto_unica):
    #soma_total_caracteres / numero de frases
    numero_frases = len(lista_frases_texto_unica)
    numero_total_caracteres_palavras_texto = 0
    quantidade_espacos_entre_palavras = len(tamanhos_palavras_texto)
    for tamanhos in tamanhos_palavras_texto:
        numero_total_caracteres_palavras_texto = numero_total_caracteres_palavras_texto + tamanhos
    numero_real_caracteres_texto = numero_total_caracteres_palavras_texto + (quantidade_espacos_entre_palavras - 1) - (numero_frases - 1)
    tamanho_medio_frase = numero_real_caracteres_texto / numero_frases

    return tamanho_medio_frase

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    #criando listas de frases, palavras, sentenças, tamanho de palavras
    lista_sentencas_texto = separa_sentencas(texto)
    
    lista_frases_texto = []
    for i in lista_sentencas_texto:
        lista_frases_texto.append (separa_frases(i)) 
    lista_frases_texto_unica = transforma_listadelista_em_lista(lista_frases_texto)
    
    lista_palavras_texto = []
    for i in lista_frases_texto_unica:
        lista_palavras_texto.append(separa_palavras(i))
    lista_palavras_texto_unica = transforma_listadelista_em_lista(lista_palavras_texto)
    
    tamanhos_palavras_texto = tamanhos_palavras(lista_palavras_texto_unica)

    numero_palavras_diferentes = n_palavras_diferentes(lista_palavras_texto_unica)
    
    numero_total_palavras = len(lista_palavras_texto_unica)

    numero_palavras_aparecem_umavez = n_palavras_unicas(lista_palavras_texto_unica)


    #calcula TAMANHO MEDIO PALAVRA
    tamanho_medio_palavra = calcula_tamanho_medio_palavras(tamanhos_palavras_texto, lista_palavras_texto_unica)
    print("tamanho médio palavra: ")
    print(tamanho_medio_palavra)
    print()


    #calcula razao_type_token
    razao_type_token = calcula_razao_type_token(numero_palavras_diferentes, numero_total_palavras)
    print("razao type token: ")
    print(razao_type_token)
    print()

    #calcula Razão Hapax Legomana
    razao_Hapax_legomana = calcula_razao_Hapax_legomana(numero_palavras_aparecem_umavez, numero_total_palavras)
    print("Razão Hapax Legomana: ")
    print(razao_Hapax_legomana)
    print()

    #calcula tamanho medio sentença
    tamanho_medio_sentenca = calcula_tamanho_medio_sentenca(tamanhos_palavras_texto,lista_sentencas_texto)
    print("Tamanho medio sentença: ")
    print(tamanho_medio_sentenca)
    print()

    #calcula complexidade de uma sentença
    complexidade_de_sentenca = calcula_complexidade_sentenca(lista_frases_texto_unica, lista_sentencas_texto)
    print("Complexidade de sentença: ")
    print(complexidade_de_sentenca)
    print()

    #calcula tamanho médio de frase
    tamanho_medio_frase = calcula_tamanho_medio_frase(tamanhos_palavras_texto, lista_frases_texto_unica)
    print("Tamanho médio de frase: ")
    print(tamanho_medio_frase)
    print()







def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass

def main():
    #calcula_assinatura("Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca.")
    calcula_assinatura("caio caio, caio caio. caio ciao, caio caio")
    
main()
   

