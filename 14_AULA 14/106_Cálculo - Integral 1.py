"""
Cálculo - Integral 1

"""

# Importa operação Integral da biblioteca sympy.
# Importa Symbol - possibilidade de operações com símbolos.
from sympy import Integral, Symbol


# Define uma nova função.
def calcula_f(x):
    return 2 * x + 6


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Calcula a integral indefinida da função calcula_f.
resultado = Integral(calcula_f(x), x).doit()

print (u'\n Integral indefinida da função calcula_f.')
print (resultado)
