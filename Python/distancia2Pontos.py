import math

xP1 = int(input("Digite cordenada x do ponto 1 "))
yP1 = int(input("Digite cordenada y do ponto 1 "))
xP2 = int(input("Digite cordenada x do ponto 2 "))
yP2 = int(input("Digite cordenada y do ponto 2 "))

distancia = math.sqrt((xP1 - xP2)**2 + (yP1 - yP2)**2)

if(distancia >= 10):
    print("longe")
else:
    print("perto")

print("Distância é : ", distancia)