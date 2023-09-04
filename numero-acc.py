# Datos de entrada
accidentes = [0, 1, 2, 3, 4, 5]
prob_accidentes = [0.01, 0.02, 0.72, 0.15, 0.05, 0.05]
vehiculos = ['Moto', 'Carro', 'Panel', 'Autobus', 'Bicicleta', 'Otro']
accidentes_vehiculos = [10, 8, 4, 6, 4, 3]

# Número mínimo y máximo de accidentes en Motocicleta
min_accidentes_moto = 3
max_accidentes_moto = 5

# Cálculo de la distribución de probabilidades conjunta
total_accidentes_vehiculos = sum(accidentes_vehiculos)
prob_vehiculos = [x / total_accidentes_vehiculos for x in accidentes_vehiculos]
prob_conjunta = [[prob_accidentes[i] * prob_vehiculos[j] for j in range(len(vehiculos))] for i in range(len(accidentes))]

# Imprimir la tabla de distribución de probabilidades conjunta
print('Distribución de probabilidades conjunta:')
print('X/Y\t' + '\t'.join(vehiculos))
for i in range(len(accidentes)):
    print(f'{accidentes[i]}\t' + '\t'.join([f'{x:.4f}' for x in prob_conjunta[i]]))

# Cálculo de la probabilidad de que ocurran entre min_accidentes_moto y max_accidentes_moto accidentes en Motocicleta
prob_min_max_accidentes_moto = sum([prob_conjunta[i][0] for i in range(min_accidentes_moto,max_accidentes_moto+1)])
print(f'\nProbabilidad de que ocurran entre {min_accidentes_moto} y {max_accidentes_moto} accidentes en Motocicleta: {prob_min_max_accidentes_moto:.4f}')