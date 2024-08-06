"""
Funções - Mista
"""

# Importa funções exp (exponencial) e sin (seno) da biblioteca math.
from math import exp, sin


# Define uma nova função. Neste caso, uma Função Logarítmica.
def calcula_f(x):
    return 2 * exp(x / 2) - 3 * sin(x) + 2 * x**3 - 5


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Chama a função para calcular o valor para x = 3.0.
x = 3.0
y = calcula_f(x)

print (u'\n Resultado da função calcula_f para x = 3.0.')
print ('y =', y)
