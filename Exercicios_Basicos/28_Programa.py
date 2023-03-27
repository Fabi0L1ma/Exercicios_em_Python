"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário descobrir
qua foi o número escolhido pelo computador.
- O programa deverá escrever na tela se o usúario venceu ou perdeu."""

import random
import time

num = [0, 5]
escolha_c = random.choice(num)
escolha_p = eval(input('Escolha um número de 0 à 5:'))

print('PROCESSANDO...')
time.sleep(3)

if escolha_p == escolha_c:
    print('Você venceu')
else:
    print('Você perdeu')

print('Escolha do PC: {}'.format(escolha_c))
print('Escolha da pessoa: {}'.format(escolha_p))