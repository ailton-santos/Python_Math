"""
Matrizes - Ordenação

Autor: Ailton Dos Santos
"""

# Importa biblioteca numpy que permite trabalhar com matrizes.
# Função matrix para definir matrizes.
# Função argsort para fazer ordenação de matriz.
from numpy import matrix, argsort

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

# Organizar as linhas da Matriz A por ordem crescente
# dos valores da primeira coluna.
# As linhas são mantidas inalteradas. Somente trocam de posição na
# matriz para refletir a ordenação desejada.
# Esta operação faz a variável indice receber a nova ordem da matriz.
indice = matriz_A[:, 0].argsort(axis=0)

# Esta operação faz a nova matriz receber os valores da
# matriz A com as linhas ordenadas.
matriz_A_ordenada = matriz_A[indice, :]

print ('\n')
print ('Matriz A ordenada por ordem crescente dos valores da primeira coluna')
print (matriz_A_ordenada)
