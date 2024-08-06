"""
Solução de Equações - Exponenciais 1

"""

# Importa Symbol - possibilidade de operações com símbolos.
# Importa solve - permite solução de equações.
from sympy import Symbol, solve


# Define uma nova função.
def calcula_f(x):
    return 2**x - 8


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Resolve a equação calcula_f = 0.
y = calcula_f(x)

resultado = solve(y)

print (u'\n Resultado da equação 2**x - 8 = 0.')
print ('x =', resultado)
