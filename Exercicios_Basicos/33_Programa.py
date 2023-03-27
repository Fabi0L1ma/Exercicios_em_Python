"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

n1 = eval(input('Digite um número:'))
n2 = eval(input('Digite outro número:'))
n3 = eval(input('Digite mais um outro número:'))

if n1 > n2 and n1 > n3:
    print('{} é maior que {} e {}'.format(n1, n2, n3))
else:
    if n2 > n1 and n2 > n3:
        print('{} é maior que {} e {}'.format(n2, n1, n3))
    else:
        if n3 > n1 and n3 > n2:
            print('{} é maior que {} e {}'.format(n3, n1, n2))
        else:
            print('Valores iguais.')


