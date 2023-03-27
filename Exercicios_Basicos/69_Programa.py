# Crie um programa que leia a IDADE e o SEXO de VÁRIAS PESSOAS. A cada pessoa cadastrada, o programa deverá perguntar
#se o USUÁRIO quer ou não continuar. No final, mostre:

# 1 - Quantas pessoas tem mais de 18 ANOS.
# 2 - Quantos HOMENS foram cadastrados.
# 3 - Quantas MULHERES tem menos de 20 ANOS.

soma_maiores = 0
soma_homens = 0
soma_mulheres_menores = 0

while True:
    pessoa = str(input('Digite o seu nome: '))
    idade = eval(input('Digite sua idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]

    if idade > 18:
        soma_maiores += 1

    if sexo == 'M':
        soma_homens += 1

    if idade < 20 and sexo == 'F':
        soma_mulheres_menores += 1

    cont_cadastro = ' '
    while cont_cadastro not in 'SN':
        cont_cadastro = str(input('Que continuar o cadastramento? [S/N] ')).strip().upper()[0]
    if cont_cadastro == 'N':
        break

print('\nNúmeros de pessoas com mais de 18 = {}'.format(soma_maiores))
print('Numero de homens cadastrados = {}'.format(soma_homens))
print('Número de mulheres com menos de 20 = {}'.format(soma_mulheres_menores))







