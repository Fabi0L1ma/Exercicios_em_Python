""" Faça um programa que leia a largura e a altura de uma parede em metros,calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2
"""

med1 = eval(input('Digite a largura da parede:'))
med2 = eval(input('Digite a altura da parede:'))

area = med1*med2

areap = area/2

print('A area a ser pintada é de: {}m²  \nA quantidade de tinta necessária sera de: {}L'.format(area,areap))