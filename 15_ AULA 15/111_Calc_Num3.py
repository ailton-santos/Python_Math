"""
Cálculo Numérico - Zero de Funções - Método de Newton-Raphson
"""

# Importa operação Derivative (derivada) da biblioteca sympy.
# Importa Symbol - possibilidade de operações com símbolos.
from sympy import Derivative, Symbol


# Define uma nova função.
def calcula_f(x):
    return x ** 3 + 5 * x ** 2 - 5 * x - 12


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Define valores de controle.
# Define número máximo de iterações.
# Se o método não convergir, este será o critério de parada.
iteracao_maxima = 100

iteracao = 0  # Contador de iterações. Inicializa com 0.
# Erro máximo definido como critério de parada do método.
erro_definido = 0.0001

# Variável de controle do loop de repetição do método.
# Quando um dos critérios de parada do método for atingido
# (iterações máximas ou erro definido) seu valor muda para 1.
parar = 0

# Define primeiro valor da variável independente
# x para se buscar a raiz da função.
x0 = -5.0  # Estimativa inicial para a raiz.

while parar == 0:
    iteracao = iteracao + 1  # Incrementa contador de iterações.

    f_x0 = calcula_f(x0)  # Calcula valor da função em x = x0.

    d = Derivative(calcula_f(x), x)  # Calcula derivada da função.
    # Calcula valor da derivada da função em x = x0.
    f_linha_x0 = d.doit().subs({x: x0})

    # Calcula próxima estimativa para a raiz da função.
    x1 = x0 - (f_x0 / f_linha_x0)

    # Calcula o erro entre o valor anterior e o atual.
    # Usa somente o valor absoluto.
    erro = abs(x0 - x1)

    x0 = x1  # Atualiza variável x0 com a nova estimativa.

    if (iteracao > iteracao_maxima) or (erro < erro_definido):
        # Se um dos critérios de parada é atingido, muda valor de parar.
        # parar = 1 faz o loop while encerrar
        # e o programa terminar sua execução.
        parar = 1

# Imprime valores obtidos.
print (u'Total de Iterações')
print (iteracao)

print ('\nValor de x')
print ('x = ', x0)

print ('\nerro encontrado')
print ('erro = ', erro)
