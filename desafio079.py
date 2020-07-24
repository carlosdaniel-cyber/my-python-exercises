listnum = list()
while True:
    v = int(input('Digite um valor: '))
    if v not in listnum:
        listnum.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print('-=' * 25)
print(f'Você digitou os valores {sorted(listnum)}')
