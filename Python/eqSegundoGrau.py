# PROGRAMA  calcula valor de raizes equação segundo grau

import math



def delta(a, b, c):
    return (b * b) - 4 * a * c


def main():
    a = int(input("Digite a "))
    b = int(input("Digite b "))
    c = int(input("Digite c "))
    imprime_raizes(a, b, c)


def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d > 0:
        print("A equação possui 2 raízes.")
        raiz1 = (-b + math.sqrt(d)) / 2 * a
        raiz2 = (-b - math.sqrt(d)) / 2 * a
        print("primeira raiz = ", raiz1, " segunda raiz : ", raiz2)

    elif d == 0:
        print("A equação possui 1 raízes.")
        raiz = -b / (2 * a)
        print("A raiz vale : ", raiz)

    else:
        print("A equação não possuiu raizes")

main()