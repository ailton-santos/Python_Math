"""
Operações - Floor e Ceil (Teto e Chão)

Autor: Ailton Dos Santos
"""

# Importa funções ceil e floor da biblioteca math.
from math import ceil, floor

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores.
a = 3.456
b = 7.890

# Operações inteiras.
#floor retorna maior numero interio menor do que a.
#floor retorna menor numero interio maior do que a.

piso_a = floor(a)
teto_a = ceil(a)

piso_b = floor(b)
teto_b = ceil(b)

print (u'Resultado das operações inteiras.')
print ('a =', a)
print ('Piso de a =', piso_a)
print ('Teto de a =', teto_a)
print ('\n')
print ('b =', b)
print ('Piso de b =', piso_b)
print ('Teto de b =', teto_b)
