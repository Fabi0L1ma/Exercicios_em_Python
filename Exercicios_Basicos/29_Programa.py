"""Escreva um programa que leia a velocidade de um carro. -Se ele ultrapassar 80Km/,mostre uma menssagem dizendo
 que ele foi multado.
-A multa vai custar R$7,00 por cada Km acima do limite."""

vel_car = eval(input('Qual foi a velocidade do carro ?'))

if vel_car > 80:
    val_mul = (vel_car - 80) * 7.00
    print('Sua velocidade é de {}KM e você foi multado no valor de R${:.2f}'.format(vel_car, val_mul))
else:
    print('Você não foi multado!')