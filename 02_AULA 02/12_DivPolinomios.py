"""
Operações - Divisão de Polinômios

Autor: Ailton Dos Santos
"""

# Importa função de operação com polinômios da biblioteca numpy.
from numpy import polydiv

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Divisão de polinômios.
coeficientes_pol1 = [4, 6, 3, 2]  # Define polinômio 1.
coeficientes_pol2 = [2, 1, 2]  # Define polinômio 2.

resultado1 = polydiv(coeficientes_pol1, 2)
resultado2 = polydiv(coeficientes_pol1, coeficientes_pol2)

print (u'Coeficientes do resultado da divisão de 4x**3 + 6x**2 + 3x + 2 por 2.')
print ('Coeficientes =', resultado1)
print ('Interpretando o Resultado:')
print ('Quociente 2x**3 + 3x**2 + 1.5x + 1 / Resto 0.')
print ('\n')
print (u'Coeficientes do resultado da divisão de '\
                                   '4x**3 + 6x**2 + 3x + 2 por 2x**2 + x + 2.')
print ('Coeficientes =', resultado2)
print ('Interpretando o Resultado:')
print ('Quociente 2x + 2 / Resto -3x - 2.')
