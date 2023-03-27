# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while

pa1 = eval(input('Digite o primeiro termo da PA: '))
razao = eval(input('Digite a razão: '))

termo = pa1
contador = 0

while contador <= 10:
    print(termo, end=' -> ')
    contador += 1
    termo += razao
print('ACABOU!')