'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule IMC e mostre seu status, de acordo com a
tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''

peso = eval(input('Digite o seu peso:'))
altura = eval(input('Digite a sua altura:'))

imc = peso/(altura)**2

if imc < 18.5:
    print('IMC = {:.2f}. \nAbaixo do peso.'.format(imc))
elif imc < 25 or imc == 18.5:
    print('IMC = {:.2f}. \nPeso ideal.'.format(imc))
elif imc <= 30 or imc == 25:
    print('IMC = {:.2f}. \nSobrepeso.'.format(imc))
elif imc <= 40 or imc == 30:
    print('IMC = {:.2f}. \nObesidade.'.format(imc))
elif imc > 40:
    print('IMC = {:.2f}. \nObesidade mórbida.'.format(imc))
