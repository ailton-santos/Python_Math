"""

Cálculo - Derivada 1

"""

# Importa operação Derivative (derivada) da biblioteca sympy.
# Importa Symbol - possibilidade de operações com símbolos.
# Importa função N, que permite exibir resultados em ponto flutuante.
from sympy import Derivative, Symbol, N


# Define uma nova função.
def calcula_f(x):
    return 1 / x


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Calcula a derivada da função calcula_f.
resultado = Derivative(calcula_f(x), x).doit()

print (u'\n Derivada da função calcula_f.')
print (resultado)

# Calcula a derivada da função calcula_f no ponto x = 3.
resultado = Derivative(calcula_f(x), x).doit().subs({x: 3})

print (u'\n Derivada da função calcula_f no ponto x = 3.')
print (resultado)
print (N(resultado))
