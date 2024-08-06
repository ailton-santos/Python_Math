"""
Matemática com Python
Um Guia Prático

Matrizes - Definição Flutuante

Exemplo 3.2

Autor: Ailton Dos Santos
"""

# Importa biblioteca numpy que permite trabalhar com matrizes.
# Função matrix para definir matrizes.
# Função zeros para criar matriz com valores 0.
# Função ones para criar matriz com valores 1.
# Função identity para criar matriz identidade.
from numpy import zeros, ones, identity

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Cria uma matriz com todos os elementos iguais a zero ou a um.
matriz_C = zeros((4, 3), dtype='int')  # Matriz com valores inteiros.

print ('\n')
print ('Matriz 4 x 3 com todos os elementos iguais a zero - Inteiros')
print (matriz_C)

# Matriz com valores em ponto flutuante.
matriz_D = ones((2, 3), dtype='float')

print ('\n')
print ('Matriz 2 x 3 com todos os elementos iguais a um - Ponto Flutuante')
print (matriz_D)

# Cria uma matriz com todos os elementos iguais a
#                   um valor escolhido (neste caso 5).
# Matriz com valores de ponto flutuante.
matriz_E = 5 * (ones((4, 2), dtype='float'))

print ('\n')
print ('Matriz 4 x 2 com todos os elementos iguais a 5 - Ponto Flutuante')
print (matriz_E)

# Cria uma matriz identidade 3 x 3
matriz_F = identity(3)

print ('\n')
print ('Matriz identidade 3 x 3')
print (matriz_F)
