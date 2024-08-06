"""
Cálculo - Limite 3
"""
# Importa operação Limit (limite) da biblioteca sympy.
# Importa Symbol - possibilidade de operações com símbolos.
# Importa função sympy S que transforma texto em algumas constantes padrão.
from sympy import Limit, Symbol, S, sin

from math import pi  # Importa a constante pi da biblioteca math.


# Define uma nova função.
def calcula_f(x):
    return sin(2 * x) / x


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Calcula limite da função quando x -> 0.
resultado = Limit(calcula_f(x), x, 0).doit()

print (u'\n Limite da função calcula_f para x -> 0.')
print (resultado)

# Calcula limite da função quando x -> pi/6.
resultado = Limit(calcula_f(x), x, pi/6).doit()

print (u'\n Limite da função calcula_f para x -> pi/6.')
print (resultado)

# Calcula limite da função quando x -> oo.
resultado = Limit(calcula_f(x), x, S.Infinity).doit()

print (u'\n Limite da função calcula_f para x -> oo.')
print (resultado)

# Calcula limite da função quando x -> -oo.
resultado = Limit(calcula_f(x), x, -S.Infinity).doit()

print (u'\n Limite da função calcula_f para x -> -oo.')
print (resultado)
