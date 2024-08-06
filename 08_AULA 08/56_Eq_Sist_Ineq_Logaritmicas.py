"""
Solução de Equações - Logarítmicas 2

"""

# Importa Symbol - possibilidade de operações com símbolos.
# Importa solve - permite solução de equações.
# Importa função logarítmica (log).
from sympy import Symbol, solve, log


# Define uma nova função.
def my_function(x):
    return log(2 * x + 3, x) - 2


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Resolve a equação my_function = 0.
y = my_function(x)

resultado = solve(y)

print (u'\n Resultado da equação log(2*x + 3,x) - 2 = 0.')
print ('x =', resultado)
