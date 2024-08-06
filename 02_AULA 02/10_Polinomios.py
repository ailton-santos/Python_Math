"""
Operações - Soma e Subtração de Polinômios

Autor: Ailton Dos Santos
"""
# Importa funções de operações com polinômios da biblioteca numpy.
from numpy import polyadd, polysub

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Adição de polinômios.
coeficientes_pol1 = [3, 2, -1]  # Define polinômio 3x**2 + 2x - 1
coeficientes_pol2 = [4, -1, 3]  # Define polinômio 4x**2 - x + 3

resultado = polyadd(coeficientes_pol1, coeficientes_pol2)

print ('Coeficientes do resultado da soma entre 3x**2 + 2x - 1 e\
                                                               4x**2 - x + 3.')
print ('Coeficientes =', resultado)

# Subtração de polinômios.
coeficientes_pol1 = [3, -2, 1]  # Define polinômio 3x**2 - 2x + 1
coeficientes_pol2 = [-2, 0, 4]  # Define polinômio -2x**2 + 4

resultado = polysub(coeficientes_pol1, coeficientes_pol2)

print (u'\nCoeficientes do resultado da subtração de 3x**2 - 2x + 1 '\
                                                              'por 2x**2 + 4.')
print ('Coeficientes =', resultado)
