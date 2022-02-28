s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('Voê informou {} número(s) PAR(ES) e a soma é igual a {}'.format(cont, s))
