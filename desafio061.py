print('Gerador de PA')
print('-='*10)
pt = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
n = 1
"""termo = pt
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' -> ')
    termo += r
    cont += 1"""
while n <= 10:
    pa = pt + (n - 1) * r
    n += 1
    print('{}'.format(pa), end=' -> ')
print('FIM')
