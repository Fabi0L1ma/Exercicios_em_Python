# Faça um programa que mostre a TABUADA de VÁRIOS NÚMEROS, um de cada vez, para cada valor digitado pelo usuário.
#O programa será INTERROMPIDO quando o número solicitado for NEGATIVO.

num = 1

while num > 0:
    num = eval(input('Digite o número da tabuada: '))
    if num < 0:
        break
    for c in range(1, 11):
        cal = num * c
        print(c, 'x', num, '=', cal)

