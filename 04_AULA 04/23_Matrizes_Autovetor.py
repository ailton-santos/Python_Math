"""
Matrizes - Autovalor e Autovetor

Autor: Ailton Dos Santos
"""

# Importa biblioteca numpy que permite trabalhar com matrizes.
# Função matrix para definir matrizes.
# Função linalg para usar elemento de álgebra linear (neste caso eig).
from numpy import matrix, linalg

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Cria matriz A com valores inteiros (int).
matriz_A = matrix([
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3]
])

print ('Matriz A')
print (matriz_A)

# Autovalores e autovetores da matriz A.
resultado = linalg.eig(matriz_A)

print ('\n')
print ('Autovalores da Matriz A.')
print (resultado[0])

print ('\n')
print ('Autovetores da Matriz A.')
print (resultado[1])
