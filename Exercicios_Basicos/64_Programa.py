# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma ]
# entre eles (desconsiderando o flag)

num = eval(input('Digite alguns números (999 para SAIR): '))

soma = 0
cont = 0

while num != 999:
    soma += num
    cont += 1
    num = eval(input('Digite alguns números (999 para SAIR): '))
print('A soma dos números são {} e foram digitados {} números.'.format(soma, cont))
