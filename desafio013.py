x = float(input('Qual é o sálario do funcionário? R$'))
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(x, x+x*15/100))
