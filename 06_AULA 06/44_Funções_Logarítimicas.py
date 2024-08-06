"""
Funções - Logarítmicas

Autor: Ailton Dos Santos
"""

# Importa função logarítmica (log) da biblioteca math.
from math import log


# Define uma nova função. Neste caso, uma Função Logarítmica.
def calcula_f(x, a):
    return 3 * log(x / 2, a)


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Chama a função para calcular o valor para base a = 10 e x = 25.0.
x = 25.0
a = 10
y = calcula_f(x, a)

print (u'\n Resultado da função calcula_f para base a = 10 e x = 25.0.')
print ('y =', y)

# Chama a função para calcular o valor para base a = 3 e x = 2.5.
x = 2.5
a = 3
y = calcula_f(x, a)

print (u'\n Resultado da função calcula_f para base a = 3 e x = 2.5.')
print ('y =', y)
