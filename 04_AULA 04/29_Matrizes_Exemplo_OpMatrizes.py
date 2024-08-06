"""
Matrizes - Operações entre matrizes - Soma e Subtração
Autor: Ailton Dos Santos
"""

# Importa biblioteca numpy que permite trabalhar com matrizes.
# Função matrix para definir matrizes.
from numpy import matrix

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Cria as matrizes A e B com valores inteiros (int).
matriz_A = matrix([
    [7, 2, 4],
    [3, 5, 9]
])

matriz_B = matrix([
    [3, 6, 9],
    [1, 8, 2]
])

print ('Matriz A')
print (matriz_A)

print ('\n')
print ('Matriz B')
print (matriz_B)

# Soma das Matrizes A e B.
resultado = matriz_A + matriz_B

print ('\n')
print ('Soma das Matrizes A e B')
print (resultado)

# Subtação da Matriz A pela Matriz B
resultado = matriz_A - matriz_B

print ('\n')
print (u'Subtração da Matriz A pela Matriz B')
print (resultado)
