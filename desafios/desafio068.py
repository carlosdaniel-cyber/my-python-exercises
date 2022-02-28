from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
vencedor = jogador = ''
cont = 0
while True:
    n = int(input('Diga um valor: '))
    print('-' * 40)
    comp = randint(0, 10)
    soma = comp + n
    op = ' '
    while op not in 'PI':
        op = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {n} e o computador {comp}. Total de {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 40)
    if soma % 2 == 0:
        if op == 'P':
            vencedor = jogador
            cont += 1
        else:
            vencedor = comp
    elif soma % 2 == 1:
        if op == 'I':
            vencedor = jogador
            cont += 1
        else:
            vencedor = comp
    if vencedor == jogador:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 20)
    elif vencedor == comp:
        break
print('Você PERDEU!')
print('=-' * 20)
print(f'GAME OVER! Você venceu {cont} veze(s).')
