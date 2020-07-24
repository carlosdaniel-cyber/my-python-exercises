v = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
t = int(input('Quantos anos de financiamento: '))
p = v/(t * 12)
print('Para comprar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(v, t, p))
if p > (30/100) * s:
    print('Emprétimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
