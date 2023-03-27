'''Melhore o jogo do DESAFIO 028 onde o computador vai 'PENSAR' em um número entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer'''

import random
import time

print('========== JOGO DE ADV ==========')
esc_pess = eval(input('Escolha um número de 0 à 10: '))
print('=================================')

num = [0,1,2,3,4,5,6,7,8,9,10]

esc_comp = random.choice(num)
time.sleep(1)

palpites = 0

while esc_comp != esc_pess:
    num = [0,1,2,3,4,5,6,7,8,9,10]
    esc_comp = random.choice(num)
    print('PC escolhendo...')
    time.sleep(1)
    print(esc_comp)
    palpites += 1
print('numero de palpites: {} '.format(palpites))


