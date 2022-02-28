d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar auma viagem de {}Km'.format(d))
""" 
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
"""
p = d * 0.50 if d <= 200 else d * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(p))
