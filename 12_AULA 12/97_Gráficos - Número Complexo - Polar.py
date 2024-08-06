"""
Gráficos - Número Complexo - Polar

"""

# Importa todas as funções (*) de elaboração de gráficos da biblioteca pylab.
from pylab import *

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define dois números complexos.
z1 = 2 - 5j
z2 = -3 + 2j

# Exibe gráfico na forma polar.
# [0,angle(z1)] e [0,angle(z2)] – indica o ângulo do número complexo no gráfico
# [0,abs(z1)] e [0,abs(z2)]– indica o módulo do número complexo no gráfico
# marker - indica o tipo de marcador utilizado.
polar([0, angle(z1)], [0, abs(z1)], marker='o')
polar([0, angle(z2)], [0, abs(z2)], marker='*')
