"""

Gráficos - Formatação - Texto

"""

# Importa função de elaboração de gráficos da biblioteca pylab.
# Função plot para plotar o gráfico.
# Função arange para definir as faixas de valores.
# Funções text para incluir texto.
from pylab import plot, arange, text

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores a serem plotados no gráfico.
x = arange(0, 4, 0.5)  # Faixa de valores para x.
y = 3 * x

# Exibe gráfico com uma sequência de pontos.
plot(x, y, 'd')

# Inclui texto no gráfico. Posição do texto definida pelos valores 1 e 13.
# Texto inicia na posição 1 do eixo horizontal.
# Texto inicia na posição 10 do eixo vertical.
text(1, 10, u'Inclui texto no gráfico')
