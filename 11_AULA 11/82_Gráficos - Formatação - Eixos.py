"""
Gráficos - Formatação - Eixos sem Borda
"""

# Importa função de elaboração de gráficos da biblioteca pylab.
# Função arange para definir as faixas de valores.
# Funções xlabel e ylabel para incluir rótulos nos eixos.
# Função title para incliur nome do gráfico.
# Função subplots para retirar contornos.
from pylab import arange, xlabel, ylabel, title, subplots

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores a serem plotados no gráfico.
x = arange(-2, 4, 0.5)  # Faixa de valores para x.
y = 3 * x

# Exibe gráfico com rótulos e grid.
# Exibe somente eixos nas origens.

fig, ax = subplots()

# Plota a função no gráfico.
ax.plot(x, y)

# Inclui o grid no gráfico.
ax.grid(True, which='both')

# Muda apresentação geral do gráfico.
# Em vez de colocar o gráfico dentro de uma "caixa",
# exibe somente os eixos na origem.
# A caixa considera os quatro cantos do contorno:
# esquerda, direita, inferior e superior.
ax.spines['left'].set_position('zero')  # Define contorno da esquerda em x = 0.
ax.spines['bottom'].set_position('zero')  # Define contorno inferior em y = 0.

ax.spines['right'].set_color('none')  # Não exibe linha de contorno da direita.
ax.spines['top'].set_color('none')  # Não exibe linha de contorno superior.

ax.yaxis.tick_left()  # Exibe marcação no eixo vertical.
ax.xaxis.tick_bottom()  # Exibe marcação no eixo horizontal.

# Inclui rótulo para eixo horizontal. Ajusta posição do rótulo.
xlabel(
    'Variavel Independente x', horizontalalignment='right', position=(1, 10))
# Inclui rótulo para eixo vertical. Ajusta posição do rótulo.
ylabel('Funcao y = 3x', verticalalignment='center', position=(1, 0.7))
title('Nome do Grafico')  # Inclui nome no gráfico.
