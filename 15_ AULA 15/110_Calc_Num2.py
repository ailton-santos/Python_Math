"""
Cálculo Numérico - Zero de Funções - Método da Falsa Posição

"""


# Define uma nova função.
def calcula_f(x):
    return x ** 3 + 5 * x ** 2 - 5 * x - 12


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

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

# Define faixa de valores da variável independente x
# para se buscar a raiz da função.
# Importante 1: f(a) deve ter sinal trocado em relação a f(b).
# Importante 2: os valores de a e b devem ser definidos como ponto flutuante.
a = -6.0  # Limite inferior.
b = -4.0  # Limite superior.

y1 = calcula_f(a)  # Calcula o valor da função para x = a.
y2 = calcula_f(b)  # Calcula o valor da função para x = b.

# Estabelece um valor inicial para c_anterior.
# Este pode ser um valor qualquer que faça com que
# o método não atinja um dos critérios de parada
# (c - c_anterior < erro) antes da primeira iteração.
c_anterior = 2*b

if y1*y2 > 0:
    # Exibe este erro se a função não muda de sinal entre a e b.
    # Execução para por não ter como aplicar o método.
    print (u'erro de Execução - Redefinir valores de a e b.')

else:

    while parar == 0:
        iteracao = iteracao + 1  # Incrementa contador de iterações.

        # Encontra valor de c.
        # Valor de x em que a reta imginária
        # entre a e b cruza eixo das abscissas.
        c = b - (y2 * (b - a)) / (y2 - y1)

        yc = calcula_f(c)  # Verifica o valor da função em x = c.

        # Decide se o valor a ser substituído para a próxima iteração é a ou b.
        if y1 * yc > 0:
            a = c  # f(c) e f(a) possuem o mesmo sinal. Faz a = c.

        if y2 * yc > 0:
            b = c  # f(c) e f(b) possuem o mesmo sinal. Faz b = c.

        # Calcula o erro entre o valor anterior e o atual.
        # Usa somente o valor absoluto.
        erro = abs(c - c_anterior)

        c_anterior = c  # Prepara para próxima iteração (se ocorrer).

        if (iteracao > iteracao_maxima) or (erro < erro_definido):
            # Se um dos critérios de parada é atingido, muda valor de parar.
            # parar = 1 faz o loop while encerrar e o
            # programa terminar sua execução.
            parar = 1

    # Imprime valores obtidos.
    print (u'Total de Iterações')
    print (iteracao)

    print ('\nValor de x')
    print ('x = ', c)

    print ('\nerro encontrado')
    print ('erro = ', erro)
