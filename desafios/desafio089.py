dados = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2)/2
    dados.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for pos, a in enumerate(dados):
    print(f'{pos:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    op = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if op == 999:
        print('FINALIZANDO...')
        break
    if op <= len(dados) - 1:
        print(f'Notas de {dados[op][0]} são {dados[op][1]}')
print('<<< VOLTE SEMPRE >>>')
