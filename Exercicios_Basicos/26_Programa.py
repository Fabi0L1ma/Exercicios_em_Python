"""Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A" e
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez."""

frase = str(input('Digite uma frase:')).upper().strip()

print('A letra A aparece:{}'.format(frase.count('A')))
print('Primeira posição:{}'.format(frase.find('A')+1))
print('A última posição {}'.format(frase.rfind('A')+1))
