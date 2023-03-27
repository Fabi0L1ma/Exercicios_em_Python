'''Refaça o DESAFIO 035 dos triÂngulos, acrescentando o recurso de mostrar que tipo de triÂngulo será formado:

-EQUILÁTERO: todos os lados iguais.
-ISÓSCELES: dois lados iguais.
-ESCALENO: todos os lados diferentes.
'''

med1 = eval(input('Informe a primeira médida:'))
med2 = eval(input('Informe a segunda médida:'))
med3 = eval(input('Informe a terceira médida:'))

if med1 == med2 == med3:
    print('Equilatero.')
elif med1 == med2 != med3 or med1 == med3 != med2 or med2 == med3 != med1:
    print('Isósceles.')
elif med1 != med2 != med3:
    print('Escaleno.')