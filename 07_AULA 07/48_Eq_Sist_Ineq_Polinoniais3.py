"""
Solução de Equações - Polinomiais 3
"""
# Importa Symbol - possibilidade de operações com símbolos.
# Importa solve - permite solução de equações.
from sympy import Symbol, solve


# Define uma nova função.
def calcula_f(x):
    return x**2 + x + 1


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Resolve a equação calcula_f = 0.
y = calcula_f(x)

resultado = solve(y)

print (u'\n Resultado da equação x**2 + x + 1 = 0.')
print ('x =', resultado)
