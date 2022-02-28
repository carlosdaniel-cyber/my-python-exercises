print('Gerador de PA')
print('-='*10)
pt = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = pt
cont = 1
total = 0
nt = 10
while nt != 0:
    total += nt
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    nt = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
