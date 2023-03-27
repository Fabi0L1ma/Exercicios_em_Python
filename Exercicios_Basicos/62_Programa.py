# Molhere o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
#ele disser que quer mostrar 0 TERMOS.

pa1 = eval(input('Digite o primeiro termo: '))
razao = eval(input('Digite a razão: '))

termo = pa1
cont = 1
total = 0
opc = 10

while opc != 0:
    total = total + opc
    while cont <= total:
        print(termo, end=' -> ')
        cont += 1
        termo += razao
    print('PAUSA!')
    opc = eval(input('Gostaria de mostrar mais quantos termos? '))
print('FIM!')
