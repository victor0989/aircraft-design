#In [6]:
sympy.solve(C_eq)
Out[6]:
[3]

#The value of the constant of integration is 3, therefore our solution to the initial value problem is:
y(x)=3+ex3−ex
#Another constants for differential equations
In [7]:
# Solution potential series
f = y(x)**2 + x**2 -1
sympy.dsolve(y(x).diff(x) - f)
Out[7]:y(x)=x33(C1(3C1−1)+1)+x560(C1(4C1−7)+10C1−6)+C1+C1x+C1x2+C1x412+O(x6)
# Direction Fields is a simple but useful technique for visualizing possible solutions to first order differential equations:
dydx=f(x,y(x))
# iterate over x values on the coordinate grid of interest and evaluate f(x,y(x))
# Direction Fields are useful because smooth, 
#continuous curves that are tangent to the slope lines at each point on the graph are possible solutions to the Ordinary 
# Differential Equation.
In [8]: 
def plot_direction_field(x, y_x, f_xy, x_lim=(-5, 5), y_lim=(-5, 5), ax=None):
    """Esta función dibuja el campo de dirección de una EDO"""
    
    f_np = sympy.lambdify((x, y_x), f_xy, modules='numpy')
    x_vec = np.linspace(x_lim[0], x_lim[1], 20)
    y_vec = np.linspace(y_lim[0], y_lim[1], 20)
    
    if ax is None:
        _, ax = plt.subplots(figsize=(4, 4))
    
    dx = x_vec[1] - x_vec[0]
    dy = y_vec[1] - y_vec[0]
    
    for m, xx in enumerate(x_vec):
        for n, yy in enumerate(y_vec):
            Dy = f_np(xx, yy) * dx
            Dx = 0.8 * dx**2 / np.sqrt(dx**2 + Dy**2)
            Dy = 0.8 * Dy*dy / np.sqrt(dx**2 + Dy**2)
            ax.plot([xx - Dx/2, xx + Dx/2],
                    [yy - Dy/2, yy + Dy/2], 'b', lw=0.5)
    
    ax.axis('tight')
    ax.set_title(r"$%s$" %
                 (sympy.latex(sympy.Eq(y(x).diff(x), f_xy))),
                 fontsize=18)
    
    return ax

# solution, defining the equation variables
x = sympy.symbols('x')
y = sympy.Function('y')

# function f = y(x)**2 + x**2 -1
f = y(x)**2 + x**2 -1

# topology field
fig, axes = plt.subplots(1, 1, figsize=(8, 6))
campo_dir = plot_direction_field(x, y(x), f, ax=axes)
