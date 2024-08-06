"""
Solução de Equações - Trigonométricas 3

"""

# Importa Symbol - possibilidade de operações com símbolos.
# Importa solve - permite solução de equações.
# Importa funções seno (sin), cosseno (cos) e tangente (tan).
from sympy import Symbol, solve, sin, cos, tan


# Define uma nova função.
def calcula_f(x):
    return (sin(2 * x)) ** 2 - cos(2 * x) - tan(2 * x) - 1


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Resolve a equação calcula_f = 0.
y = calcula_f(x)

resultado = solve(y)

print (u'\n Resultado da equação (sin(2*x))**2 - cos(2*x) - tan(2*x) - 1 = 0.')
print ('x =', resultado)
