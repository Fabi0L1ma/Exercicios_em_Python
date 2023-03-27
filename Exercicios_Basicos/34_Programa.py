"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. -Para salários superiores
a R$1.250,00, calcule um aumento de 10%. -Para os inferiores ou iguais, o aumento é de 15%."""

sal = eval(input('Digite o salário do funcionario: R$'))

sal_M = (sal * 10) / (100) + sal
sal_m = (sal * 15) / (100) + sal
if sal >= 1250:
    print('O salario de R${:.2f} receberá o aumento de 10% e ficará no valor de R${:.2f}'.format(sal, sal_M))
else:
    if sal < 1250:
        print('O salario de R${:.2f} recebra o aumento de 15% e ficará no valor de R${:.2f}'.format(sal, sal_m))
