"""Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO."""

esc_anos = eval(input('Digite um ano:'))

p_anos =  esc_anos % 4

if p_anos == 0 and esc_anos % 100 != 0 or esc_anos % 400 == 0:
    print('{} é um ano Bissexto'.format(esc_anos))
else:
    print('{} não é um ano Bissexto'.format(esc_anos))


