"""

Números Complexos - Conversão e parâmetros 1

"""

# Importa funções de tratamento de números complexos da biblioteca cmath.
# Função polar para conversão da forma retangular para a polar.
# Função phase para identificar o argumento de um número complexo.
from cmath import polar, phase
# Importa função de conversão de radianos para graus.
from math import degrees
# Importa função conj da biblioteca numpy para
# encontrar o conjugado de número complexo.
from numpy import conj

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define um número complexo na forma retangular.
z1 = -3 + 4j

print (u'Número complexo -3 + 4j.')
print ('\n (Forma retangular) z1 =', z1)
print ('\n Conjungado de z1 =', conj(z1))
print ('\n Parte Real de z1 =', z1.real)
print (u'\n Parte Imaginária de z1 =', z1.imag)
print ('\n (Forma Polar) z1 =', polar(z1))  # Conversão de z1 para forma polar.
print (u'\n Módulo de z1 =', abs(z1))
print ('\n Argumento (radianos) de z1 =', phase(z1))
print ('\n Argumento (graus) de z1 =', degrees(phase(z1)))
