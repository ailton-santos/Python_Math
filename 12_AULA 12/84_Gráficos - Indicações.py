"""
Gráficos - Indicações
"""

# Importa função de elaboração de gráficos da biblioteca pylab.
# Função plot para plotar o gráfico.
# Função arange para definir as faixas de valores.
# Funções xlabel e ylabel para incluir rótulos nos eixos.
# Função title para incliur nome do gráfico.
# Função grid para fazer o grid no gráfico.
from pylab import plot, arange, xlabel, ylabel, title, grid, annotate

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores a serem plotados no gráfico.
x = arange(0, 4, 0.5)  # Faixa de valores para x.
y = 3 * x

# Exibe gráfico uma sequência de pontos.
plot(x, y, '^')

xlabel('Variavel Independente x')  # Inclui rótulo para eixo horizontal.
ylabel('Funcao y = 3x')  # Inclui rótulo para eixo vertical.
title('Nome do Grafico')  # Inclui nome no gráfico.
grid(True)  # Inclui o grid no gráfico.

# Inclui as setas com texto para indicar pontos específicos.
annotate(
    'Ponto 1', xy=(1.5, 3 * 1.5), xytext=(2.5, 3),
    arrowprops=dict(facecolor='k', shrink=0.1))
annotate(
    'Ponto 2', xy=(2.5, 3 * 2.5), xytext=(1.5, 9),
    arrowprops=dict(facecolor='k', shrink=0.1))
