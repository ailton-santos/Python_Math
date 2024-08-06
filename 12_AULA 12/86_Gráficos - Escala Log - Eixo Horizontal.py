"""
Gráficos - Escala Log - Eixo Horizontal

"""

# Importa função de elaboração de gráficos da biblioteca pylab.
# Função plot para plotar o gráfico.
# Função arange para definir as faixas de valores.
# Função xscale para alterar escala do eixo horizontal.
from pylab import plot, arange, xscale

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores a serem plotados no gráfico.
x = arange(0, 10000, 10)  # Faixa de valores para x.
y = x ** (1.0 / 8)

# Exibe gráfico com uma sequência de pontos.
# Eixo das ordenadas em escala logarítmica.
plot(x, y)

xscale('log')  # Altera escala do eixo horizontal para logarítmica.
