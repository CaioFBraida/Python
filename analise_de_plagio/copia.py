##PROJETO ESTUDO
##ESQUELETO DE CÓDIGO PRONTO - 7 PRIMEIRAS FUNÇÃO FEITAS - TODAS AS OUTRAS AUTORIA PRÓPRIA.
##concertar funçoes tamanho medio sentença e tamanho medio frase
##Sab < 5 provavelmente é plágio
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
    tamanho_medio_sentenca = calcula_tamanho_medio_sentenca(tamanhos_palavras_texto,lista_sentencas_texto)
    
    #calcula complexidade de uma sentença
    complexidade_de_sentenca = calcula_complexidade_sentenca(lista_frases_texto_unica, lista_sentencas_texto)
    
    #calcula tamanho médio de frase
    tamanho_medio_frase = calcula_tamanho_medio_frase(tamanhos_palavras_texto, lista_frases_texto_unica)
    
    lista_assinatura = [tamanho_medio_palavra, razao_type_token, razao_Hapax_legomana, tamanho_medio_sentenca, complexidade_de_sentenca, tamanho_medio_frase]

    return lista_assinatura

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    menor_grau_similaridade = 10000
    numero_do_texto_infectado = 0
    for i in range(len(textos)):
        ass_texto = []
        ass_texto = calcula_assinatura(textos[i])
        grau_similaridade = compara_assinatura(ass_cp, ass_texto)
        if grau_similaridade < menor_grau_similaridade:
            menor_grau_similaridade = grau_similaridade
            numero_do_texto_infectado = i - 1
    return numero_do_texto_infectado




def main():
    #calcula_assinatura("Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca.")
    #calcula_assinatura("caio caio, caio caio. caio ciao, caio caio")
    
    #ass_0 = [4.51, 0.693, 0.55, 70.82, 1.82, 38.5]

    #ass_texto_1 = []
    #ass_texto_1 = calcula_assinatura("Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.")
    #print(ass_texto_1)
    #print()

    #ass_texto_2 = []
    #ass_texto_2 = calcula_assinatura("Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma.")
    #print(ass_texto_2)
    #print()
    #print(compara_assinatura(ass_0, ass_texto_1))
    
    #ass = []
    #ass = calcula_assinatura("Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova.")
    #print(ass)
    #####################
    assinatura_base = []
    assinatura_base = le_assinatura()
    listas_de_textos_lidas = []
    listas_de_textos_lidas = le_textos()

    #avalia_textos(listas_de_textos_lidas, assinatura_base)
main()
   

