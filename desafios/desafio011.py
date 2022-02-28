x = float(input('Largura da parede: '))
y = float(input('Altura da parede: '))
z = x*y
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².\nPara pintar essa parede, você precisará de{:.2f}L de tinta.'.format(x, y, z, z/2))
