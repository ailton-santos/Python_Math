"""

Gráficos - Barras Horizontais

"""

# Importa todas as funções (*) de elaboração de gráficos da biblioteca pylab.
from pylab import *

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores a serem plotados no gráfico.
quantidades = [5, 16, 10, 22]
x = [1, 2, 3, 4]

# Exibe gráfico de barras horizontais.
barh(x, quantidades, align='center')

# Estabelece rótulo para os valores mostrados no gráfico.
yticks(x, ('A', 'B', 'C', 'D'))

# Estabele rótulo para os eixos e o gráfico.
xlabel('Quantidades')  # Inclui rótulo para eixo horizontal.
ylabel('Classe')  # Inclui rótulo para eixo vertical.
title('Grafico de Barras Horizontais')  # Inclui nome no gráfico.
