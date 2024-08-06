"""
Gráficos - Pizza

"""

# Importa todas as funções (*) de elaboração de gráficos da biblioteca pylab.
from pylab import *

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores a serem plotados no gráfico.
# Inclui rótulo nos dados.
produtos = ['Prod 1', 'Prod 2', 'Prod 3', 'Prod 4']
quantidade_produtos = [9, 15, 12, 6]
cores = ['m', 'r', 'y', 'g']

# Exibe gráfico de pizza.
# labels = Produtos - inclui rótulo nos itens do gráfico.
# colors=Cores - estabelece as cores.
# radius=1 - define tamanho do gráfico.
# autopct='%.1f%%' - inclui a indicação dos valores percentuais.
# % - indica que será o valor percentual.
# .1f - indica que valor apresentado será ponto flutuante com uma casa decimal.
# % % - inclui símbolo % ao final do valor.
pie(quantidade_produtos, labels=produtos, colors=cores, radius=1,
        autopct='% .1f %%')

title('Grafico de Vendas')  # Inclui nome no gráfico.
