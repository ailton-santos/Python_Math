"""
Solução de Equações - Logarítmicas 1
"""

# Importa Symbol - possibilidade de operações com símbolos.
# Importa solve - permite solução de equações.
# Importa função logarítmica (log).
from sympy import Symbol, solve, log


# Define uma nova função.
def calcula_f(x):
    return log(3 * x + 2, 4) - log(2 * x + 5, 4)


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Resolve a equação calcula_f = 0.
y = calcula_f(x)

resultado = solve(y)

print (u'\n Resultado da equação log(3*x + 2,4) - log(2*x + 5,4) = 0.')
print ('x =', resultado)
