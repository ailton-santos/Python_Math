"""
Operações - Fatoração

Autor: Ailton Dos Santos
"""
# Importa x da biblioteca sympy.bac para tratar variável.
# Importa factor da biblioteca sympy para fatoração.
from sympy.abc import x
from sympy import factor

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n'*100)

resultado = factor(x**2 + 3*x)
print (u'Resultado da fatoração do polinômio x**2 + 3*x.')
print (resultado)
print ('\n')

resultado = factor(x**2 - 9)
print (u'Resultado da fatoração do polinômio x**2 - 9.')
print (resultado)
print ('\n')

resultado = factor(x**2 - 4*x + 4)
print (u'Resultado da fatoração do polinômio x**2 - 4*x + 4.')
print (resultado)
print ('\n')

resultado = factor(x**2 + x - 6)
print (u'Resultado da fatoração do polinômio x**2 + x - 6.')
print (resultado)
print ('\n')

resultado = factor(x**3 - 3*x**2 - 10*x + 24)
print (u'Resultado da fatoração do polinômio x**3 - 3*x**2 - 10*x + 24.')
print (resultado)
print ('\n')

resultado = factor(x**3 - 3*x**2 - 10*x)
print (u'Resultado da fatoração do polinômio x**3 - 3*x**2 - 10*x.')
print (resultado)
