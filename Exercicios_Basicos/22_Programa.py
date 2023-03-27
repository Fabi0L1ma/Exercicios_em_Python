"""Crie um programa que leia o nome completo de uma pessoa e mostre:
 1- O nome com todas as letras maiúsculas e minúsculas.
 2- Quantas letras ao todo (sem considerar espaço)
 3- Quantas letras tem o primeiro nome."""

nome = str(input("Digite o seu nome:")).strip()

print("Em maiúsculas é: {} ".format(nome.upper()))
print("Em minúsculas é: {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))