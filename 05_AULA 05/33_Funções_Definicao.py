"""
Funções - Definição 1

Autor: Ailton Dos Santos
"""


# Define uma nova função. Neste caso, de uma única variável independente x.
def calcula_f(x):
    return 2 * x


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Chama a função para calcular o valor para x = 3.0.
x = 3.0
y = calcula_f(x)

print ('Resultado da função calcula_f(x) para x = 3.')
print ('y =', y)
