"""
Funções - Exponenciais 1

Autor: Ailton Dos Santos

"""


# Define uma nova função. Neste caso, uma Função Exponencial.
def calcula_f(a, x):
    return 3 * a**(x / 2)


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Chama a função para calcular o valor quando a = 2 e x = 4.
a = 2
x = 4.0
y = calcula_f(a, x)

print (u'Resultado da função calcula_f de base a = 2 e x = 4.0.')
print ('y =', y)

# Chama a função para calcular o valor quando a = 3 e x = 3.0.
a = 3
x = 3.0
y = calcula_f(a, x)

print (u'\nResultado da função calcula_f de base a = 3 e x = 3.0.')
print ('y =', y)
