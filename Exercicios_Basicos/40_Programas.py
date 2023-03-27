'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingia:

-Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9:RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO.
'''

nota1 = eval(input('Digite a primeira nota:'))
nota2 = eval(input('Digite a segunda nota:'))

med = (nota1 + nota2)/2

if med < 5.0:
    print('Nota:{} \nREPROVADO!'.format(med))
elif med < 7.0 or med == 5.0:
    print('Nota:{} \nRECUPERAÇÃO!'.format(med))
elif med >= 7.0:
    print('Nota:{} \nAPROVADO!'.format(med))