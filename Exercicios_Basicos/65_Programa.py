# Crie um programa que leia vários números inteiros pelo teclado. No final da execução , mostre a média entre todos
# os valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# CONTINUAR a digitar valores.

med = 0
soma = 0
cont = 0
maior = 0
menor = 0
opc = 0

while opc != 'N':
    num = eval(input('Digite um número: '))
    soma += num
    cont += 1
    med = soma / cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opc = str(input('Digite [N] para SAIR ou [S] para continuar: ')).upper()
print('\nA média = {}'.format(med))
print('O maior = {}'.format(maior))
print('O menor = {}'.format(menor))