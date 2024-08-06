"""
Solução de Equações - Sistemas de Equações Lineares 1

"""

# Importa Symbol - possibilidade de operações com símbolos.
# Importa solve - permite solução de equações.
from sympy import Symbol, solve


# Define duas novas funções.
def calcula_f1(x, y):
    return -2 * x + 4 * y - 5


def calcula_f2(x, y):
    return 3 * x - 2 * y - 3


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x e y como variáveis.
x = Symbol('x')
y = Symbol('y')

# Resolve o sistema de equações.
g = calcula_f1(x, y)
h = calcula_f2(x, y)

resultado = solve((g, h))

print (u'\n Resultado do sistema de equações.')
print (resultado)
