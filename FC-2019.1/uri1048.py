s = float(input())
if 0 <= s <= 400:
    print('Novo salário: {:.2f}'.format(s + (s * (15/100))))
    print('Reajuste ganho: {:.2f}'.format(s * 0.15))
    print('Em percentual: 15 %')
elif 400.01 <= s <= 800:
    print('Novo salário: {:.2f}'.format(s + (s * (12/100))))
    print('Reajuste ganho: {:.2f}'.format(s * 0.12))
    print('Em percentual: 12 %')
elif 800.01 <= s <= 1200:
    print('Novo salário: {:.2f}'.format(s + (s * (10/100))))
    print('Reajuste ganho: {:.2f}'.format(s * 0.1))
    print('Em percentual: 10 %')
elif 1200.01 <= s <= 2000:
    print('Novo salário: {:.2f}'.format(s + (s * (7/100))))
    print('Reajuste ganho: {:.2f}'.format(s * 0.07))
    print('Em percentual: 7 %')
else:
    print('Novo salário: {:.2f}'.format(s + (s * (4/100))))
    print('Reajuste ganho: {:.2f}'.format(s * 0.04))
    print('Em percentual: 4 %')
