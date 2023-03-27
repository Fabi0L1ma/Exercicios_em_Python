""" Escreva um programa que pergunte a quantidade de KM percorrido por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
o carro custa R$60 por dia R$0,15 por KM rodado.
"""
"""

EXEMPLO 1:

temp = eval(input('Digite quantos dias o carro ficou alugado:'))
km = eval(input('Digite quantos KM foi percorrido pelo carro:'))

kmv = km * 0.15
tempv = temp * 60
val = kmv + tempv

print('O valor a ser pago será de: R${:.2f}'.format(val))

"""

tempo = eval(input('Digite quantos dias o carro ficou alugado:'))
km = eval(input('Digite quantos Km foi percorrido pelo carro:'))

print('O valor a ser pago será de: R${:.2f}'.format((km*0.15+tempo*60)))