while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 35)
    cont = 0
    if n < 0:
        break
    while cont <= 9:
        cont += 1
        print(f'{n} x {cont:2} = {n * cont}')
    print('-' * 35)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
