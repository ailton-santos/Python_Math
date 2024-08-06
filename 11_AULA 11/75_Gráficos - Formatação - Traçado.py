"""
Gráficos - Formatação - Traçado

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
y1 = 3 * y
y2 = y ** 2

# Exibe gráfico com várias sequências de pontos.
# Gráfico com linhas diferentes: tracejada, pontilhada e traço-ponto.
# Sem marcadores.
plot(x, y, '--')
plot(x, y1, ':')
plot(x, y2, '-.')
