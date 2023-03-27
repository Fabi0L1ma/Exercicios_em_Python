"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados."""

n = eval(input("Digite um número:"))

unid = n // 1 % 10
dezen = n // 10 % 10
cent = n // 100 % 10
mil = n // 1000 % 10

print("Analisando o número {}".format(n))
print("Unidade: {}".format(unid))
print("Dezena: {}".format(dezen))
print("Centena: {}".format(cent))
print("Milhar: {}".format(mil))

