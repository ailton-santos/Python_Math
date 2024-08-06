"""
Funções - Definição 2

Exemplo 4.2
Autor: Ailton José dos Santos
"""


# Define uma nova função. Neste caso, com duas variáveis independentes x e z.
def calcula_f(x, z):
    return 2 * x + 3 * z


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Chama a função para calcular o valor para x = 3.0 e z = 2.0.
x = 3.0
z = 2.0
y = calcula_f(x, z)

print (u'\n Resultado da função calcula_f para x = 3.0 e z = 2.0.')
print ('y =', y)
