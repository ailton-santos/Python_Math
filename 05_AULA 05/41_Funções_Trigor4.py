"""
Funções - Trigonométricas 4

Autor: Ailton Dos Santos
"""

# Importa funções trigonométricas (sin e cos) da biblioteca math.
# Importa também a constante pi.
from math import sin, cos, pi


# Define uma nova função. Neste caso, uma Função Trigonométrica.
def calcula_f(x):
    return 2 * sin(x / 4 + pi / 8) + (1 / 4) * (cos(2 * x - pi / 3))**2


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Usa Função calcula_f. Argumento em radianos.
y = calcula_f(pi / 6)

print (u'\n Resultado da Função calcula_f para argumento pi/6.')
print ('y =', y)

# Usa Função calcula_f. Argumento em radianos.
y = calcula_f(3 * pi / 4)

print (u'\n Resultado da Função calcula_f para argumento 3*pi/4.')
print ('y =', y)
