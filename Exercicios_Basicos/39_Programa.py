'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar .
- Se já passou do tempo do alistamento.

Seu programa também deverá mostra o tempo que falta ou que passou do prazo.
'''

ano_n = eval(input('Informe o seu ano de nascimento:'))

cal_i = 2022 - ano_n

print('Você possui {} Anos.'.format(cal_i))

if cal_i == 18:
    print('É a hora de se alistar.')
elif cal_i > 18:
    print('Passou do tempo do alistamento. Você passou {} anos do prazo.'.format(cal_i-18))
elif cal_i < 18:
    print('Você vai ser chamado para o alistamento militar daqui a {} anos.'.format(18-cal_i))
