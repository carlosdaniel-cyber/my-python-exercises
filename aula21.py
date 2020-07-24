help(input)
print(input.__doc__)


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    # Doc_string
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador)


def soma(a=0, b=0, c=0):
    # Parâmetros Opcionais
    s = a + b + c
    print(f'A soma vale {s}')


soma(3, 2, 5)
soma(8, 4)
soma()


def teste():
    x = 8   # Variável Local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x val {x}')


n = 2   # Variável Global
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')


def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 global vale {n1}')


def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')


def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(6)
print(f'Os resultados foram {r1}, {r2} e {r3}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
