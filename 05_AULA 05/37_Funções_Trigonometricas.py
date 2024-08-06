"""
Funções - Trigonométricas 1

Autor: Ailton Dos Santos
"""

# Importa funções trigonométricas (sin, cos e tan) da biblioteca math.
# Importa também a constante pi e a função de conversão
# de graus para radianos (radians).
from math import sin, cos, tan, pi, radians


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Usa Função Seno. Argumento em radianos.
y = sin(pi / 2)

print (u'\n Resultado da Função y = sen(pi/2).')
print (u'y =', y)

# Usa Função Cosseno.  Argumento em radianos.
y = cos(pi / 6)

print (u'\n Resultado da Função y = cos(pi/6).')
print ('y =', y)

# Usa Função Tangente. Argumento em radianos.
y = tan(pi / 4)

print (u'\n Resultado da Função y = tan(pi/4).')
print ('y =', y)

# Usa Função Seno. Argumento em graus.
angulo = radians(30)
y = sin(angulo)

print (u'\n Resultado da Função y = sen(30).')
print ('y =', y)

# Usa Função Cosseno. Argumento em graus.
y = cos(radians(120))

print (u'\n Resultado da Função y = cos(120).')
print ('y =', y)

# Usa Função Tangente. Argumento em graus.
y = tan(radians(60))

print (u'\n Resultado da Função y = tan(60).')
print ('y =', y)
