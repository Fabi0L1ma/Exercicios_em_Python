'''Desenvolva um programa que leia o primeiro termo e a razão de PA. No final, mostre os 10 primeiros
 termos dessa progressão.'''

a1 = eval(input('Digite o primeiro termo da PA:'))
r = eval(input('Digite a razão da PA:'))

for c in range (1, 11):
    c = a1 + (c-1)*r
    print(c, end=' -> ')
print('ACABOU')