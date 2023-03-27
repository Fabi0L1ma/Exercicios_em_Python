"""Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retângulo, calcule e mostre comprimento da
hipotenusa."""

import math

co = eval(input("Comprimento do cateto oposto:"))
ca = eval(input("Comprimento do cateto adjacente:"))
hi = math.hypot(co,ca)

print(("A hipotenusa vai medir {:.2f}".format(hi)))