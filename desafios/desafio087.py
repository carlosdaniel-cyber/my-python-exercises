matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = soma3c = maior2L = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
        if c == 2:
            soma3c += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior2L:
                maior2L = matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {somapares}')
"""for l in range(0, 3):
    soma3c += matriz[l][2]"""
print(f'A soma dos valores da terceira coluna é {soma3c}.')
"""for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior2L:
        maior2L = matriz[1][c]"""
print(f'O maior valor da segunda linha é {maior2L}.')
