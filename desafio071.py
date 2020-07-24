print('=' * 30)
print('{:^30}'.format('BANCO CD'))
print('=' * 30)
v = int(input('Que valor você quer sacar? R$'))
tot = v
ced = 50
totced = 0
while True:
    if tot >= ced:
        tot -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédula(s) de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if tot == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CARLOS DANIEL! Tenha um bom dia!')
