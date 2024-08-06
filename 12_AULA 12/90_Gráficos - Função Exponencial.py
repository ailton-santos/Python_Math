"""
Gráficos - Função Exponencial
"""

# Importa função exponencial (exp) da biblioteca math.
from math import exp
# Importa todas as funções (*) de elaboração de gráficos da biblioteca pylab.
from pylab import *


# Define uma nova função.
def calcula_f(x):
    return 2 * exp(-x / 4)


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define faixa de valores da variável independente x.
x = arange(-1, 9, 0.01)  # Neste caso x varia de -1 a 9, com passo de 0.01.

# Faz y igual à função.
y = calcula_f(x)

# Exibe gráfico com rótulos e grid.
plot(x, y)

xlabel('Variavel Independente x')  # Inclui rótulo para eixo horizontal.
ylabel('Funcao y = f(x)')  # Inclui rótulo para eixo vertical.
title('Funcao Exponencial y = 2*exp(-x/4)')  # Inclui nome no gráfico.
grid(True)  # Inclui o grid no gráfico.
