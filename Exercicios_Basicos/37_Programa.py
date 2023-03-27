'''Escreva um programa que leia um número inteiro qualquer e peça para o usuaário escolher qual será a base de conversão:

-1 para binário
-2 para octal
-3 para hexadecimal

'''

print('=====Conversor de Números=====')

num = eval(input('Digite o número que você quer converter:'))

print('Escolha o tipo de conversão:')
print('1 - Para binário \n2- Para octal \n3- Para hexadecimal')
opc = eval(input('Escolha:'))


if opc == 1:
    print('{} para binario é {}.'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} para octal é {}.'.format(num, oct(num)[2:]))
elif opc == 3:
    print('{} para hexaadecimal é {}'.format(num, hex(num)[2:834]))
