from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
a = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - a
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['contratação'] - a + 35
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
