"""
Solução de Inequações - Inequação Função Modular

"""

# Importa função Abs de sympy para tratar funções modulares.
# Indica que x é a variável independente de sympy.abc.
# Importa função reduce_abs_inequalities de sympy.solvers.inequalities
# para resolver inequações polinomiais.
from sympy import Abs
from sympy.abc import x
from sympy.solvers.inequalities import reduce_abs_inequalities


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

resultado = reduce_abs_inequalities([(Abs(5 * x + 4) - 3, '>=')], x)

print (u'Solução da inequação |5*x + 4| >= 3')
print (resultado)
print (u'Interpretando resultado:')
print (u'Solução x < -7/5 ou x > -1/5.')
print ('\n')

resultado = reduce_abs_inequalities([(Abs(3 * x - 7) - 2, '<')], x)

print (u'Solução da inequação |3*x - 7| < 2')
print (resultado)
print (u'Interpretando resultado:')
print (u'Solução 5/3 < x < 3.')
print ('\n')

resultado = reduce_abs_inequalities([(Abs(3 * x - 7) + 2, '<')], x)

print (u'Solução da inequação |3*x - 7| < -2')
print (resultado)
print (u'Não existe solução.')
