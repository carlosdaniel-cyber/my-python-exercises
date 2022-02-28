print('-' * 40)
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print('-' * 40)
tot = cont1000 = menor = cont = 0
barato = ''
while True:
    n = str(input('Nome do Produto: '))
    p = float(input('Preço: R$'))
    cont += 1
    tot += p
    if p > 1000.00:
        cont1000 += 1
    if cont == 1 or p < menor:
        menor = p
        barato = n
        """if cont == 1:
        menor = p
        barato = n
    else:
        if p < menor:
            menor = p
            barato = n"""
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {cont1000} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
