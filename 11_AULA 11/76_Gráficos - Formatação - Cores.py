"""
Gráficos - Formatação - Cores

""""

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
# Gráfico com marcadores diferentes:
# triângulos verdes, círculos vermelhos e asteriscos pretos.
# Sem linhas.
plot(x, y, '^g')
plot(x, y1, 'or')
plot(x, y2, '*k')
