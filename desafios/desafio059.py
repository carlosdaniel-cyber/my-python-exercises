from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    op = int(input('>>>>> Qual é a sua opção? '))
    if op == 1:
        s = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, s))
    elif op == 2:
        m = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, m))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif op == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-'*20)
    sleep(1)
print('Fim do programa! Volte sempre!')
