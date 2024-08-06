"""
Funções - Polinomiais- Raízes

"""

# Importa função de cálculo de raiz (root) da biblioteca numpy.
from numpy import roots

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define coeficientes da Função do Primeiro Grau 2x + 1.
coeficientes = [2, 1]
raiz = roots(coeficientes)

print (u'\n Raiz da função 2x + 1.')
print (raiz)

# Define coeficientes da Função do Segundo Grau x**2 - 4x + 3.
coeficientes = [1, -4, 3]
raiz = roots(coeficientes)

print (u'\n Raízes da função x**2 - 4x + 3.')
print (raiz)

# Define coeficientes da Função do Segundo Grau x**2 + x + 1.
coeficientes = [1, 1, 1]
raiz = roots(coeficientes)

print (u'\n Raízes da função x**2 + x + 1.')
print (raiz)

# Define coeficientes da Função do Terceiro Grau 3x**3 - 11x**2 + 5x + 3.
coeficientes = [3, -11, 5, 3]
raiz = roots(coeficientes)

print (u'\n Raízes da função 3x**3 - 11x**2 + 5x + 3.')
print (raiz)
