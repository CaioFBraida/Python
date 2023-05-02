##PROJETO ESTUDO
##ESQUELETO DE CÓDIGO PRONTO - 7 PRIMEIRAS FUNÇÃO FEITAS - TODAS AS OUTRAS AUTORIA PRÓPRIA.
##concertar funçoes tamanho medio sentença e tamanho medio frase

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

def calcula_tamanho_medio_sentenca(lista_sentencas_texto):
    #numero de cararcteres sentencas /numero sentencas
    soma_caracteres_sentencas = 0
    lista_numero_caracteres_sentencas = []
    for i in range(len(lista_sentencas_texto)):
        lista_numero_caracteres_sentencas.append (len(lista_sentencas_texto[i]))
    
    for numero in lista_numero_caracteres_sentencas:
        soma_caracteres_sentencas = soma_caracteres_sentencas + numero

    tamanho_medio_sentenca = soma_caracteres_sentencas / len(lista_sentencas_texto)
      
    return tamanho_medio_sentenca

def calcula_complexidade_sentenca(lista_frases_texto, lista_sentencas_texto):
    #complexidade_sentenca = numero_total_frases / numero_total_sentencas
    numero_total_frases = len(lista_frases_texto)
    numero_total_sentencas = len(lista_sentencas_texto)
    complexidade_sentenca = numero_total_frases / numero_total_sentencas
    return complexidade_sentenca

def calcula_tamanho_medio_frase(lista_frases_texto_unica):
    #numero de cararcteres frase/numero frase
    soma_caracteres_frase = 0
    lista_numero_caracteres_frase = []
    for i in range(len(lista_frases_texto_unica)):
        lista_numero_caracteres_frase.append (len(lista_frases_texto_unica[i]))

    for numero in lista_numero_caracteres_frase:
        soma_caracteres_frase = soma_caracteres_frase + numero

    tamanho_medio_frase = soma_caracteres_frase / len(lista_frases_texto_unica)
  
    return tamanho_medio_frase

def compara_assinatura(as_a, as_b):
    #recebe duas assinaturas e compara a diferença entre elas
    somas = []
    for i in range(len(as_a)):
        somas.append(abs(as_a[i] - as_b[i]))
    
    somatorio = 0
    for soma in somas:
        somatorio = somatorio + soma
    
    grau_similaridade_Sab = somatorio / len(somas)

    return grau_similaridade_Sab

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
    
    #calcula razao_type_token
    razao_type_token = calcula_razao_type_token(numero_palavras_diferentes, numero_total_palavras)
   
    #calcula Razão Hapax Legomana
    razao_Hapax_legomana = calcula_razao_Hapax_legomana(numero_palavras_aparecem_umavez, numero_total_palavras)
    
    #calcula tamanho medio sentença
    tamanho_medio_sentenca = calcula_tamanho_medio_sentenca(lista_sentencas_texto)
    
    #calcula complexidade de uma sentença
    complexidade_de_sentenca = calcula_complexidade_sentenca(lista_frases_texto_unica, lista_sentencas_texto)
    
    #calcula tamanho médio de frase
    tamanho_medio_frase = calcula_tamanho_medio_frase(lista_frases_texto_unica)
    
    lista_assinatura = [tamanho_medio_palavra, razao_type_token, razao_Hapax_legomana, tamanho_medio_sentenca, complexidade_de_sentenca, tamanho_medio_frase]

    return lista_assinatura

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    lista_assinaturas_texto = []
    for i in range(len(textos)):
        lista_assinaturas_texto.append(calcula_assinatura(textos[i]))

    lista_grau_similaridade_textos = []
    for i in range(len(lista_assinaturas_texto)):
        lista_grau_similaridade_textos.append(compara_assinatura(lista_assinaturas_texto[i], ass_cp))
    
    valor_do_texto_infectado = lista_grau_similaridade_textos[0]
    numero_do_texto_infectado = 0
    for i in range(len(lista_grau_similaridade_textos)):
        if valor_do_texto_infectado > lista_grau_similaridade_textos[i]:
            valor_do_texto_infectado = lista_grau_similaridade_textos[i]
            numero_do_texto_infectado = i + 1
    
    return numero_do_texto_infectado 


def main():
    ######### testes aqui:
    
    #############
    assinatura_base = []
    assinatura_base = le_assinatura()
    listas_de_textos_lidos = []
    listas_de_textos_lidos = le_textos()

    numero_texto_infectado = avalia_textos(listas_de_textos_lidos, assinatura_base)
    
    print()
    print("O autor do texto " +  str(numero_texto_infectado) +  " está infectado com COH-PIAH")



