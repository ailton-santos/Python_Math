"""
Matrizes - Sistemas Lineares 1
Autor: Ailton Dos Santos
"""

# Importa biblioteca numpy que permite trabalhar com matrizes.
# Função matrix para definir matrizes.
# Função linalg para fazer matriz inversa.
from numpy import matrix, linalg

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Cria a matriz A.
matriz_A = matrix([
    [2, -5],
    [3, 6]
])

# Cria a matriz B.
matriz_B = matrix([
    [11],
    [3]
])

# Cria a matriz inversa de A.
matriz_A_inv = linalg.inv(matriz_A)

# Resolve o sistema de equações lineares.

solucao = matriz_A_inv * matriz_B

print (u'Resultado do sistema de equações lineares:')
print (solucao)
