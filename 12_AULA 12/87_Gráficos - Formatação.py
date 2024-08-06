"""
Gráficos - Formatação

"""

# Importa função de elaboração de gráficos da biblioteca pylab.
# Função plot para plotar o gráfico.
# Função arange para definir as faixas de valores.
# Função yscale para alterar escala do eixo vertical.
# Função title para incluir nome no gráfico.
# Funções figure e subplot para exibir mais de um gráfico.
from pylab import plot, arange, yscale, subplot, title

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores a serem plotados no gráfico.
x = arange(0, 4, 0.5)  # Faixa de valores para x.
y = 2 * x
y1 = 3 * y
y2 = y ** 2

# Exibe gráfico com várias sequências de pontos.
# Gráfico com triângulos verdes, círculos vermelhos e traços azuis.

subplot(121)
plot(x, y, 'g^', x, y1, 'rd', x, y2, 'b*')
title('Grafico 1')

subplot(122)
yscale('log')  # Muda escala do eixo vertical para log.
plot(x, y, 'mv', x, y1, 'wo', x, y2, 'k8')
title('Grafico 2 - Eixo y Esc Log')
