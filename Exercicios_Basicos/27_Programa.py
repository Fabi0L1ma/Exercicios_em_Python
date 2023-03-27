"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo nome separadamente."""

nome = str(input('Digite o seu nome:')).strip().split()

print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))