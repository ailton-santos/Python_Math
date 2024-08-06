"""
Gráficos - Escala Log - Eixo Vertical

"""

# Importa função de elaboração de gráficos da biblioteca pylab.
# Função plot para plotar o gráfico.
# Função arange para definir as faixas de valores.
# Função yscale para alterar escala do eixo vertical.
from pylab import plot, arange, yscale

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores a serem plotados no gráfico.
x = arange(0, 4, 0.5)  # Faixa de valores para x.
y = x ** 8

# Exibe gráfico com uma sequência de pontos.
# Eixo das ordenadas em escala logarítmica.
plot(x, y)

yscale('log')  # Altera escala do eixo vertical para logarítmica.
