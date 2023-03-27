# Faça um programa que leia um número qualquer e mostre o seu fatorial

# Exemplo: 5! = 5x4x3x2x1 = 120

'''num = eval(input('Digite um número: '))
mult = 1
x = 0
m = num

while x <= num:
    x += 1
    mult = mult * x
print('Fatorial de {}! é {}'.format(num, mult))
'''

n = eval(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1

print('Calculando {}! = '.format(n), end='')

while c > 0:
    print('{}'.format(c), end='')
    print(' -> ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))