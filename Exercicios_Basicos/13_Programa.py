""" Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
""""
EXEMPLO 1:

salr = eval(input('Digite o seu salario: R$'))

aumsalr = salr + ((salr*15)/100)

print('O funcionário ganhava R${:.2f}, com o aumento de 15% o salário dele passará a ser de R${:.2f}'.format(salr,aumsalr))
"""

salario = eval(input('Digite o seu salario: R$'))

print('O funcionário ganhava R${:.2f}, com aumento de 15% o salário dele passará a ser de R${:.2f}'.format(salario,(salario+(salario*15)/100)))


