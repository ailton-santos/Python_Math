"""
Números Complexos - Operações com Funções

"""

# Importa funções de tratamento de números complexos da biblioteca cmath.
# Função exp para função exponencial de base e.
# Função log para cálculo do logaritmo.
# Funções trigonométricas seno (sin), cosseno (cos) e tangente (tan).
from cmath import exp, log, sin, cos, tan, pi

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define dois números complexos.
z1 = 2 - 5j  # Número complexo definido na forma retangular.
z2 = 4 * exp(1j * pi / 3)  # Número complexo definido na forma exponencial.

print ('z1 = ', z1)
print ('z2 = ', z2)
print ('exp(z1) = ', exp(z1))  # Exponencial de número complexo.
print ('log(z2) = ', log(z2, 4))  # Logaritmo de número complexo.
print ('sen(z1) = ', sin(z1)) # Seno de número complexos.
print ('cos(z2) = ', cos(z2))  # Cosseno de número complexos.
print ('tan(z1) = ', tan(z1)) # Tangente de número complexos.
