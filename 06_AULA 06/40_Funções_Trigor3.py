"""
Funções - Trigonométricas 3

Autor: Ailton Dos Santos
"""

# Importa funções trigonométricas (sin, cos e tan) da biblioteca math.
# Importa também a constante pi.
from math import sin, cos, tan, pi


# Define uma nova função. Neste caso, uma Função Trigonométrica.
def calcula_f(x):
    return 2 * sin(x / 4 + pi / 8) + (1.0 / 4) * \
                            cos(2 * x - pi / 2) - (1.0 / 3) * tan(x + pi)


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Usa Função calcula_f. Argumento em radianos.
y = calcula_f(pi / 4)

print (u'\n Resultado da Função calcula_f para argumento pi/2.')
print ('y =', y)

# Usa Função calcula_f. Argumento em radianos.
y = calcula_f(3 * pi / 4)

print (u'\n Resultado da Função calcula_f para argumento 3*pi/2.')
print ('y =', y)
