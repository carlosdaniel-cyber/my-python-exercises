lista = list()
cont = 0
while True:
    v = lista.append(int(input('Digite um valor: ')))
    cont += 1
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
print('-=' * 30)
print(f'Você digitou {cont} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
