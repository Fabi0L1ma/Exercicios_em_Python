'''Faça um programa que calcule a soma entre todos os númros impares que são mútiplos de três e que se
encontram no intervalo de 1 até 500.'''

soma = 0
cont = 0

for c in range (1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
        print(c, end=' ')
print('\nA SOMA DE TODOS OS {} FOI {}.'.format(cont, soma))