"""
Gráficos - Formatação - Legenda
"""

# Importa função de elaboração de gráficos da biblioteca pylab.
# Função plot para plotar o gráfico.
# Função arange para definir as faixas de valores.
# Funções legend para incluir legenda.
from pylab import plot, arange, legend

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores a serem plotados no gráfico.
x = arange(0, 4, 0.5)  # Faixa de valores para x.
y = 2 * x
y1 = 3 * y
y2 = y ** 2

# Exibe gráfico com várias sequências de pontos.
# Gráfico com marcadores e linhas diferentes:
# círculos e linha tracejada verdes
# cruzes e linha pontilhada vermelhas
# quadrados e linha tracejada pretos.
# Inclui legenda. Os rótulos são associados na ordem em cada linha "plot".
plot(x, y, 'g8--', label='Linha_1')
plot(x, y1, 'r+:', label='Linha_2')
plot(x, y2, 'bs--', label='Linha_3')
legend(loc=2)  # Define posição da legenda.
