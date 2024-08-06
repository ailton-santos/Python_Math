"""
Matrizes - Operações elemento por elemento - Divisão
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

# Divisão, elemento por elemento, da Matriz A pela B.
resultado = matriz_A / matriz_B

print ('\n')
print (u'Divisão, elemento por elemento, da Matriz A pela B -\
                                                            resultado inteiro')
print (resultado)

# Transforma B antes em matriz com valores em ponto flutuante.
resultado = matriz_A / (1.0*matriz_B)

print ('\n')
print (u'Divisão, elemento por elemento, da Matriz A pela B - '\
                                                'resultado em ponto flutuante')
print (resultado)
