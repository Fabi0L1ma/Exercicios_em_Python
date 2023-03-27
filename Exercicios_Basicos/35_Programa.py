"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo."""

med1 = eval(input('Digite a primeira médida:'))
med2 = eval(input('Digite a segunda médida:'))
med3 = eval(input('Digite a terceira médida:'))

if med1 < med2 + med3 and med2 < med1 + med3 and med3 < med1 + med2:
    print('É UM TRIANGULO')
else:
    print('NÃO É TRIANGULO')
