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


def moeda(valor=0.0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
