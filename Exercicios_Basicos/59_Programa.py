# Crie um programa que leia dois valores e mostre um menu na tela:

# [1] SOMAR
# [2] MULTIPLICAR
# [3] MAIOR
# [4] NOVOS NÚMEROS
# [5] SAIR DO PROGRAMA

# Seu programa deverá realizar a operação solicitada em cada caso.

num1 = eval(input('Digite o primeiro número: '))
num2 = eval(input('Digite o segundo número: '))

esc = 0

while esc != 5:

    print('========== Escolhas ==========')

    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA\n')

    esc = eval(input('Qual é a sua escolha: '))

    if esc == 1:
        print('A SOMA É {}\n'.format(num1+num2))

    elif esc == 2:
        print('A MULTIPLICAÇÃO É {}\n'.format(num1*num2))

    elif esc == 3:
        if num1 > num2:
            print('O maior número é {}\n'.format(num1))
        elif num2 > num1:
            print('O número é {}\n'.format(num2))
        else:
            print('OS NÚMEROS SÃO IGUAIS!')

    elif esc == 4:
        print('Digite novos números.\n')
        num1 = eval(input('Digite o primeiro número:'))
        num2 = eval(input('Digite o segundo número: '))

    elif esc == 5:
        print('SAINDO DO PROGRAMA!')
