# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
# sequência de Fibonacci.

# EXEMPLO: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8


num = eval(input('Qunatos termos você quer mostrar? '))

t1 = 0
t2 = 1

print('{} -> {}'.format(t1, t2), end='')

cont = 3

while cont <= num:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('-> FIM!')
