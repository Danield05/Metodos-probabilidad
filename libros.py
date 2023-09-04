import math

# Número total de libros por tipo
total_historia = 4
total_musica = 5
total_pintura = 5

# Número total de libros en la caja
total_libros = total_historia + total_musica + total_pintura

# Función para calcular la combinación
def comb(n, r):
    return math.comb(n, r)

# Probabilidad de sacar x libros de música y y libros de pintura
def prob(x, y):
    # Combinaciones de libros de música y pintura
    comb_musica = comb(total_musica, x)
    comb_pintura = comb(total_pintura, y)
    
    # Combinaciones de libros de historia
    comb_historia = comb(total_historia, 3 - x - y)
    
    # Combinaciones totales
    comb_total = comb(total_libros, 3)
    
    return (comb_musica * comb_pintura * comb_historia) / comb_total

# Calcular la probabilidad de obtener a lo sumo 1 libro de música
prob_musica = sum(prob(x, y) for x in range(2) for y in range(4) if x + y <= 3)
print(f'Probabilidad de obtener a lo sumo 1 libro de música: {round(prob_musica, 4)}')
