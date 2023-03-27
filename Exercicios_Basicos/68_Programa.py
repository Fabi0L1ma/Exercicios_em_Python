# Faça um programa que jogue PAR OU IMPAR com o computador. O jogo só sera interrompido quando o jogador Perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

v = 0

while True:
    jogador = eval(input('Diga um valor: '))
    computador = random.randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR? [P/I] = ')).strip().upper()[0]
    print('Você jogou {} e o computador {}. Total = {}'.format(jogador, computador, total))
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente!')
print('Números de vitórias = {}'.format(v))








