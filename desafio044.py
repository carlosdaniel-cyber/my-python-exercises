print(f"{' LOJAS DANIEL ':=^40}")
p = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual é a opção? '))
if op == 1:
    total = p - (p*0.1)
elif op == 2:
    total = p - (p*0.05)
elif op == 3:
    total = p
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(parcela))
elif op == 4:
    np = int(input('Quantas parcelas? '))
    total = p + (p*0.2)
    parcela = total / np
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(np, parcela))
else:
    total = p
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(p, total))
