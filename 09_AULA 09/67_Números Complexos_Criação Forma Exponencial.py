""

Números Complexos - Criação Forma Exponencial

"""

# Importa funções de tratamento de números complexos da biblioteca cmath.
# Função exp para função exponencial de base e.
# Importa constante pi.
from cmath import exp, pi

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define um número complexo na forma retangular.
z1 = 5 * exp(1j * pi / 6)  # Número complexo definido na forma exponencial.

print (u'Número complexo módulo = 5 e argumento = pi/6.')
print (u'\n (Forma retangular) z1 =', z1)
