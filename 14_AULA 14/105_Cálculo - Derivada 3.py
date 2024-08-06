#Cálculo - Derivada 3

# Importa operação Derivative (derivada) da biblioteca sympy.
# Importa Symbol - possibilidade de operações com símbolos.
# Importa a função exp (exponencial) da biblioteca sympy.
# Importa a função sin (seno) da biblioteca sympy.
# Importa função N, que permite exibir resultados em ponto flutuante.
from sympy import Derivative, Symbol, exp, sin, N


# Define uma nova função.
def calcula_f(x):
    return exp(3 * x) * sin(x / 3)


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Calcula a derivada de primeira ordem da função calcula_f.
resultado = Derivative(calcula_f(x), x).doit()
# Derivada de primeira ordem da função calcula_f no ponto x = 1.
resultado1 = Derivative(calcula_f(x), x).doit().subs({x: 1})

print (u'\n Derivada de primeira ordem  da função calcula_f.')
print (resultado)
print (u'\n Derivada de primeira ordem  da função calcula_f no ponto x = 1.')
print (resultado1)
print (N(resultado1)) # Apresenta o resultado em ponto flutuante.

# Calcula a derivada de segunda ordem da função calcula_f.
resultado = Derivative(calcula_f(x), x, 2).doit()
# Derivada de segunda ordem da função calcula_f no ponto x = 2.
resultado1 = Derivative(calcula_f(x), x, 2).doit().subs({x: 2})

print (u'\n Derivada de segunda ordem da função calcula_f.')
print (resultado)
print (u'\n Derivada de segunda ordem da função calcula_f no ponto x = 2.')
print (resultado1)
print (N(resultado1))  # Apresenta o resultado em ponto flutuante.

# Calcula a derivada de terceira ordem da função calcula_f.
resultado = Derivative(calcula_f(x), x, 3).doit()
# Derivada de segunda ordem da função calcula_f no ponto x = 0.5.
resultado1 = Derivative(calcula_f(x), x, 3).doit().subs({x: 0.5})

print (u'\n Derivada de terceira ordem da função calcula_f.')
print (resultado)
print (u'\n Derivada de terceira ordem  da função calcula_f no ponto x = 0.5.')
print (resultado1)
