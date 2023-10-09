# y=f(x) = () is a function, then its derivative is dy/dx
# In many natural processes,the variables involved and their rate of change are connected to each other through 
# basic scientific principles.
# F=ma, The derivative position of the object with respect to time, which is the same as saying that g=d2u/dt2
# F(x,y,y′,y′′,…,y(n))=0 , dyg(y)=f(x)dx
# In many physical problems we must find a particular solution that satisfies a condition of the form y(to)=y0 
# equation-form is ydx+P(x)y=Q(x)
# A power series is a series, generally infinite and 
# The domain of this function will be given by the set of all X for which the series converges.

#1st function system with matplotlib
In [1]:
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import sympy 
from scipy import integrate
# math notation init print functions
sympy.init_printing(use_latex='mathjax')
x = sympy.Symbol('x')
y = sympy.Function('y')

# expreso la ecuacion
f = 6*x**2 - 3*x**2*(y(x))
sympy.Eq(y(x).diff(x), f)

#2nd functional system for differential equations with matplotlib
In[3]: sympy.dsolve(y(x).diff(x) - f)
out[3]:y(x)=C1e−x3+2

#3rd differential equation-system
In [4]:
# defining the equation
eq = 1.0/2 * (y(x)**2 - 1)

# Initial condition
ics = {y(0): 2}

# computing the differential equation for diferent applications
edo_sol = sympy.dsolve(y(x).diff(x) - eq)
edo_sol
Out[4]:y(x)=C1+exC1−ex

#4our system for motion
In [5]:
C_eq = sympy.Eq(edo_sol.lhs.subs(x, 0).subs(ics), edo_sol.rhs.subs(x, 0))
C_eq
Out[5]:2=C1+1C1−1
# Finally, we solve for the value of the constant of integration by solving the equation
In [6]:
sympy.solve(C_eq)
Out[6]:
[3]


