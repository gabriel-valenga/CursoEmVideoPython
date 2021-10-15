largura = float(input('Qual a largura da parede?'))
altura = float(input('Qual a altura da parede?'))
area = largura * altura
quantidadeTinta = area / 2
print('Área da parede: {}m², quantidade de tinta necessária: {:.3f} litros'.format(area,quantidadeTinta))