"""
Matrizes - Operações entre matrizes - Multiplicação
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
    [3, 9],
    [5, 8],
    [7, 6]
])

print ('Matriz A')
print (matriz_A)

print ('\n')
print ('Matriz B')
print (matriz_B)

# Multiplicação da Matriz A pela B.
resultado = matriz_A * matriz_B

print ('\n')
print (u'Multiplicação da Matriz A pela B')
print (resultado)
