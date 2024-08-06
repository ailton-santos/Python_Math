"""

Cálculo Numérico - Análise Gráfica
"""

# Importa função de elaboração de gráficos da biblioteca pylab.
from pylab import *


# Define uma nova função.
def calcula_f(x):
    return x ** 3 + 5 * x ** 2 - 5 * x - 12


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define faixa de valores da variável independente x.
x = arange(-6, 5, 0.01)  # Neste caso x varia de -2 a 5, com passo de 0,01.

# Faz y igual à função.
y = calcula_f(x)

# Exibe gráfico com rótulos e grid.
plot(x, y)

xlabel('Variavel Independente x')  # Inclui rótulo para eixo horinzontal.
ylabel('Funcao y = f(x)')  # Incliu rótulo para eixo vertical.
title('Funcao y = x**3 + 5*x**2 - 5*x - 12')  # Incliu nome no gráfico.
grid(True)  # Incliu o grid no gráfico.
