"""
Solução de Equações - Sistemas de Equações Não Lineares 2

"""

# Importa Symbol - possibilidade de operações com símbolos.
# Importa solve - permite solução de equações.
from sympy import Symbol, solve


# Define duas novas funções.
def calcula_f1(x, y):
    return (x**2 / 3) + y ** 2 - 1


def calcula_f2(x, y):
    return x**2 + (y**2 / 4) - 1


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x e y como variáveis.
x = Symbol('x')
y = Symbol('y')

# Resolve o sistema de equações.
f = calcula_f1(x, y)
g = calcula_f2(x, y)

resultado = solve((f, g))

print (u'\n Resultado do sistema de equações.')
print (resultado)
