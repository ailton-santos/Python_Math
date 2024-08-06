"""
Gráficos - Formatação - Eixos

"""

# Importa função de elaboração de gráficos da biblioteca pylab.
# Função plot para plotar o gráfico.
# Função arange para definir as faixas de valores.
# Funções xlabel e ylabel para incluir rótulos nos eixos.
# Função title para incliur nome do gráfico.
# Função grid para fazer o grid no gráfico.
# Funções axhline e axvline para incluir eixos nas origens.
from pylab import plot, arange, xlabel, ylabel, title, grid, axhline, axvline

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores a serem plotados no gráfico.
x = arange(-2, 4, 0.5)  # Faixa de valores para x.
y = 3 * x

# Exibe gráfico.
plot(x, y)

xlabel('Variavel Independente x')  # Inclui rótulo para eixo horizontal.
ylabel('Funcao y = 3x')  # Inclui rótulo para eixo vertical.
title('Nome do Grafico')  # Inclui nome no gráfico.
grid(True)  # Inclui o grid no gráfico.

# Inclui os eixos na origem - x = 0 e y = 0.
axhline(y=0, color='k')  # Traça uma linha horizontal em y = 0.
axvline(x=0, color='k')  # Traça uma linha vertical em x = 0.
