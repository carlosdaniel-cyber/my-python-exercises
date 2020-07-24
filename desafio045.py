from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
op = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('Computador jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[op]))
print('-='*11)
if comp == 0:
    if op == 0:
        print('EMPATE')
    elif op == 1:
        print('JOGADOR VENCE')
    elif op == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif comp == 1:
    if op == 0:
        print('COMPUTADOR VENCE')
    elif op == 1:
        print('EMPATE')
    elif op == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif comp == 2:
    if op == 0:
        print('JOGADOR VENCE')
    elif op == 1:
        print('COMPUTADOR VENCE')
    elif op == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
