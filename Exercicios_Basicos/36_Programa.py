'''Escreva um programa para aprovar o emprèstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
casa, o salário do comprador e em quantos anos ele vai pagar.

- Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo sera negado.'''

val_c = eval(input('Digite o valor da casa: R$'))
sal_p = eval(input('Digite o seu salário: R$'))
anos_p = eval(input('Em quantos anos o senhor deseja realizar o pagamento?'))

cal_pre = (sal_p * 30)/100
pre_c = val_c / (anos_p*12)

print('Para pagar uma casa de R${:.2f} em {} anos'.format(val_c, anos_p))
print('a prestação será de R${:.2f}'.format(pre_c))

if pre_c > cal_pre:
    print('EMPRESTIMO NEGADO!')

elif pre_c <= cal_pre:
    print('EMPRÉSTIMO APROVADO!')