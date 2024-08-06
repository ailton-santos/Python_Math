"""
Funções - Trigonométricas 2


"""

# Importa a função trigonométrica sin (seno) da biblioteca math.
# Importa também a constante pi.
from math import sin, pi


# Define uma nova função. Neste caso, uma Função Senoidal.
def calcula_f(x):
    return 2 * sin(x / 4)


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Usa Função calcula_f. Argumento em radianos.
y = calcula_f(pi / 2)

print (u'\n Resultado da Função calcula_f para argumento pi/2.')
print ('y =', y)

# Usa Função calcula_f. Argumento em radianos.
y = calcula_f(3 * pi)

print (u'\n Resultado da Função calcula_f para argumento 3*pi.')
print ('y =', y)
