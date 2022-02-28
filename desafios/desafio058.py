from random import randint
totpalp = 0
palp = -1
comp = randint(0, 10)
print("""Sou seu computador...
Acabei de pensar em um número entre 0 e 10
Será que você consegue adivinhar qual foi?""")
while palp != comp:
    palp = int(input('Qual é seu palpite? '))
    totpalp += 1
    if palp < comp:
        print('Mais... Tente mais uma vez.')
    elif palp > comp:
        print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(totpalp))
"""
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print('Mais... Tente mais uma vez.')
        elif jogador > comp:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(totpalp))
"""