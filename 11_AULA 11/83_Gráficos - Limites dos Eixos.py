"""
Gráficos - Limites dos Eixos
"""

# Importa função de elaboração de gráficos da biblioteca pylab.
# Função plot para plotar o gráfico.
# Função arange para definir as faixas de valores.
# Funções xlabel e ylabel para incluir rótulos nos eixos.
# Função title para incliur nome do gráfico.
# Função grid para fazer o grid no gráfico.
# Função axis para definir faias de valores no gráfico.
from pylab import plot, arange, xlabel, ylabel, title, grid, axis

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores a serem plotados no gráfico.
x = arange(0, 4, 0.5)  # Faixa de valores para x.
y = 3 * x

# Exibe gráfico com uma sequência de pontos.
plot(x, y, 'v')

xlabel('Variavel Independente x')  # Inclui rótulo para eixo horizontal.
ylabel('Funcao y = 3x')  # Inclui rótulo para eixo vertical.
title('Nome do Grafico')  # Inclui nome no gráfico.
grid(True)  # Inclui o grid no gráfico.
# Define a faixa de valores dos eixos do gráfico.
# x de -4 a 3. y de -7 a 7.
axis([-4, 3, -7, 7])
