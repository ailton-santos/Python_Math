"""
Gráficos - Função Logarítmica
"""

# Importa função logarítmica da biblioteca numpy.
# Função arange para definir as faixas de valores.
from numpy import log10, arange
# Importa função de elaboração de gráficos da biblioteca pylab.
# Função plot para plotar o gráfico.
# Funções xlabel e ylabel para incluir rótulos nos eixos.
# Função title para incliur nome do gráfico.
# Função grid para fazer o grid no gráfico.
from pylab import plot, xlabel, ylabel, title, grid


# Define uma nova função.
def calcula_f(x):
    return 3 * log10(x ** 2)


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define faixa de valores da variável independente x.
# Neste caso x varia de 1.0 a 9.0, com passo de 0.01.
x = arange(1.0, 9.0, 0.01)

# Faz y igual à função.
y = calcula_f(x)

# Exibe gráfico com rótulos e grid.
plot(x, y)

xlabel('Variavel Independente x')  # Inclui rótulo para eixo horizontal.
ylabel('Funcao y = f(x)')  # Inclui rótulo para eixo vertical.
title('Funcao Logaritmica y = 3*log10(x**2)')  # Inclui nome no gráfico.
grid(True)  # Inclui o grid no gráfico.
