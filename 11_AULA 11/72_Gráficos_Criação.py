"""
Gráficos - Criação
"""

# Importa função de elaboração de gráficos da biblioteca pylab.
# Função plot para plotar o gráfico.
from pylab import plot

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores a serem plotados no gráfico.
x = [0, 1, 2, 3, 4]
y = [1, 3, 7, 9, 15]

# Exibe gráfico.
# Valores de x apresentados no eixo horizontal.
# Valores de y apresentados no eixo vertical.
plot(x, y)
