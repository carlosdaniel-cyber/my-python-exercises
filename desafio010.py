x = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${:.2f} você pode comprar US${:.2f} ou €{:.2f}.'.format(x, x/5.59, x/6.05))
