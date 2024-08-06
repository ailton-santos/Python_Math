"""
Matemática com Python
Um Guia Prático

Matrizes - Operações elemento por elemento - Potência

Exemplo 3.13

Autor: Ailton Dos Santos
"""

# Importa biblioteca numpy que permite trabalhar com matrizes.
# Função matrix para definir matrizes.
# Função power para fazer a potência dos elementos da matriz.
from numpy import matrix, power

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

# Eleva todos os elementos da Matriz A ao cubo.
matriz_B = power(matriz_A, 3)

print ('\n')
print ('Todos os elementos da Matriz A elevados ao cubo.')
print (matriz_B)
