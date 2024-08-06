"""
Operações - Multiplicação de Polinômios

Autor: Ailton Dos Santos
"""

# Importa função de operação com polinômios da biblioteca numpy.
from numpy import polymul

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Multiplicação de polinômios.
coeficientes_pol1 = [2, 4, 0.5]  # Define polinômio 1.
coeficientes_pol2 = [3, 2, 0]  # Define polinômio 2.

resultado1 = polymul(coeficientes_pol1, 2)
resultado2 = polymul(coeficientes_pol1, coeficientes_pol2)

print (u'Coeficientes do resultado da multiplicação de 2x**2 + 4x + 1/2\
                                                                       por 2.')
print ('Coeficientes =', resultado1)
print ('\n')
print (u'Coeficientes do resultado da multiplicação de '\
                                              '2x**2 + 4x + 1/2 e 3x**2 + 2x.')
print ('Coeficientes =', resultado2)
