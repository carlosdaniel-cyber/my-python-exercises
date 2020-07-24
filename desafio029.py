v = float(input('Qual a velocidade atual do carro? '))
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format((v - 80)*7))
print('Tenha um bom dia! Dirija com segurança!')
