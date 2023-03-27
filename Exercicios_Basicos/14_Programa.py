""" F = C x 1,8 + 32

Informar a temperatura em °C e coverter para °F

"""
"""
EXEMPLO 1 : 

temp = eval(input('Digite a temperatura em °C: '))

convers = temp * 1.8 + 32

print('O valor em °C é: {} \nO valor em °F é: {}'.format(temp,convers))
"""

temp = eval(input('Digite a temperatura em °C: '))

print('O valor em °C é: {} \nO valor em °F é: {}'.format(temp,(temp * 1.8 + 32)))