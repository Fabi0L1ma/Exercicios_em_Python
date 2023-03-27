'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
de pagamento:

- À vista dinheiro/cheque: 10% de desconto;
- À vista no cartão: 5% de desconto;
- Em até 2x no cartão: Preço normal;
- 3x ou mais no cartão: 20% de juros.
'''

valor_p = eval(input('Digite o valor a ser pago:R$'))

print('Selecione a forma de pagamento:')
escolha = eval(input('1- A vista DINHEIRO/CHEQUE \n2- A vista no CARTÃO \n3- Até 2x no CARTÃO \n4- 3x ou mais no CARTÃO \nESCOLHA:'))


v_dc = valor_p - (valor_p*10)/100
v_c = valor_p - (valor_p*5)/100
v_cx3 = valor_p + (valor_p*20)/100

if escolha == 1:
    print('Você terá 10% de desconto e o valor a ser pago será de R${:.2f}'.format(v_dc))
elif escolha == 2:
    print('VocÊ terá 5% de desconto e o valor a ser pago será de R${:.2f}'.format(v_c))
elif escolha == 3:
    print('Você parcelará em 2x e pagará o preço normal que será de R${:.2f}'.format(valor_p/2))
elif escolha == 4:
    parcelas = eval(input('Quantidade de parcelas:'))
    print('Você parcelará o valor em {}x, tera um juros de 20% e o valor a ser pago será de R${:.2f}'.format(parcelas, v_cx3/parcelas))





