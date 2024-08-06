"""
Gráficos - Função Trigonométrica
"""

# Importa função sin (seno) e constante pi da bilbioteca math.
from math import sin, pi
# Importa todas as funções (*) de elaboração de gráficos da biblioteca pylab.
from pylab import *


# Define uma nova função.
def calcula_f(x):
    return 2 * sin(x / 2 + pi / 3)


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define faixa de valores da variável independente x.
# Neste caso x varia de 0 a 6*pi+pi/3, com passo de 0.01.
x = arange(0.0, 6 * pi + pi / 3, 0.01)

# Faz y igual à função.
y = calcula_f(x)

# Exibe gráfico com rótulos e grid.

plot(x, y)

xlabel('Variavel Independente x')  # Inclui rótulo para eixo horizontal.
ylabel('Funcao y = f(x)')  # Inclui rótulo para eixo vertical.
title('Funcao Trigonometrica y = 2sin(x/2 + pi/3)')  # Inclui nome no gráfico.
grid(True)  # Inclui o grid no gráfico.
# Define a faixa de valores dos eixos do gráfico.
# x de 0 a 20. y de -2.5 a 2.5.
axis([0, 20, -2.5, 2.5])
