"""
Funções - Polinomiais 1

Autor: Ailton José dos Santos
"""


# Define uma nova função. Neste caso, uma Função Polinomial.
def calcula_f(x):
    return 3 * x**3 - 4 * x**2 + 2 * x - 5


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Chama a função para calcular o valor para x = 3.0.
x = 3.0
y = calcula_f(x)

print (u'\n Resultado da função calcula_f para x = 3.0.')
print ('y =', y)
