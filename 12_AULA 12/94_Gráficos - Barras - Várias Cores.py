"""
Gráficos - Barras - Várias Cores
"""

# Importa todas as funções (*) de elaboração de gráficos da biblioteca pylab.
from pylab import *

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores a serem plotados no gráfico.
# Inclui rótulo nos dados. Alterna cor das barras.
valores = [5, 16, 10, 22]
x = [1, 2, 3, 4]
rotulo_barras = ['Prod 1', 'Prod 2', 'Prod 3', 'Prod 4']

# Exibe gráfico de barras.
# tick_label = Rotulo_Barras - Inclui nome dos
# itens representados pelas barras.
# color = ['r','g'] - Alterna cores das barras: vermelho e verde.
# Width - largura das barras.
# align = 'center' - Posiciona rótulo no meio das barras.
bar(
    x, valores, tick_label=rotulo_barras, width=0.4,
    align='center', color=['r', 'g'])

xlabel('Produtos')  # Inrclui rótulo para eixo horizontal.
ylabel('Unidades')  # Inclui rótulo para eixo vertical.
title('Grafico de Vendas')  # Inclui nome no gráfico.
axis([0, 5, 0, 30])  # Define a faixa de valores dos eixos do gráfico.
grid(True, axis='y')  # Inclui somente linhas horizontais no grid.
