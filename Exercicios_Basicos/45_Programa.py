'''Crie um programa que faça o computador jogar Jokenpô com você.'''

import random
import time

n = [0, 2]
print('Suas opções: \n[0]PEDRA \n[1]PAPEL \n[2]TESOURA')
esc_p = eval(input('Qual a sua escolha? '))

esc_c = random.choice(n)
print('JOKENPÔ!')
time.sleep(1)

if esc_c == 0 and esc_p == 1:
    print('O PC escolheu PEDRA  e Você PAPEL.')
    print('VOCÊ VENCEU!')
elif esc_c == 1 and esc_p == 2:
    print('O PC escolheu PAPEL e Você TESOURA.')
    print('VOCÊ VENCEU!')
elif esc_c == 2 and esc_p == 0:
    print('O PC escolheu TESOURA e Você PEDRA.')
    print('VOCÊ VENCEU!')
elif esc_p == 0 and esc_c == 1:
    print('O PC escolheu PEDRA e Você PAPEL.')
    print('O PC VENCEU!')
elif esc_p == 1 and esc_c == 2:
    print('O PC escolheu TESOURA e Você PAPEL.')
    print('O PC VENCEU!')
elif esc_p == 1 and esc_c == 0:
    print('O PC escolheu PAPEL e Você PEDRA.')
    print('O PC VENCEU!')
elif esc_c == esc_p:
    print('O PC e Você fizeram a mesma jogada.')
    print('EMPATE')
elif esc_p != n and esc_c != n:
    print('Jogada ivalida!')






