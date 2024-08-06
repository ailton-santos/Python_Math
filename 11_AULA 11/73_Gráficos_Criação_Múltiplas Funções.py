"""
Gráficos - Criação - Múltiplas Funções

"""

# Importa função de elaboração de gráficos da biblioteca pylab.
# Função plot para plotar o gráfico.
# Função arange para definir as faixas de valores.
from pylab import plot, arange

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores a serem plotados no gráfico.
x = arange(0, 4, 0.5)  # Faixa de valores para x.
y = 2 * x
y1 = 6 * x
y2 = x**2

# Exibe gráfico com várias sequências de pontos.
# Valores de x apresentados no eixo horizontal.
# Valores de y, y1 e y2 apresentados no eixo vertical.
plot(x, y, x, y1, x, y2)
