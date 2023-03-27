'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

num = eval(input('Digite o número que você quer a tabuada:'))

for c in range(1, 11):
    cal = num * c
    print(c, 'x', num, '=', cal )