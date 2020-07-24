print('-=' * 15)
tb = ('Palmeiras', 'Santos', 'Flamengo', 'Internacional', 'Atlético Mineiro',
      'Goiás', 'Botafogo', 'Bahia', 'São Paulo', 'Conrinthias', 'Grêmio',
      'Athletico-PR', 'Ceará', 'Fortaleza', 'Vasco da Gama', 'Fluminense',
      'Chapecoense', 'Cruzeiro', 'CSA', 'Avaí')
print(f'Lista de times do Brasileirão: {tb}')
"""for t in tb:
      print(t)"""
print('-=' * 15)
print(f'Os 5 primeiros são {tb[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {tb[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(tb)}')
print('-=' * 15)
print(f'O Chapeoense está na {tb.index("Chapecoense") + 1}ª posição')
