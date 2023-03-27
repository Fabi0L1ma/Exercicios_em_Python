'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:

-Até 9 anos: MIRIM
-Até 14 anos: INFANTIL
-Até 19 anos: JUNIOR
-Até 20 anos: SÊNIOR
-ACIMA:MASTER
'''

ano_n = eval(input('Informe o ano de nascimento do atleta:'))

cal_c = 2022 - ano_n

if cal_c <= 9:
    print('MIRIM')
elif cal_c <= 14:
    print('INFANTIL')
elif cal_c <= 19:
    print('JUNIOR')
elif cal_c <= 20:
    print('SÊNIOR')
elif cal_c > 20:
    print('MASTER')