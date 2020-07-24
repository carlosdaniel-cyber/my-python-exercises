print('='*20)
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
"""décimo = pt + (10 - 1) * r"""
for c in range(pt, pt + (r*10), r):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
