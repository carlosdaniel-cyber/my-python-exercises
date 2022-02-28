listnum = [[], []]
for c in range(1, 8):
    v = int(input(f'Digite o {c}º valor: '))
    if v % 2 == 0:
        listnum[0].append(v)
    else:
        listnum[1].append(v)
print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(listnum[0])}')
print(f'Os valores ímpares digitados foram: {sorted(listnum[1])}')
