"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo."""

import math

ang = eval(input("Digite o ângulo que você deseja:"))
sen = math.sin(math.radians((ang)))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print("SENO = {:.2f} \nCOSSENO = {:.2f} \nTANGENTE = {:.2f}".format(sen, cos, tang))
