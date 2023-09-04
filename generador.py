class GeneradorCongruencialMixto:
    def __init__(self, seed, a, c, m):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def generar(self, n):
        numeros_generados = []
        for _ in range(n):
            self.state = (self.a * self.state + self.c) % self.m
            numeros_generados.append(self.state / self.m)
        return numeros_generados

# Parámetros del generador
# seed = 0  # Semilla inicial
# a = 22073  # Multiplicador
# c = 8485  # Incremento
# m = 32768  # Módulo


seed = 0  # Semilla inicial
a = 13  # Multiplicador
c = 5  # Incremento
m = 11  # Módulo

# Crear instancia del generador
generador = GeneradorCongruencialMixto(seed, a, c, m)

# Generar 10 números pseudoaleatorios
numeros_aleatorios = generador.generar(15)

# Imprimir los números generados
for i, numero in enumerate(numeros_aleatorios, start=1):
    print(f"Número {i}: {numero}")

# El valor mas pequeño de la lista que no sea 0
minimo = 1
for i in numeros_aleatorios:
    if i < minimo and i != 0:
        minimo = i

print("El valor mas pequeño de la lista que no sea 0 es: ", minimo)