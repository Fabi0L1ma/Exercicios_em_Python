'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

tot = 0

num = eval(input('Digite um número: '))

for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')

print('\n\033[m\nO número {} foi divisivel {} vezes\n'.format(num, tot))

if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')
