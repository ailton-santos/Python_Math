"""
Matrizes - Definição

Exemplo 3.1

Autor: Ailton Dos Santos

"""

# Importa biblioteca numpy que permite trabalhar com matrizes.
# Função matrix para definir matrizes.
from numpy import matrix

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Cria matriz A com valores inteiros (int).
matriz_A = matrix([
    [1, 2, 3],
    [4, 5, 6]
])

# Cria matriz B com valores usando ponto flutuante (float).
matriz_B = matrix([
    [1.0, 2.2, 3.1],
    [4.6, 5.4, 6.7]
])

print ('Matriz A')
print (matriz_A)

print ('\n')
print ('Matriz B')
print (matriz_B)

# Identifica dimensões da Matriz A.
dimensoes_matriz_A = matriz_A.shape

print ('\n')
print (u'Dimensões da Matriz A')
print (dimensoes_matriz_A)

# Busca um elemento da Matriz B.
# Lembrar que para o Python, a primeira linha/Coluna é zero.
elemento_B_L0_C1 = matriz_B[0, 1]

print ('\n')
print (u'Elemento da primeira linha e segunda coluna da Matriz B')
print (elemento_B_L0_C1)
