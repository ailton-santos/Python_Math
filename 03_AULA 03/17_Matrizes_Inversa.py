"""
Matrizes - Inversa

Autor: Ailton Dos Santos
"""

# Importa biblioteca numpy que permite trabalhar com matrizes.
# Função matrix para definir matrizes.
# Função linalg para fazer matriz inversa.
from numpy import matrix, linalg

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Cria matriz A com valores inteiros (int).
matriz_A = matrix([
    [7, 2, 4],
    [3, 5, 9],
    [1, 6, 8]
])

print ('Matriz A')
print (matriz_A)

# Cria a matriz inversa de A.
matriz_A_inv = linalg.inv(matriz_A)

print ('\n')
print ('Matriz Inversa de A')
print (matriz_A_inv)
