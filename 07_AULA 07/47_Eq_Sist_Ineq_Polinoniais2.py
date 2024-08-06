"""
Solução de Equações - Polinomiais 2

Autor: Ailton Dos Santos
"""
# Importa Symbol - possibilidade de operações com símbolos.
# Importa solve - permite solução de equações.
from sympy import Symbol, solve


# Define uma nova função.
def calcula_f(x):
    return x ** 2 - 4 * x + 3


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)


# Define x como uma variável.
x = Symbol('x')

# Resolve a equação calcula_f = 0.
y = calcula_f(x)

resultado = solve(y)

print (u'\n Resultado da equação x**2 - 4*x + 3 = 0.')
print ('x =', resultado)
