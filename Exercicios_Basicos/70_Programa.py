# Crie um programa que leia o NOME e o PREÇO de VÁRIOS PRODUTOS. O programa deverá perguntar se o USUÁRIO vai continuar.
#No final, mostre:

# 1 - Qual é o TOTAL GASTO na compra.
# 2 - Quantos produtos custam MAIS de R$1000.
# 3 - Qual é o NOME do produto mais BARATO.

total_g = 0
produtos_mais_mil = 0
nome_produto_barato = 0
cont = 0


while True:
    nome_produto = str(input('Digite o nome do produto: '))
    valor_produto = eval(input('Digite o valor do produto: R$'))

    total_g += valor_produto
    cont += 1

    if valor_produto > 1000:
        produtos_mais_mil += 1

    if cont == 1:
        nome_produto_barato = valor_produto
    else:
        if valor_produto < nome_produto_barato:
            nome_produto_barato = valor_produto

    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if pergunta == 'N':
        break

print('\nTotal da compra: R${:.2f}'.format(total_g))
print('Números de produtos custando mais de R$1000 = {} UND'.format(produtos_mais_mil))
print('Produto mais barato custa: R${:.2f} '.format(nome_produto_barato))



