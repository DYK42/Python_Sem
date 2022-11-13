import sympy.polys.polytools
from sympy import *
from sympy.plotting import plot
import intersection
import variables

init_printing()


def draw_func():
    x = Symbol('x')
    f1 = variables.f1
    f2 = variables.f2
    pfun1 = plot(f1, line_color='red', title='f1 and f2', show=False)
    pfun2 = plot(f2, line_color='blue', show=False)
    pfun1.append(pfun2[0])
    pfun1.show()


def draw_general_func():
    poly_sum = intersection.get_poly_sum()
    plot(poly_sum, line_color='green', title='general function')
