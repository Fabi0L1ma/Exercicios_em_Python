"""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule e peça o preço da passagem, cobrando R$0,50
por Km para viagens de até 200Km e R#0,45 para viagens mais longas."""

dist_v = eval(input('Qual foi a distância da viagem?'))

if dist_v <= 200:
    print('O valor a ser pago: R${:.2f}'.format(dist_v * 0.50))
else:
    print('O valor a ser pago será de R${:.2f}'.format(dist_v * 0.45))
