"""
Funções - Trigonométricas - Inversas

Autor: Ailton José dos Santos
"""

# Importa funções trigonométricas inversas
# (asin, acos e atan) da biblioteca math.
# Importa também a função de conversão
# radianos para graus (degrees).
from math import asin, acos, atan, degrees

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Usa Função Arco Seno. Resultado em radianos e em graus.
y = asin(0.9)
y_em_graus = degrees(y)

print (u'\n Resultado da Função y = arcsen(0.9) em radianos.')
print ('y =', y)

print ('u\n Resultado da Função y = arcsen(0.9) em graus.')
print ('y =', y_em_graus)

# Usa Função Cosseno. Resultado em radianos e em graus.
y = acos(0.5)
y_em_Graus = degrees(y)

print (u'\n Resultado da Função y = arccos(0.5) em radianos.')
print ('y =', y)

print (u'\n Resultado da Função y = arccos(0.5) em graus.')
print ('y =', y_em_graus)

# Usa Função Tangente. Resultado em radianos.
y = atan(3)

print (u'\n Resultado da Função y = arctan(3) em radianos.')
print ('y =', y)

print (u'\n Resultado da Função y = arctan(3) em graus.')
print ('y =', degrees(y))
