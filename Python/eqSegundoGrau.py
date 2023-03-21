#PROGRAMA  calcula valor de raizes equação segundo grau

import math

a = int(input("Digite a "))
b = int(input("Digite b "))
c = int(input("Digite c "))

delta = (b * b) - 4 * a * c




if delta > 0:
    print("A equação possui 2 raízes.")
    raiz1 = (-b + math.sqrt(delta) ) / 2 * a
    raiz2 = (-b - math.sqrt(delta) ) / 2 * a

    print("primeira raiz = ", raiz1, " segunda raiz : ", raiz2)

elif delta == 0:
    print("A equação possui 1 raízes.")
    raiz = -b  / (2 * a)

    print("A raiz vale : ", raiz)

else:
    print("A equação não possuiu raizes")