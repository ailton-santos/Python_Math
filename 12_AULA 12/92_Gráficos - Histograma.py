"""
Gráficos - Histograma
"""

# Importa todas as funções (*) de elaboração de gráficos da biblioteca pylab.
from pylab import *
# Importa funçãos de geração de números
# aleatórios (random) da biblioteca numpy.
from numpy import random

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores a serem plotados no gráfico.
random.seed(200)
media = 10
desvio_padrao = 3

# Gera 3000 valores aleatórios para apresentar no gráfico.
Valores = media + desvio_padrao * random.randn(3000)

# Define informações no gráfico.
xlabel('Valores')  # Inclui rótulo para eixo horizontal.
ylabel('Probabilidade')  # Inclui rótulo para eixo vertical.
title('Histograma')  # Inclui nome no gráfico.
axis([0, 20, 0, 0.2])  # Define limites dos eixos.
text(1, 0.17, 'Media = 10 , Desvio Padrao = 3')  # Insere texto no gráfico.

# Apresenta histograma.
# 30 - indica em quantos grupos de valores o histograma será dividido.
# normed = 1 - apresenta valores normalizados. Na versão Python 3, esta opção
# não funciona. Foi substituída por: density=True (mesma função).
# facecolor = 'orange' - define cor laranja (orange) para as barras.
hist(Valores, 30, density=True, facecolor='m')
