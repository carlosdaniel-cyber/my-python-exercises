def aumentar(valor=0, taxa=0, fmt=False):
    res = valor + (valor * taxa/100)
    return moeda(res) if fmt else res


def diminuir(valor=0, taxa=0, fmt=False):
    res = valor - (valor * taxa / 100)
    return moeda(res) if fmt else res


def dobro(valor=0, fmt=False):
    res = valor * 2
    return moeda(res) if fmt else res


def metade(valor=0, fmt=False):
    res = valor / 2
    return moeda(res) if fmt else res


def moeda(valor=0.0, currency='R$'):
    return f'{currency}{valor:.2f}'.replace('.', ',')


def resumo(valor=0, red=0, aum=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aum} % de aumento: \t{aumentar(valor, aum, True)}')
    print(f'{red} % de redução: \t{diminuir(valor, red, True)}')
    print('-' * 30)
