"""
Matrizes - Transposta

Autor: Ailton Dos Santos
"""

# Importa biblioteca numpy que permite trabalhar com matrizes.
# Função matrix para definir matrizes.
# Função transpose para fazer matriz transposta.
from numpy import matrix, transpose

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Cria matriz A com valores inteiros (int).
matriz_A = matrix([
    [7, 2, 4],
    [3, 5, 9]
])

print (' Matriz A')
print (matriz_A)

# Cria a matriz transposta de A.
matriz_A_t = transpose(matriz_A)

print ('\n')
print ('Matriz A Transposta')
print (matriz_A_t)
