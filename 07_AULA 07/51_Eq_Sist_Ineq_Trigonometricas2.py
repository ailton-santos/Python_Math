"""
Solução de Equações - Trigonométricas 2

"""

# Importa Symbol - possibilidade de operações com símbolos.
# Importa solve - permite solução de equações.
# Importa função cosseno (cos).
from sympy import Symbol, solve, cos


# Define uma nova função.
def calcula_f(x):
    return 4 * (cos(x))**2 - 3


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Resolve a equação calcula_f = 0.
y = calcula_f(x)

resultado = solve(y)

print (u'\n Resultado da equação 4*(cos(x))**2 - 3 = 0.')
print ('x =', resultado)
