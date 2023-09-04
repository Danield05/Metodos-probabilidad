from scipy.integrate import dblquad
from math import sqrt

#esto es para una integral doble
def esperanza(g, h, x_min, x_max, y_min, y_max):
    resultado, error = dblquad(lambda y, x: g(x, y) * h(x, y), x_min, x_max, y_min, y_max)
    return resultado

#funcion E (personalizada) o para x
def g(x, y):
    return ((2*x)+(3*y))

#funcion para y
def g2(x, y):
    return y

#funcion de probabilidad
def h(x, y):
    return (1/210)*(2*x+y)

#limites de integracion
x_min = 0
x_max = 6
y_min = 0
y_max = 5

resultado_integral = esperanza(g, h, x_min, x_max, y_min, y_max)
resultado2_integral = esperanza(g2, h, x_min, x_max, y_min, y_max)
print("Resultado de de esperanza1:", resultado_integral)
print("Resultado de de esperanza2:", resultado2_integral, "\n")

#funcion de varianza
def varianza(g, h, x_min, x_max, y_min, y_max, inter):
    
    resultado, error = dblquad(lambda y, x: (x - inter)**2 * h(x, y), x_min, x_max, y_min, y_max)
    return resultado
print("la varianza 1 es: ", varianza(g, h, x_min, x_max, y_min, y_max, resultado_integral))
print("la varianza 2 es: ", varianza(g2, h, x_min, x_max, y_min, y_max, resultado2_integral),"\n")

#funcion covarianza(x,y)
def covarianza(g, h, x_min, x_max, y_min, y_max):
    
    resultado, error = dblquad(lambda y, x: (x - resultado_integral)*(y - resultado2_integral) * h(x, y), x_min, x_max, y_min, y_max)
    return resultado

print("la covarianza es: ", covarianza(g, h, x_min, x_max, y_min, y_max))


def correlacion():
    return covarianza(g, h, x_min, x_max, y_min, y_max)/((sqrt(varianza(g, h, x_min, x_max, y_min, y_max, resultado_integral))) * sqrt(varianza(g2, h, x_min, x_max, y_min, y_max, resultado2_integral)))

print("la correlacion es: ", correlacion())