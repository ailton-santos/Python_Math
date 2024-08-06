"""
Gráficos - Barras
"""

# Importa todas as funções (*) de elaboração de gráficos da biblioteca pylab.
from pylab import *

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores a serem plotados no gráfico.
valores = [5, 16, 10, 22]
x = [1, 2, 3, 4]

# Exibe gráfico de barras.
# Width - largura das barras.
# align = 'center' - Posiciona rótulo no meio das barras.
bar(x, valores, width=0.5, align='center')

xlabel('Valores')  # Inclui rótulo para eixo horizontal.
ylabel('Unidade')  # Inclui rótulo para eixo vertical.
title('Grafico de Barras')  # Inclui nome no gráfico.
axis([0, 5, 0, 30])  # Define a faixa de valores dos eixos do gráfico.
