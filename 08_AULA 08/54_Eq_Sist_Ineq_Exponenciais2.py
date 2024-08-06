"""
Solução de Equações - Exponenciais 2

"""

# Importa Symbol - possibilidade de operações com símbolos.
# Importa solve - permite solução de equações.
# Importa função exp.
from sympy import Symbol, solve, exp


# Define uma nova função.
def calcula_f(x):
    return exp(2 * x + 1) * exp(-3 * x + 4) - 1


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Resolve a equação calcula_f = 0.
y = calcula_f(x)

resultado = solve(y)

print (u'\n Resultado da equação exp(2*x + 1) * exp(-3*x + 4) - 1.')
print ('x =', resultado)
