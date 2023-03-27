# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a CONDIÇÃO DE PARADA. No final mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles
# (DISCONSIDERANDO O FLAG)

num = eval(input('Digite um número: '))

soma = 0
cont = 0

while num != 999:
    soma += num
    cont += 1
    num = eval(input('Digite um número: '))
    if num == 999:
        print('\n')
        break

print('Quantidade de números digitados: {}'.format(cont))
print('Soma dos números: {}'.format(soma))