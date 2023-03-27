"""Um professor quer sortear um dos seus quatro alunos para apagar o
quadro. Faça um programa que ajude ele, lendo o nome deles e
escrevendo o nome do escolhido."""

import random

a1 = str(input("Primeiro aluno:"))
a2 = str(input("Segundo aluno:"))
a3 = str(input("Terceiro aluno:"))
a4 = str(input("Quarto aluno:"))

escolha_a = [a1, a2, a3, a4]
aluno_s = random.choice(escolha_a)

print("O aluno selecionado foi:{}".format(aluno_s))