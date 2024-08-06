"""

Solução de Inequações - Inequação Racional

"""

# Importa função Poly, para definir polinômio.
# Indica que x é a variável independente de sympy.abc.
# Importa função solve_rational_inequalities de sympy.solvers.inequalities
# para resolver inequações racionais.
from sympy import Poly
from sympy.abc import x
from sympy.solvers.inequalities import solve_rational_inequalities


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Resolve inequação [(x-1)/(x+4)] <= 0
resultado = solve_rational_inequalities([[((
                                        Poly(x - 1), Poly(x + 4)), '<='), ]])
print (u'Solução da inequação [(x-1)/(x+4)] <= 0')
print (resultado)
print (u'Interpretando resultado:')
print (u'Solução -4 < x <= 1.')
print ('\n')

# Resolve inequação [(x-1)/(x+4)] > 0
resultado = solve_rational_inequalities([[((
                                        Poly(x - 1), Poly(x + 4)), '>'), ]])
print (u'Solução da inequação [(x-1)/(x+4)] > 0')
print (resultado)
print (u'Interpretando resultado:')
print (u'Solução x < -4 ou x > 1.')
print ('\n')

# Resolve inequação [(x-1)/(x+4)] > 0
resultado = solve_rational_inequalities([[((
                                    Poly(x**2 - 1), Poly(x + 3)), '!='), ]])
print (u'Solução da inequação [(x**2 - 1)/(x + 3)] != 0')
print (resultado)
print (u'Interpretando resultado:')
print (u'Solução x < -3 ou -3 < x < -1 ou -1 < x < 1 ou x > 1.')
