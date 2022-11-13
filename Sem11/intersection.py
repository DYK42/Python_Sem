import sympy.polys.polytools
from sympy import *
import variables


def get_poly_sum():
    f1 = variables.f1
    f2 = variables.f2
    poly1 = sympy.polys.polytools.poly_from_expr(str(f1))[0]
    poly2 = sympy.polys.polytools.poly_from_expr(str(f2))[0]
    return (poly1 + poly2).as_expr()


def get_intersection():
    x = Symbol('x')
    poly_sum = get_poly_sum()
    lst = solve(poly_sum, x)
    return lst


if __name__ == '__main__':
    p = get_poly_sum()
    print(p)
