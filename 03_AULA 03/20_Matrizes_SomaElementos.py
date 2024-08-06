"""
Matrizes - Soma dos Elementos

Autor: Ailton Dos Santos

"""

# Importa biblioteca numpy que permite trabalhar com matrizes.
# Função matrix para definir matrizes.
from numpy import matrix

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Cria matriz A com valores inteiros (int).
matriz_A = matrix([
    [7, 2, 4],
    [3, 5, 9]
])

print (' Matriz A')
print (matriz_A)

# Soma dos elementos da Matriz A por coluna.
soma_colunas_A = matriz_A.sum(axis=0)

print ('\n')
print ('Soma dos elementos das colunas da Matriz A')
print (soma_colunas_A)

# Soma dos elementos da Matriz A por linha.
soma_linhas_A = matriz_A.sum(axis=1)

print ('\n')
print ('Soma dos elementos das linhas da Matriz A')
print (soma_linhas_A)

# Soma de todos os elementos da Matriz A.
soma_A = matriz_A.sum()

print ('\n')
print ('Soma de todos os elementos da Matriz A')
print (soma_A)
