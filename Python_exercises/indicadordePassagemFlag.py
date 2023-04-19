#descobrir se um numero tem 2 algarismos adjacentes iguais

numero = int(input("Digite um numero qualquer "))

ultimoNumero = 0
algarismoAdjacente = False
antipnultimoNumero = 0
while (numero > 0 and not algarismoAdjacente):
    ultimoNumero = numero % 10
    numero = numero // 10
    if(ultimoNumero == antipnultimoNumero):
        algarismoAdjacente = True
    
    antipnultimoNumero = ultimoNumero

   
if algarismoAdjacente:
    print("Possui algarismos adjacentes")
else:
    print("Não possui algarismos adjacentes")