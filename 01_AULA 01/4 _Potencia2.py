"""
Operações - Potenciação 2
Autor: Ailton Dos Santos
"""

# Importa função pow (potência) da biblioteca math.
from math import pow

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores.
a = 2
b = 6

# Operações com potências.

a_quadrado = pow(a, 2)
a_cubo = pow(a, 3)
a_quarta = pow(a, 4)
a_elevado_b = pow(a, b)

print (u'Resultado das operações de potência.')
print ('a =', a)
print ('b =', b)
print ('a ao quadrado =', a_quadrado)
print ('a ao cubo =', a_cubo)
print ('a a quarta =', a_quarta)
print ('a elevado a b =', a_elevado_b)
