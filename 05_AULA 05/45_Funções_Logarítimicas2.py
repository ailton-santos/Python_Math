"""
Funções - Logarítmicas 2
"""

# Importa função logarítmica (log) da biblioteca math.
# Importa valor da constante e, base do logaritmo natural.
from math import log, e


# Define uma nova função. Neste caso, uma Função Logarítmica.
def calcula_f(x):
    return 2 * log(3 * x, e)


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Chama a função para calcular o valor x = 10.0.
x = 10.0
y = calcula_f(x)

print (u'\n Resultado da função calcula_f para x = 10.0.')
print ('y =', y)

# Chama a função para calcular o valor para x = 0.5.
x = 0.5
y = calcula_f(x)

print (u'\n Resultado da função calcula_f para x = 0.5.')
print ('y =', y)
