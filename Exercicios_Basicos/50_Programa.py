'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquele que forem pares. Se o valor
digitado for impar, desconsidere-o.'''

soma = 0

for c in range(1, 7):
    num = eval(input('Digite um número:'))
    if num % 2 == 0:
        soma = num + soma
print('A soma dos pares {}'.format(soma))