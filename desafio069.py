contm = contf = cont = 0
while True:
    print('-' * 30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 30)
    if i >= 18:
        cont += 1
    if s == 'M':
        contm += 1
    if s == 'F' and i < 20:
        contf += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {contm} homens cadastrados')
print(f'E temos {contf} mulheres com menos de 20 anos')
