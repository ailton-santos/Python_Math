"""
Solução de Equações - Logarítmicas 3


"""

# Importa Symbol - possibilidade de operações com símbolos.
# Importa solve - permite solução de equações.
# Importa função logarítmica (log).
from sympy import Symbol, solve, log


# Define uma nova função.
def calcula_f(x):
    return x ** (log(x + 3, x)) - 7


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Resolve a equação calcula_f = 0.
y = calcula_f(x)

resultado = solve(y)

print (u'\n Resultado da equação x**(log(x + 3,x)) - 7 = 0.')
print ('x =', resultado)
