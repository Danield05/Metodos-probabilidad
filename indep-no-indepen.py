import sympy as sp

# Definir el símbolo c
c = sp.symbols('c')

# Definir la función de densidad conjunta h(x, y)
x, y = sp.symbols('x y')
h = c * x**2 * y

# Límites para la integración
x_min = 0
x_max = 1
y_min = 0
y_max = 1

# Encontrar las funciones de densidad marginales f(x) y g(y)
f_x = sp.integrate(h, (y, y_min, y_max))  # Integra h respecto a y en el rango [y_min, y_max]
g_y = sp.integrate(h, (x, x_min, x_max))  # Integra h respecto a x en el rango [x_min, x_max]

# Calcular el valor de la constante c para que la integral sea igual a 1
eq = sp.Eq(sp.integrate(h, (x, x_min, x_max), (y, y_min, y_max)), 1)
c_value = sp.solve(eq, c)

# Verificar si las variables son independientes
if c_value:
    respuesta = 2  # Las variables NO son independientes
else:
    respuesta = 1  # Ambas variables son independientes

print(respuesta)
