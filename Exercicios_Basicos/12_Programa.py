""" Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
"""
vprodut = eval(input('Qual o valor do produto ? R$'))

desc = (vprodut*5)/100

vdesc = vprodut - desc

print('O valor do produto com desconto será de: R${}'.format(vdesc))
"""

valProdut = eval(input('Qual o valor do produto? R$'))

print('O valor do produto com desconto será de: R${:.2f}'.format(valProdut - (valProdut * 5)/100))
