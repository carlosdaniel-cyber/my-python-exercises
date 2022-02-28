"""pessoas = {'nome': 'Carlos', 'sexo': 'M', 'idade': 18}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.items())
pessoas['peso'] = 60
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')

Brasil = []
estado1 = {'uf': 'Maranhão', 'sigla': 'MA'}
estado2 = {'uf': 'Ceará', 'sigla': 'CE'}
Brasil.append(estado1)
Brasil.append(estado2)
print(Brasil[1]['sigla'])
"""
estado = dict()
Brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    Brasil.append(estado.copy())
for e in Brasil:
    for v in e.values():
        print(v, end=' ')
    print()
