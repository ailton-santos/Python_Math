"""
Cálculo - Integral 2

"""

# Importa operação Integral da biblioteca sympy.
# Importa Symbol - possibilidade de operações com símbolos.
# Importa a função exp (exponencial) da biblioteca sympy.
# Importa função N, que permite exibir resultados em ponto flutuante.
from sympy import Integral, Symbol, N, exp


# Define uma nova função.
def calcula_f(x):
    return x ** 2 * exp(x)


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Calcula a integral indefinida da função calcula_f.
resultado = Integral(calcula_f(x), x).doit()

print (u'\n Integral indefinida da função calcula_f.')
print (resultado)

# Calcula a integral definida da função calcula_fpara x entre 0 e 2.
resultado = Integral(calcula_f(x), (x, 0, 2)).doit()

print (u'\n Integral definida da função calcula_f para x entre 0 e 2.')
print (resultado)
print (N(resultado))  # Resultado em ponto flutuante.
