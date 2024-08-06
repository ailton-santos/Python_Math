"""
Funções - Exponenciais 2

Autor: Ailton Dos Santos
"""

# Importa função exp (exponencial) da biblioteca math.
from math import exp


# Define uma nova função. Neste caso, uma Função Exponencial.
def calcula_f(x):
    return 2 * exp(3 * x)


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Chama a função para calcular o valor para x = 3.0.
x = 3.0
y = calcula_f(x)

print (u'\n Resultado da função calcula_f para x = 3.0.')
print ('y =', y)

# Chama a função para calcular o valor para x = 1.0/2.
# Neste caso, para que a operação seja feita com ponto flutuante,
# numerador ou denominador (ou ambos) deve ser escrito usando sua casa decimal.
x = 1.0 / 2
y = calcula_f(x)

print (u'\n Resultado da função calcula_f para x = 1.0/2.')
print ('y =', y)
