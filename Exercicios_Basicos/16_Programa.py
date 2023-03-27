"""Crie um programa que leia um número Real qualquer pelo teclado e
mostre na tela a sua porção inteira.
Exemplo: Digite o número 6.123 o número 6.123 tem a parte inteira 6."""

import math
num = eval(input("Digite um número:"))
valor_t = math.trunc(num)
print("O valor do numero REAL {} em INTEIRO é {}".format(num, valor_t))