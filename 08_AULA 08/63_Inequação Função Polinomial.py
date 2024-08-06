"""
Solução de Inequações - Inequação Função Polinomial

"""

# Importa função Poly, para definir polinômio.
# Indica que x é a variável independente de sympy.abc.
# Importa função solve_poly_inequality de sympy.solvers.inequalities
# para resolver inequações polinomiais.
from sympy import Poly
from sympy.abc import x
from sympy.solvers.inequalities import solve_poly_inequality


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

resultado = solve_poly_inequality(Poly(3 * x - 7, x), '!=')
print (u'Solução da inequação 3*x - 7 != 0')
print (resultado)
print (u'Interpretando resultado:')
print (u'Solução x < 7/3 ou x > 7/3. Que é o mesmo que x != 7/3.')
print ('\n')

resultado = solve_poly_inequality(Poly(x**2 + x - 6, x), '<=')
print (u'Solução da inequação x**2 + x - 6 <= 0')
print (resultado)
print (u'Interpretando resultado:')
print (u'Solução -3 <= x <= 2.')
print ('\n')

resultado = solve_poly_inequality(
                            Poly(x**3 - 3 * x**2 - 10 * x + 24, x), '>')

print (u'Solução da inequação x**3 - 3*x**2 - 10*x + 24 > 0')
print (resultado)
print (u'Interpretando resultado:')
print (u'Solução -3 < x < 2 ou x > 4.')
