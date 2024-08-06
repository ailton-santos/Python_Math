"""

Gráficos - Número Complexo - Retangular

"""

# Importa todas as funções (*) de elaboração de gráficos da biblioteca pylab.
from pylab import *

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define dois números complexos.
z1 = 2 - 5j
z2 = -3 + 2j

# Exibe gráfico na forma polar.
plot([0, z1.real], [0, z1.imag], 'ro-')  # Plota z1.
# Escreve rótulo z1 para identificar no gráfico.
text(z1.real + 0.2, z1.imag + 0.2, 'z1')
plot([0, z2.real], [0, z2.imag], 'b*--')  # Plota z2.
# Escreve rótulo z2 para identificar no gráfico.
text(z2.real + 0.2, z2.imag + 0.2, 'z2')
# Define a faixa de valores dos eixos do gráfico.
axis([-4, 3, -7, 7])

# Inclui os eixos na origem - x = 0 e y = 0.
axhline(y=0, color='k')  # Traça uma linha horizontal em y = 0.
axvline(x=0, color='k')  # Traça uma linha vertical em x = 0.

grid(True)  # Inclui o grid no gráfico.
