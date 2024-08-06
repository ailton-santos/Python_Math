"""
Números Complexos - Operações

"""

# Importa função sqrt para cálculo de raiz quadrada
# de números complexos da biblioteca cmath.
from cmath import sqrt, pi, exp

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define dois números complexos.
z1 = 2 - 5j  # Número complexo definido na forma retangular.
z2 = 4 * exp(1j * pi / 3)  # Número complexo definido na forma exponencial.

print (z1)
print (z2)
print ('z1 + z2 = ', z1 + z2) # Soma de números complexos.
print ('z1 - z2 = ', z1 - z2)  # Subtração de números complexos.
print ('z1 * z2 = ', z1 * z2)  # Multiplicação de números complexos.
print ('z1 / z2 = ', z1 / z2)  # Divisão de números complexos.
print ('z1**z2 = ', z1**z2)  # Potenciação de números complexos.
print ('sqrt(z1) = ', sqrt(z1))  # Raiz quadrada de número complexo.
