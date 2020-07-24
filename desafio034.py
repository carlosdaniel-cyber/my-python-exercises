s = float(input('Qual é o salário do funcionário? R$'))
"""
n = s + s * 0.15 if s <= 1250 else s + s *0.1
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(s, n))
"""
if s <= 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(s, s + s * 0.15))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(s, s + s * 0.1))
