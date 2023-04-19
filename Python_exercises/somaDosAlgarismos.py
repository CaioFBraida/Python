#soma dos digitos do numero

numero = int(input("Digite um numero qualquer "))

soma = 0
ultimoNumero = 0
while(numero > 0):
    ultimoNumero = numero % 10
    numero = numero // 10
    soma += ultimoNumero
    
    print("o numero ficou ", numero)
    print("o ultimo numero é ",ultimoNumero)
    print("a soma esta ", soma)

print(soma)