"""
Matrizes - Operações elemento por elemento - Soma e Subtração
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
    [3, 5, 9],
    [1, 6, 8]
])

print ('Matriz A')
print (matriz_A)

# Adiciona a todos os elementos da Matriz A por um valor (4).
matriz_B = matriz_A+4

print ('\n')
print ('Todos os elementos da Matriz A adicionados de 4.')
print (matriz_B)

# Subtrai todos os elementos da Matriz A de 1.
matriz_B = 1-matriz_A

# Como todos os valores são inteiros, o resultado
# apresenta somente suas partes inteiras.
print ('\n')
print ('Todos os elementos da Matriz A subtraídos de 1.')
print (matriz_B)
