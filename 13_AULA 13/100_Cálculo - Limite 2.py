"""
Cálculo - Limite 2

"""

# Importa operação Limit (limite) da biblioteca sympy.
# Importa Symbol - possibilidade de operações com símbolos.
# Importa função sympy S que transforma texto em algumas constantes padrão.
from sympy import Limit, Symbol, S


# Define uma nova função.
def calcula_f(x):
    return (x ** 3 - 1) / (x - 1)


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Calcula limite da função quando x -> 1.
resultado = Limit(calcula_f(x), x, 1).doit()

print (u'\n Limite da função calcula_f para x -> 1.')
print (resultado)

# Calcula limite da função quando x -> oo.
resultado = Limit(calcula_f(x), x, S.Infinity).doit()

print (u'\n Limite da função calcula_f para x -> oo.')
print (resultado)

# Calcula limite da função quando x -> -oo.
resultado = Limit(calcula_f(x), x, -S.Infinity).doit()

print (u'\n Limite da função calcula_f para x -> -oo.')
print (resultado)

# Calcula limite da função quando x -> 1-.
resultado = Limit(calcula_f(x), x, 1, '-').doit()

print (u'\n Limite da função calcula_f para x -> 1-.')
print (resultado)

# Calcula limite da função quando x -> 1+.
resultado = Limit(calcula_f(x), x, 1, '+').doit()

print (u'\n Limite da função calcula_f para x -> 1+.')
print (resultado)
