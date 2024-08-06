"""

Solução de Equações - Sistemas de Equações Lineares 2

"""

# Importa Symbol - possibilidade de operações com símbolos.
# Importa solve - permite solução de equações.
from sympy import Symbol, solve


# Define duas novas funções.
def calcula_f1(x, y, z):
    return -2 * x + 4 * y - z - 5


def calcula_f2(x, y, z):
    return 3 * x - 2 * y + 4 * z - 3


def calcula_f3(x, y, z):
    return -x + 5 * y - 4 * z - 3


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x, y e z como variáveis.
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

# Resolve o sistema de equações.
f = calcula_f1(x, y, z)
g = calcula_f2(x, y, z)
h = calcula_f3(x, y, z)

resultado = solve((f, g, h))

print (u'\n Resultado do sistema de equações.')
print (resultado)
