"""
Matrizes - Operações elemento por elemento - Multiplicação e Divisão

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


# Multiplica todos os elementos da Matriz A por um valor (3).
matriz_B = matriz_A*3

print ('\n')
print ('Todos os elementos da Matriz A multiplicados por 3.')
print (matriz_B)

# Divide todos os elementos da Matriz A por 2.
matriz_B = matriz_A/2

# Como todos os valores são inteiros, o resultado
# apresenta somente suas partes inteiras.
print ('\n')
print ('Todos os elementos da Matriz A divididos por 2 - Resultado Inteiro.')
print (matriz_B)

# Se a opção for pelo resultado em pontos flutuantes,
# basta definir o divisor desta forma.
matriz_B = matriz_A/2.0

print ('\n')
print ('Todos os elementos da Matriz A divididos por 2 - '\
                                                  'Resultado Ponto Flutuante.')
print (matriz_B)
